package io.kb.app.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import io.kb.app.data.ProgressModel
import io.kb.app.data.ProgressStatus

/** PROTOTYPE — shared progress surfacing pieces for the progress-tracking prototype (#130). */

@Composable
fun statusColor(status: ProgressStatus): Color = when (status) {
    ProgressStatus.NEW -> MaterialTheme.colorScheme.outline
    ProgressStatus.IN_PROGRESS -> MaterialTheme.colorScheme.primary
    ProgressStatus.CONSUMED -> MaterialTheme.colorScheme.tertiary
    ProgressStatus.REVISITING -> MaterialTheme.colorScheme.secondary
}

@Composable
fun StatusBadge(status: ProgressStatus) {
    val color = statusColor(status)
    Surface(
        color = color.copy(alpha = 0.14f),
        shape = RoundedCornerShape(8.dp),
    ) {
        Text(
            text = ProgressModel.label(status),
            color = color,
            style = MaterialTheme.typography.labelSmall,
            modifier = Modifier.padding(horizontal = 8.dp, vertical = 3.dp),
        )
    }
}

@Composable
fun StatusDot(status: ProgressStatus, modifier: Modifier = Modifier) {
    Box(
        modifier = modifier
            .size(10.dp)
            .background(statusColor(status), CircleShape),
    )
}

@Composable
fun FractionBar(fraction: Float) {
    LinearProgressIndicator(
        progress = { fraction.coerceIn(0f, 1f) },
    )
}

@Composable
fun FractionRing(
    fraction: Float,
    modifier: Modifier = Modifier,
    trackColor: Color = MaterialTheme.colorScheme.surfaceVariant,
) {
    CircularProgressIndicator(
        progress = { fraction.coerceIn(0f, 1f) },
        modifier = modifier,
        trackColor = trackColor,
    )
}

fun percentText(position: Int, bodyLength: Int): String =
    "${(ProgressModel.fraction(position, bodyLength) * 100).toInt()}%"
