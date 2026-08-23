package io.kb.app.ui.reader

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import io.kb.app.data.FakeConceptRepository
import io.kb.app.data.Progress
import io.kb.app.data.ProgressModel
import io.kb.app.data.ProgressStatus
import io.kb.app.data.ProgressWrite
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class ReaderUiState(
    val conceptId: String = "",
    val title: String = "",
    val body: String = "",
    val takeaways: List<String> = emptyList(),
    val bodyLength: Int = 0,
    val progress: Progress = Progress(ProgressStatus.NEW),
    val isLoading: Boolean = true,
    val error: String? = null,
)

class ReaderViewModel(
    private val repository: FakeConceptRepository,
    private val conceptId: String,
) : ViewModel() {

    private val _uiState = MutableStateFlow(ReaderUiState(conceptId = conceptId))
    val uiState: StateFlow<ReaderUiState> = _uiState.asStateFlow()

    init {
        load()
        viewModelScope.launch {
            repository.progress.collect { progress ->
                _uiState.update {
                    it.copy(
                        progress = progress[conceptId] ?: it.progress,
                    )
                }
            }
        }
    }

    fun load() {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true, error = null) }
            val detail = repository.detail(conceptId)
            _uiState.update {
                it.copy(
                    title = detail.title,
                    body = detail.body,
                    takeaways = detail.takeaways,
                    bodyLength = detail.body.length,
                    progress = detail.progress,
                    isLoading = false,
                )
            }
        }
    }

    /** The status a fresh open should transition to (NEW → IN_PROGRESS, CONSUMED → REVISITING). */
    fun onOpen() {
        _uiState.value.let { state ->
            val next = ProgressModel.onOpen(state.progress.status)
            if (next != state.progress.status) write(ProgressWrite(next, state.progress.position))
        }
    }

    /** Scroll position → char offset, saved as IN_PROGRESS (or REVISITING if re-reading). */
    fun updatePosition(position: Int) {
        val state = _uiState.value
        if (state.bodyLength == 0) return
        val clamped = position.coerceIn(0, state.bodyLength)
        val status = if (state.progress.status == ProgressStatus.CONSUMED) ProgressStatus.REVISITING else state.progress.status
        write(ProgressWrite(status, clamped))
    }

    /** Explicit finish: server normalizes position = bodyLength. */
    fun markDone() {
        write(ProgressWrite(ProgressStatus.CONSUMED, null))
    }

    /** Explicitly set back to re-reading from the current position. */
    fun markRevisiting() {
        write(ProgressWrite(ProgressStatus.REVISITING, _uiState.value.progress.position))
    }

    /** Scrolling past the end auto-finishes the pass (Resume-first variant). */
    fun onScrolledToEnd() {
        val state = _uiState.value
        val next = ProgressModel.onReachEnd(state.progress.status)
        if (next != state.progress.status) write(ProgressWrite(next, null))
    }

    private fun write(write: ProgressWrite) {
        viewModelScope.launch { repository.writeProgress(conceptId, write) }
    }
}
