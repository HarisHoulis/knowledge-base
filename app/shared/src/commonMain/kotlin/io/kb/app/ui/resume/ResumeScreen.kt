package io.kb.app.ui.resume

import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ResumeScreen(onConceptClick: (String) -> Unit) {
    Scaffold(
        topBar = { TopAppBar(title = { Text("Resume") }) },
    ) { innerPadding ->
        Text(
            text = "Resume screen — concepts with status IN_PROGRESS or REVISITING.",
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding),
        )
    }
}
