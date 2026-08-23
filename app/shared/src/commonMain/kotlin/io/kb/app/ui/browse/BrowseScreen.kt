package io.kb.app.ui.browse

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Card
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FilterChip
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import io.kb.app.data.BrowseGroup
import io.kb.app.data.ConceptSummary
import io.kb.app.data.FakeConceptRepository
import io.kb.app.data.ProgressModel
import io.kb.app.data.ProgressStatus
import io.kb.app.ui.components.StatusBadge
import io.kb.app.ui.components.StatusDot
import io.kb.app.ui.components.statusColor
import io.kb.app.ui.prototype.PrototypeVariant

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun BrowseScreen(
    onConceptClick: (String) -> Unit,
    repository: FakeConceptRepository,
    variant: PrototypeVariant,
    viewModel: BrowseViewModel = viewModel { BrowseViewModel(repository) },
) {
    val uiState by viewModel.uiState.collectAsState()

    Scaffold(
        topBar = { TopAppBar(title = { Text("Browse") }) },
    ) { innerPadding ->
        when {
            uiState.isLoading -> CircularProgressIndicator(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(innerPadding),
            )

            uiState.error != null -> Text(
                text = uiState.error.orEmpty(),
                color = MaterialTheme.colorScheme.error,
                modifier = Modifier
                    .fillMaxSize()
                    .padding(innerPadding),
            )

            else -> BrowseContent(
                uiState = uiState,
                variant = variant,
                contentPadding = innerPadding,
                onConceptClick = onConceptClick,
                onFilterChange = viewModel::setStatusFilter,
            )
        }
    }
}

@Composable
private fun BrowseContent(
    uiState: BrowseUiState,
    variant: PrototypeVariant,
    contentPadding: androidx.compose.foundation.layout.PaddingValues,
    onConceptClick: (String) -> Unit,
    onFilterChange: (ProgressStatus?) -> Unit,
) {
    Column(modifier = Modifier.fillMaxSize()) {
        if (variant == PrototypeVariant.MINIMAL) {
            FilterRow(
                selected = uiState.statusFilter,
                onFilterChange = onFilterChange,
                modifier = Modifier.padding(horizontal = 16.dp, vertical = 4.dp),
            )
        }
        LazyColumn(
            modifier = Modifier.fillMaxSize(),
            contentPadding = contentPadding,
        ) {
            uiState.groups.forEach { group ->
                val concepts = filterConcepts(group, uiState.statusFilter)
                if (concepts.isNotEmpty()) {
                    item(key = "header-${group.subdomainSlug}") {
                        Column(
                            modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp),
                        ) {
                            Text(
                                text = group.domainName,
                                style = MaterialTheme.typography.labelSmall,
                                color = MaterialTheme.colorScheme.onSurfaceVariant,
                            )
                            Text(
                                text = group.subdomainName,
                                style = MaterialTheme.typography.titleMedium,
                            )
                        }
                    }
                    items(
                        count = concepts.size,
                        key = { concepts[it].id },
                    ) { index ->
                        val concept = concepts[index]
                        when (variant) {
                            PrototypeVariant.BADGE_FIRST -> BadgeRow(
                                concept = concept,
                                onConceptClick = onConceptClick,
                            )

                            PrototypeVariant.RESUME_FIRST -> DotRow(
                                concept = concept,
                                onConceptClick = onConceptClick,
                            )

                            PrototypeVariant.MINIMAL -> AccentRow(
                                concept = concept,
                                onConceptClick = onConceptClick,
                            )
                        }
                    }
                }
            }
        }
    }
}

private fun filterConcepts(group: BrowseGroup, filter: ProgressStatus?): List<ConceptSummary> =
    if (filter == null) group.concepts else group.concepts.filter { it.progress.status == filter }

@Composable
private fun FilterRow(
    selected: ProgressStatus?,
    onFilterChange: (ProgressStatus?) -> Unit,
    modifier: Modifier = Modifier,
) {
    Row(
        modifier = modifier,
        verticalAlignment = Alignment.CenterVertically,
    ) {
        browseStatusFilters.forEach { status ->
            FilterChip(
                selected = selected == status,
                onClick = { onFilterChange(status) },
                label = { Text(status?.let { ProgressModel.label(it) } ?: "All") },
                modifier = Modifier.padding(end = 8.dp),
            )
        }
    }
}

@Composable
private fun BadgeRow(
    concept: ConceptSummary,
    onConceptClick: (String) -> Unit,
) {
    Card(
        onClick = { onConceptClick(concept.id) },
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp, vertical = 4.dp),
    ) {
        Column(modifier = Modifier.padding(horizontal = 16.dp, vertical = 12.dp)) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically,
            ) {
                Text(
                    text = concept.title,
                    style = MaterialTheme.typography.bodyLarge,
                    modifier = Modifier.weight(1f),
                )
                StatusBadge(concept.progress.status)
            }
        }
    }
}

@Composable
private fun DotRow(
    concept: ConceptSummary,
    onConceptClick: (String) -> Unit,
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clickable { onConceptClick(concept.id) }
            .padding(horizontal = 16.dp, vertical = 12.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        StatusDot(
            status = concept.progress.status,
            modifier = Modifier.padding(end = 12.dp),
        )
        Column(modifier = Modifier.weight(1f)) {
            Text(
                text = concept.title,
                style = MaterialTheme.typography.bodyLarge,
            )
        }
    }
}

@Composable
private fun AccentRow(
    concept: ConceptSummary,
    onConceptClick: (String) -> Unit,
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clickable { onConceptClick(concept.id) }
            .padding(horizontal = 16.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Box(
            modifier = Modifier
                .width(4.dp)
                .height(36.dp)
                .background(statusColor(concept.progress.status), RoundedCornerShape(2.dp)),
        )
        Column(
            modifier = Modifier
                .weight(1f)
                .padding(start = 12.dp, top = 10.dp, bottom = 10.dp),
        ) {
            Text(
                text = concept.title,
                style = MaterialTheme.typography.bodyLarge,
            )
            Text(
                text = ProgressModel.label(concept.progress.status),
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
        }
    }
}
