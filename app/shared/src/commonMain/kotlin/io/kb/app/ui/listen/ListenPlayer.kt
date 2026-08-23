package io.kb.app.ui.listen

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Slider
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import io.kb.app.data.ProgressModel
import io.kb.app.ui.components.FractionBar
import io.kb.app.ui.components.FractionRing
import io.kb.app.ui.components.percentText

/** PROTOTYPE — the three listen-mode player variants (#188). All drive one shared char-offset position. */

private fun positionText(state: ListenUiState): String =
    "${percentText(state.positionChars, state.bodyLength)} · ${state.positionChars}/${state.bodyLength} chars"

@Composable
private fun PlayPauseButton(
    state: ListenUiState,
    onToggle: () -> Unit,
    size: Int = 56,
) {
    Surface(
        shape = MaterialTheme.shapes.large,
        color = MaterialTheme.colorScheme.primary,
        contentColor = MaterialTheme.colorScheme.onPrimary,
        modifier = Modifier
            .size(size.dp)
            .clickable(onClick = onToggle),
    ) {
        Box(contentAlignment = Alignment.Center) {
            Text(
                text = if (state.isPlaying) "❚❚" else "▶",
                style = MaterialTheme.typography.titleLarge,
            )
        }
    }
}

/** Variant A — Dock: compact player pinned to the bottom; reading text stays visible above. */
@Composable
fun ListenPlayerDock(
    state: ListenUiState,
    title: String,
    onToggle: () -> Unit,
    onSeek: (Int) -> Unit,
    onRate: () -> Unit,
    onVoice: () -> Unit,
    modifier: Modifier = Modifier,
) {
    Surface(
        modifier = modifier.fillMaxWidth(),
        shadowElevation = 8.dp,
    ) {
        Column(modifier = Modifier.padding(horizontal = 16.dp, vertical = 12.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                PlayPauseButton(state = state, onToggle = onToggle, size = 44)
                Spacer(modifier = Modifier.width(12.dp))
                Column(modifier = Modifier.weight(1f)) {
                    Text(
                        text = title,
                        style = MaterialTheme.typography.titleSmall,
                        maxLines = 1,
                    )
                    Slider(
                        value = ProgressModel.fraction(state.positionChars, state.bodyLength),
                        onValueChange = { onSeek(ProgressModel.positionForFraction(it, state.bodyLength)) },
                    )
                    Text(
                        text = positionText(state),
                        style = MaterialTheme.typography.labelSmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                }
                Column(horizontalAlignment = Alignment.CenterHorizontally) {
                    Text(
                        text = "${state.rate}×",
                        style = MaterialTheme.typography.labelMedium,
                        modifier = Modifier.clickable(onClick = onRate),
                    )
                    Text(
                        text = state.voice,
                        style = MaterialTheme.typography.labelSmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                        modifier = Modifier.clickable(onClick = onVoice),
                    )
                }
            }
        }
    }
}

/** Variant B — Immersive: full-screen player; the ring is the hub, controls centered. */
@Composable
fun ListenPlayerImmersive(
    state: ListenUiState,
    title: String,
    onToggle: () -> Unit,
    onSeek: (Int) -> Unit,
    onRate: (Float) -> Unit,
    onVoice: () -> Unit,
    onBackToReading: () -> Unit,
    modifier: Modifier = Modifier,
) {
    Column(
        modifier = modifier
            .fillMaxWidth()
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
    ) {
        Spacer(modifier = Modifier.height(8.dp))
        Text(
            text = title,
            style = MaterialTheme.typography.headlineSmall,
            textAlign = androidx.compose.ui.text.style.TextAlign.Center,
        )
        Spacer(modifier = Modifier.height(24.dp))
        Box(contentAlignment = Alignment.Center) {
            FractionRing(
                fraction = ProgressModel.fraction(state.positionChars, state.bodyLength),
                modifier = Modifier.size(200.dp),
            )
            PlayPauseButton(state = state, onToggle = onToggle, size = 72)
        }
        Spacer(modifier = Modifier.height(12.dp))
        Text(
            text = positionText(state),
            style = MaterialTheme.typography.labelMedium,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
        )
        Slider(
            value = ProgressModel.fraction(state.positionChars, state.bodyLength),
            onValueChange = { onSeek(ProgressModel.positionForFraction(it, state.bodyLength)) },
            modifier = Modifier.fillMaxWidth(),
        )
        Spacer(modifier = Modifier.height(16.dp))
        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
            LISTEN_RATES.forEach { rate ->
                Surface(
                    shape = MaterialTheme.shapes.small,
                    color = if (rate == state.rate) MaterialTheme.colorScheme.primaryContainer
                    else MaterialTheme.colorScheme.surfaceVariant,
                    modifier = Modifier.clickable { onRate(rate) },
                ) {
                    Text(
                        text = "$rate×",
                        style = MaterialTheme.typography.labelMedium,
                        modifier = Modifier.padding(horizontal = 12.dp, vertical = 6.dp),
                    )
                }
            }
        }
        Spacer(modifier = Modifier.height(12.dp))
        Row(verticalAlignment = Alignment.CenterVertically) {
            Text(
                text = "Voice: ${state.voice}",
                style = MaterialTheme.typography.bodyMedium,
                modifier = Modifier.clickable(onClick = onVoice),
            )
            Text(
                text = "  ·  background audio on (iOS)",
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
        }
        Spacer(modifier = Modifier.height(32.dp))
        OutlinedButton(onClick = onBackToReading) { Text("Back to reading") }
    }
}

/** Variant C — Inline: controls sit in the reading flow, minimal chrome. */
@Composable
fun ListenPlayerInline(
    state: ListenUiState,
    onToggle: () -> Unit,
    onSeek: (Int) -> Unit,
    onRate: () -> Unit,
    onVoice: () -> Unit,
    modifier: Modifier = Modifier,
) {
    Column(modifier = modifier.fillMaxWidth().padding(horizontal = 16.dp)) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            PlayPauseButton(state = state, onToggle = onToggle, size = 36)
            Spacer(modifier = Modifier.width(10.dp))
            FractionBar(
                fraction = ProgressModel.fraction(state.positionChars, state.bodyLength),
                modifier = Modifier.weight(1f),
            )
            Spacer(modifier = Modifier.width(10.dp))
            Text(
                text = "${state.rate}×",
                style = MaterialTheme.typography.labelMedium,
                modifier = Modifier.clickable(onClick = onRate),
            )
            Text(
                text = state.voice,
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                modifier = Modifier.clickable(onClick = onVoice),
            )
        }
        Text(
            text = "Listening · ${positionText(state)}",
            style = MaterialTheme.typography.labelSmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.padding(top = 4.dp),
        )
    }
}
