package io.kb.app.ui.browse

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import io.kb.app.data.FakeConceptRepository
import io.kb.app.data.ProgressStatus
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

class BrowseViewModel(
    private val repository: FakeConceptRepository,
) : ViewModel() {

    private val _uiState = MutableStateFlow(BrowseUiState())
    val uiState: StateFlow<BrowseUiState> = _uiState.asStateFlow()

    init {
        load()
        viewModelScope.launch {
            repository.progress.collect { progress ->
                _uiState.update { it.copy(progress = progress) }
            }
        }
    }

    fun load() {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true, error = null) }
            _uiState.update {
                it.copy(
                    groups = repository.groupedSummaries(),
                    isLoading = false,
                )
            }
        }
    }

    fun setStatusFilter(status: ProgressStatus?) {
        _uiState.update { it.copy(statusFilter = status) }
    }
}
