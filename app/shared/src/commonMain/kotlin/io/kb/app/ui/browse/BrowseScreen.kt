package io.kb.app.ui.browse

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.Card
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import io.kb.app.data.ConceptRepository
import io.kb.app.data.Domain

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun BrowseScreen(
    onConceptClick: (String) -> Unit,
    repository: ConceptRepository,
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

            else -> DomainList(
                domains = uiState.domains,
                contentPadding = innerPadding,
                onConceptClick = onConceptClick,
            )
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun DomainList(
    domains: List<Domain>,
    contentPadding: androidx.compose.foundation.layout.PaddingValues,
    onConceptClick: (String) -> Unit,
) {
    LazyColumn(
        modifier = Modifier.fillMaxSize(),
        contentPadding = contentPadding,
    ) {
        domains.forEach { domain ->
            item(key = "header-${domain.id}") {
                Text(
                    text = domain.name,
                    style = MaterialTheme.typography.titleMedium,
                    modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp),
                )
            }
            items(
                count = domain.subdomains.size,
                key = { domain.subdomains[it].id },
            ) { index ->
                val subdomain = domain.subdomains[index]
                Card(
                    onClick = { onConceptClick(subdomain.id) },
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(horizontal = 16.dp, vertical = 4.dp),
                ) {
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text(
                            text = subdomain.name,
                            style = MaterialTheme.typography.bodyLarge,
                        )
                        Text(
                            text = "${subdomain.conceptCount} concepts",
                            style = MaterialTheme.typography.bodySmall,
                        )
                    }
                }
            }
        }
    }
}
