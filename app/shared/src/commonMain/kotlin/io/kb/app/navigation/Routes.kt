package io.kb.app.navigation

import androidx.navigation3.runtime.NavKey
import kotlinx.serialization.Serializable

@Serializable
sealed interface Route : NavKey {
    @Serializable
    data object Browse : Route

    @Serializable
    data object Resume : Route

    @Serializable
    data object Search : Route

    @Serializable
    data class Reader(val conceptId: String) : Route
}
