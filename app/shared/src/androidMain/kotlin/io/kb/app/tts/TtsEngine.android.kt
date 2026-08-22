package io.kb.app.tts

import android.util.Log

actual class TtsEngine actual constructor() {
    actual fun speak(text: String) {
        Log.d("TtsEngine", "speak: $text")
    }

    actual fun stop() {
        Log.d("TtsEngine", "stop")
    }
}
