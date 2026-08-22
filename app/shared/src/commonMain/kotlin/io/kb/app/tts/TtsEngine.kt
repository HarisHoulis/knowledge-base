package io.kb.app.tts

expect class TtsEngine() {
    fun speak(text: String)
    fun stop()
}
