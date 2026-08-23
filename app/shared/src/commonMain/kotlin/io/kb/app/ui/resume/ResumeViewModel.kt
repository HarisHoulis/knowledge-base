package io.kb.app.ui.resume

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import io.kb.app.data.FakeConceptRepository
import io.kb.app.data.Progress
import io.kb.app.data.ProgressStatus
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class ResumeUiState(
    val items: List<ResumeItem> = emptyList(),
    val isLoading: Boolean = true,
    val error: String? = null,
)

data class ResumeItem(
    val id: String,
    val title: String,
    val subdomainName: String,
    val status: ProgressStatus,
    val position: Int,
    val bodyLength: Int,
)

class ResumeViewModel(
    private val repository: FakeConceptRepository,
) : ViewModel() {

    private val _uiState = MutableStateFlow(ResumeUiState())
    val uiState: StateFlow<ResumeUiState> = _uiState.asStateFlow()

    init {
        load()
        viewModelScope.launch {
            repository.progress.collect { load() }
        }
    }

    fun load() {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true, error = null) }
            val items = repository.resumeSummaries().map { summary ->
                val detail = repository.detail(summary.id)
                ResumeItem(
                    id = summary.id,
                    title = summary.title,
                    subdomainName = summary.subdomainSlug,
                    status = summary.progress.status,
                    position = summary.progress.position,
                    bodyLength = detail.body.length,
                )
            }
            _uiState.update { it.copy(items = items, isLoading = false) }
        }
    }
}
