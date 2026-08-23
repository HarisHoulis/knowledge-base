package io.kb.app.ui.prototype

import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

/** PROTOTYPE — three structurally different ways to surface progress (#130). */
enum class PrototypeVariant(val key: String, val title: String, val blurb: String) {
    BADGE_FIRST("A", "Badge-first", "explicit badges + manual transitions"),
    RESUME_FIRST("B", "Resume-first", "resume as the hub + auto transitions"),
    MINIMAL("C", "Minimal", "color accents + filter chips, no badges"),
}

private val variants = PrototypeVariant.entries

@Composable
fun VariantSwitcher(
    current: PrototypeVariant,
    onChange: (PrototypeVariant) -> Unit,
    modifier: Modifier = Modifier,
) {
    val interactionSource = remember { MutableInteractionSource() }
    Surface(
        modifier = modifier
            .padding(horizontal = 12.dp, vertical = 8.dp),
        shape = RoundedCornerShape(24.dp),
        color = MaterialTheme.colorScheme.inverseSurface,
        contentColor = MaterialTheme.colorScheme.inverseOnSurface,
        shadowElevation = 8.dp,
    ) {
        Row(
            modifier = Modifier.padding(horizontal = 16.dp, vertical = 10.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Text(
                text = "‹",
                style = MaterialTheme.typography.titleLarge,
                modifier = Modifier.clickable(
                    interactionSource = interactionSource,
                    indication = null,
                ) { onChange(variants[(variants.indexOf(current) - 1 + variants.size) % variants.size]) },
            )
            Text(
                text = "${current.key} — ${current.title}",
                style = MaterialTheme.typography.titleMedium,
                modifier = Modifier.weight(1f),
            )
            Text(
                text = current.blurb,
                style = MaterialTheme.typography.bodySmall,
                modifier = Modifier.weight(2f),
            )
            Text(
                text = "›",
                style = MaterialTheme.typography.titleLarge,
                modifier = Modifier.clickable(
                    interactionSource = interactionSource,
                    indication = null,
                ) { onChange(variants[(variants.indexOf(current) + 1) % variants.size]) },
            )
        }
    }
}
