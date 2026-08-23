package io.kb.app.ui.resume

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
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
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import io.kb.app.data.FakeConceptRepository
import io.kb.app.data.ProgressModel
import io.kb.app.ui.components.FractionBar
import io.kb.app.ui.components.FractionRing
import io.kb.app.ui.components.StatusBadge
import io.kb.app.ui.components.percentText
import io.kb.app.ui.components.statusColor
import io.kb.app.ui.prototype.PrototypeVariant

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ResumeScreen(
    onConceptClick: (String) -> Unit,
    repository: FakeConceptRepository,
    variant: PrototypeVariant,
    viewModel: ResumeViewModel = viewModel { ResumeViewModel(repository) },
) {
    val uiState by viewModel.uiState.collectAsState()

    Scaffold(
        topBar = { TopAppBar(title = { Text("Resume") }) },
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

            uiState.items.isEmpty() -> Text(
                text = "Nothing in progress yet — open a concept to start reading.",
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                modifier = Modifier
                    .fillMaxSize()
                    .padding(innerPadding),
            )

            else -> LazyColumn(
                modifier = Modifier.fillMaxSize(),
                contentPadding = innerPadding,
            ) {
                items(
                    count = uiState.items.size,
                    key = { uiState.items[it].id },
                ) { index ->
                    val item = uiState.items[index]
                    when (variant) {
                        PrototypeVariant.BADGE_FIRST -> BadgeCard(item, onConceptClick)
                        PrototypeVariant.RESUME_FIRST -> ResumeCard(item, onConceptClick)
                        PrototypeVariant.MINIMAL -> MinimalRow(item, onConceptClick)
                    }
                }
            }
        }
    }
}

@Composable
private fun BadgeCard(item: ResumeItem, onConceptClick: (String) -> Unit) {
    Card(
        onClick = { onConceptClick(item.id) },
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp, vertical = 4.dp),
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(
                    text = item.title,
                    style = MaterialTheme.typography.bodyLarge,
                    modifier = Modifier.weight(1f),
                )
                StatusBadge(item.status)
            }
            Text(
                text = "${item.subdomainName} · ${percentText(item.position, item.bodyLength)}",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                modifier = Modifier.padding(top = 4.dp),
            )
            FractionBar(
                fraction = ProgressModel.fraction(item.position, item.bodyLength),
            )
        }
    }
}

@Composable
private fun ResumeCard(item: ResumeItem, onConceptClick: (String) -> Unit) {
    Card(
        onClick = { onConceptClick(item.id) },
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp, vertical = 6.dp),
    ) {
        Row(
            modifier = Modifier.padding(16.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            FractionRing(
                fraction = ProgressModel.fraction(item.position, item.bodyLength),
                modifier = Modifier.size(56.dp),
            )
            Column(
                modifier = Modifier
                    .weight(1f)
                    .padding(start = 16.dp),
            ) {
                Text(
                    text = item.title,
                    style = MaterialTheme.typography.titleMedium,
                )
                Text(
                    text = "Continue at ${percentText(item.position, item.bodyLength)}",
                    style = MaterialTheme.typography.bodySmall,
                    color = statusColor(item.status),
                )
            }
        }
    }
}

@Composable
private fun MinimalRow(item: ResumeItem, onConceptClick: (String) -> Unit) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clickable { onConceptClick(item.id) }
            .padding(horizontal = 16.dp, vertical = 14.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Column(modifier = Modifier.weight(1f)) {
            Text(
                text = item.title,
                style = MaterialTheme.typography.bodyLarge,
            )
            Text(
                text = "Continue · ${percentText(item.position, item.bodyLength)}",
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
        }
        Text(
            text = "›",
            style = MaterialTheme.typography.titleLarge,
            color = statusColor(item.status),
        )
    }
}
