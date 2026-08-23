package io.kb.app

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
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
import io.kb.app.ui.listen.ListenVariant
import io.kb.app.ui.listen.ListenVariantSwitcher
import io.kb.app.ui.prototype.PrototypeVariant
import io.kb.app.ui.prototype.VariantSwitcher
import io.kb.app.ui.reader.ReaderScreen
import io.kb.app.ui.resume.ResumeScreen
import io.kb.app.ui.search.SearchScreen
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
    val fakeRepository = repository as FakeConceptRepository // PROTOTYPE: screens observe the live in-memory store
    var variant by remember { mutableStateOf(PrototypeVariant.BADGE_FIRST) }
    var listenVariant by remember { mutableStateOf(ListenVariant.DOCK) }
    val backStack = rememberNavBackStack(navConfiguration, Route.Browse)

    Box(modifier = Modifier.fillMaxSize()) {
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
                        repository = fakeRepository,
                        variant = variant,
                        onConceptClick = { conceptId ->
                            backStack.add(Route.Reader(conceptId))
                        },
                    )
                }
                entry<Route.Resume> {
                    ResumeScreen(
                        repository = fakeRepository,
                        variant = variant,
                        onConceptClick = { backStack.add(Route.Reader(it)) },
                    )
                }
                entry<Route.Search> {
                    SearchScreen(onConceptClick = { backStack.add(Route.Reader(it)) })
                }
                entry<Route.Reader> { route ->
                    ReaderScreen(
                        conceptId = route.conceptId,
                        repository = fakeRepository,
                        variant = variant,
                        listenVariant = listenVariant,
                        onBack = { backStack.removeLastOrNull() },
                    )
                }
            },
        )
        if (backStack.lastOrNull() is Route.Reader) {
            ListenVariantSwitcher(
                current = listenVariant,
                onChange = { listenVariant = it },
                modifier = Modifier.align(Alignment.BottomCenter),
            )
        } else {
            VariantSwitcher(
                current = variant,
                onChange = { variant = it },
                modifier = Modifier.align(Alignment.BottomCenter),
            )
        }
    }
}
