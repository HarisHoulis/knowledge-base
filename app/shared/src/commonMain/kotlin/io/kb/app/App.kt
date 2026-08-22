package io.kb.app

import androidx.compose.runtime.Composable
import androidx.lifecycle.viewmodel.navigation3.rememberViewModelStoreNavEntryDecorator
import androidx.navigation3.runtime.NavKey
import androidx.navigation3.runtime.entryProvider
import androidx.navigation3.runtime.rememberNavBackStack
import androidx.navigation3.runtime.rememberSaveableStateHolderNavEntryDecorator
import androidx.navigation3.ui.NavDisplay
import androidx.savedstate.serialization.SavedStateConfiguration
import io.kb.app.data.ConceptRepository
import io.kb.app.data.FakeConceptRepository
import io.kb.app.navigation.Route
import io.kb.app.ui.browse.BrowseScreen
import io.kb.app.ui.reader.ReaderScreen
import io.kb.app.ui.resume.ResumeScreen
import io.kb.app.ui.search.SearchScreen
import io.kb.app.tts.TtsEngine
import kotlinx.serialization.modules.SerializersModule
import kotlinx.serialization.modules.polymorphic
import kotlinx.serialization.modules.subclassesOfSealed

private val navConfiguration = SavedStateConfiguration {
    serializersModule = SerializersModule {
        polymorphic(NavKey::class) {
            subclassesOfSealed<Route>()
        }
    }
}

@Composable
fun App(repository: ConceptRepository = FakeConceptRepository()) {
    val ttsEngine = TtsEngine()
    val backStack = rememberNavBackStack(navConfiguration, Route.Browse)

    NavDisplay(
        backStack = backStack,
        onBack = { backStack.removeLastOrNull() },
        entryDecorators = listOf(
            rememberSaveableStateHolderNavEntryDecorator(),
            rememberViewModelStoreNavEntryDecorator(),
        ),
        entryProvider = entryProvider {
            entry<Route.Browse> {
                BrowseScreen(
                    repository = repository,
                    onConceptClick = { conceptId ->
                        backStack.add(Route.Reader(conceptId))
                    },
                )
            }
            entry<Route.Resume> {
                ResumeScreen(onConceptClick = { backStack.add(Route.Reader(it)) })
            }
            entry<Route.Search> {
                SearchScreen(onConceptClick = { backStack.add(Route.Reader(it)) })
            }
            entry<Route.Reader> { route ->
                ReaderScreen(conceptId = route.conceptId, ttsEngine = ttsEngine)
            }
        },
    )
}
