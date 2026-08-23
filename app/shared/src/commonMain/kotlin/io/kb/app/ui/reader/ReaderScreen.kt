package io.kb.app.ui.reader

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.remember
import androidx.compose.runtime.snapshotFlow
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import io.kb.app.data.FakeConceptRepository
import io.kb.app.data.ProgressModel
import io.kb.app.data.ProgressStatus
import io.kb.app.ui.components.FractionBar
import io.kb.app.ui.components.FractionRing
import io.kb.app.ui.components.StatusBadge
import io.kb.app.ui.components.percentText
import io.kb.app.ui.components.statusColor
import io.kb.app.ui.prototype.PrototypeVariant
import kotlinx.coroutines.flow.debounce
import kotlin.math.roundToInt

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ReaderScreen(
    conceptId: String,
    repository: FakeConceptRepository,
    variant: PrototypeVariant,
    viewModel: ReaderViewModel = viewModel { ReaderViewModel(repository, conceptId) },
) {
    val uiState by viewModel.uiState.collectAsState()

    LaunchedEffect(conceptId) { viewModel.onOpen() }

    Scaffold(
        topBar = { TopAppBar(title = { Text("Reader") }) },
        bottomBar = {
            if (!uiState.isLoading) {
                when (variant) {
                    PrototypeVariant.BADGE_FIRST -> ReaderActionsBadgeFirst(viewModel, uiState)
                    PrototypeVariant.RESUME_FIRST -> ReaderActionsResumeFirst(uiState)
                    PrototypeVariant.MINIMAL -> ReaderActionsMinimal(uiState)
                }
            }
        },
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

            else -> ReaderBody(
                uiState = uiState,
                variant = variant,
                contentPadding = innerPadding,
                onPositionChanged = viewModel::updatePosition,
                onScrolledToEnd = viewModel::onScrolledToEnd,
            )
        }
    }
}

@Composable
private fun ReaderBody(
    uiState: ReaderUiState,
    variant: PrototypeVariant,
    contentPadding: androidx.compose.foundation.layout.PaddingValues,
    onPositionChanged: (Int) -> Unit,
    onScrolledToEnd: () -> Unit,
) {
    val scrollState = rememberScrollState()

    // Restore resume position once per concept open (not on every position write).
    val restoreFraction = remember(uiState.conceptId) {
        ProgressModel.fraction(uiState.progress.position, uiState.bodyLength)
    }
    LaunchedEffect(scrollState.maxValue, restoreFraction) {
        if (scrollState.maxValue > 0 && restoreFraction > 0f) {
            scrollState.scrollTo((scrollState.maxValue * restoreFraction).roundToInt())
        }
    }

    // Report scroll → char offset (debounced), and detect reaching the end.
    LaunchedEffect(scrollState, uiState.conceptId) {
        snapshotFlow { scrollState.value to scrollState.maxValue }
            .debounce(150)
            .collect { (offset, max) ->
                if (max > 0) {
                    val f = offset.toFloat() / max
                    onPositionChanged(ProgressModel.positionForFraction(f, uiState.bodyLength))
                    if (f >= 0.995f) onScrolledToEnd()
                }
            }
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(contentPadding)
            .verticalScroll(scrollState),
    ) {
        when (variant) {
            PrototypeVariant.BADGE_FIRST -> HeaderBadgeFirst(uiState)
            PrototypeVariant.RESUME_FIRST -> HeaderResumeFirst(uiState)
            PrototypeVariant.MINIMAL -> HeaderMinimal(uiState)
        }
        Text(
            text = uiState.body,
            style = MaterialTheme.typography.bodyLarge,
            modifier = Modifier.padding(16.dp),
        )
        Text(
            text = "Takeaways",
            style = MaterialTheme.typography.titleSmall,
            modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp),
        )
        uiState.takeaways.forEach { takeaway ->
            Text(
                text = "• $takeaway",
                style = MaterialTheme.typography.bodyMedium,
                modifier = Modifier.padding(horizontal = 16.dp, vertical = 2.dp),
            )
        }
        Spacer(modifier = Modifier.height(32.dp))
    }
}

@Composable
private fun HeaderBadgeFirst(uiState: ReaderUiState) {
    Column(modifier = Modifier.padding(16.dp)) {
        Text(
            text = uiState.title,
            style = MaterialTheme.typography.titleLarge,
        )
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(top = 8.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            StatusBadge(uiState.progress.status)
            Text(
                text = " ${percentText(uiState.progress.position, uiState.bodyLength)} · ${uiState.progress.position}/${uiState.bodyLength} chars",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
        }
        Spacer(modifier = Modifier.height(12.dp))
        FractionBar(ProgressModel.fraction(uiState.progress.position, uiState.bodyLength))
    }
}

@Composable
private fun HeaderResumeFirst(uiState: ReaderUiState) {
    Column(modifier = Modifier.padding(16.dp)) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            Text(
                text = uiState.title,
                style = MaterialTheme.typography.titleLarge,
                modifier = Modifier.weight(1f),
            )
            FractionRing(
                fraction = ProgressModel.fraction(uiState.progress.position, uiState.bodyLength),
                modifier = Modifier.height(40.dp).width(40.dp),
            )
        }
        Text(
            text = ProgressModel.label(uiState.progress.status),
            style = MaterialTheme.typography.labelMedium,
            color = statusColor(uiState.progress.status),
            modifier = Modifier.padding(top = 4.dp),
        )
    }
}

@Composable
private fun HeaderMinimal(uiState: ReaderUiState) {
    val color = statusColor(uiState.progress.status)
    Column(modifier = Modifier.padding(16.dp)) {
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(3.dp)
                .background(color),
        )
        Text(
            text = uiState.title,
            style = MaterialTheme.typography.titleLarge,
            modifier = Modifier.padding(top = 12.dp),
        )
        Text(
            text = "${percentText(uiState.progress.position, uiState.bodyLength)} read",
            style = MaterialTheme.typography.labelMedium,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.padding(top = 2.dp),
        )
    }
}

@Composable
private fun ReaderActionsBadgeFirst(viewModel: ReaderViewModel, uiState: ReaderUiState) {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp),
    ) {
        when (uiState.progress.status) {
            ProgressStatus.CONSUMED -> OutlinedButton(
                onClick = viewModel::markRevisiting,
                modifier = Modifier.fillMaxWidth(),
            ) { Text("Re-read") }

            else -> Button(
                onClick = viewModel::markDone,
                modifier = Modifier.fillMaxWidth(),
            ) { Text("Mark as done") }
        }
    }
}

@Composable
private fun ReaderActionsResumeFirst(uiState: ReaderUiState) {
    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp),
    ) {
        Text(
            text = "Auto-saves as you scroll · reaches the end → Done",
            style = MaterialTheme.typography.labelSmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
        )
    }
}

@Composable
private fun ReaderActionsMinimal(uiState: ReaderUiState) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp, vertical = 8.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Text(
            text = "${ProgressModel.label(uiState.progress.status)} · scroll to resume",
            style = MaterialTheme.typography.labelSmall,
            color = statusColor(uiState.progress.status),
            modifier = Modifier.weight(1f),
        )
    }
}
