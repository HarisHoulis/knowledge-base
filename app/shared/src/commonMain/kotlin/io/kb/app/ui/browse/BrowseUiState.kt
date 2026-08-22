package io.kb.app.ui.browse

import io.kb.app.data.Domain

data class BrowseUiState(
    val domains: List<Domain> = emptyList(),
    val isLoading: Boolean = true,
    val error: String? = null,
)
