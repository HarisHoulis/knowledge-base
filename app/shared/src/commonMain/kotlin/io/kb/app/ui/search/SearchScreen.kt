package io.kb.app.ui.search

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
fun SearchScreen(onConceptClick: (String) -> Unit) {
    Scaffold(
        topBar = { TopAppBar(title = { Text("Search") }) },
    ) { innerPadding ->
        Text(
            text = "Search screen — full-text search over the concept store.",
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding),
        )
    }
}
