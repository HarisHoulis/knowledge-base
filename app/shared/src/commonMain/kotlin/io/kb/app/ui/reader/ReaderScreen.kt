package io.kb.app.ui.reader

import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import io.kb.app.tts.TtsEngine

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ReaderScreen(conceptId: String, ttsEngine: TtsEngine) {
    Scaffold(
        topBar = { TopAppBar(title = { Text("Concept") }) },
    ) { innerPadding ->
        Text(
            text = "Reader screen for concept $conceptId. TTS engine ready: ${ttsEngine::class.simpleName}.",
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding),
        )
    }
}
