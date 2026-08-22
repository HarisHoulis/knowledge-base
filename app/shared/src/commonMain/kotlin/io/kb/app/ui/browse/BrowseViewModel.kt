package io.kb.app.ui.browse

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import io.kb.app.data.ConceptRepository
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharedFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

sealed interface BrowseEvent {
    data class Error(val message: String) : BrowseEvent
}

class BrowseViewModel(
    private val repository: ConceptRepository,
) : ViewModel() {

    private val _uiState = MutableStateFlow(BrowseUiState())
    val uiState: StateFlow<BrowseUiState> = _uiState.asStateFlow()

    private val _events = MutableSharedFlow<BrowseEvent>()
    val events: SharedFlow<BrowseEvent> = _events.asSharedFlow()

    init {
        load()
    }

    fun load() {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true, error = null) }
            runCatching { repository.domains() }
                .onSuccess { domains ->
                    _uiState.update { it.copy(domains = domains, isLoading = false) }
                }
                .onFailure { e ->
                    _uiState.update { it.copy(isLoading = false, error = e.message) }
                    _events.emit(BrowseEvent.Error(e.message ?: "Failed to load domains"))
                }
        }
    }
}
