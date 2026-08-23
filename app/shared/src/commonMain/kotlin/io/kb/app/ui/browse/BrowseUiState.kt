package io.kb.app.ui.browse

import io.kb.app.data.BrowseGroup
import io.kb.app.data.Progress
import io.kb.app.data.ProgressStatus

data class BrowseUiState(
    val groups: List<BrowseGroup> = emptyList(),
    val isLoading: Boolean = true,
    val error: String? = null,
    val statusFilter: ProgressStatus? = null,
    val progress: Map<String, Progress> = emptyMap(),
)

val browseStatusFilters: List<ProgressStatus?> = listOf(
    null,
    ProgressStatus.IN_PROGRESS,
    ProgressStatus.REVISITING,
    ProgressStatus.CONSUMED,
)
