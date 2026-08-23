package io.kb.app.ui.listen

import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.isActive
import kotlinx.coroutines.launch

/** PROTOTYPE — fake on-device TTS for the listen-player prototype (#188). */
data class ListenUiState(
    val isPlaying: Boolean = false,
    val isPaused: Boolean = false,
    val positionChars: Int = 0,
    val bodyLength: Int = 0,
    val rate: Float = 1f,
    val voice: String = "Default",
    val backgroundReady: Boolean = true,
)

/** Voices the real engine would expose (AVSpeechSynthesisVoice / TextToSpeech Voice). */
val LISTEN_VOICES = listOf("Default", "Alex", "Samantha")

/** Selectable speech rates, cycled by the player UI. */
val LISTEN_RATES = listOf(0.75f, 1f, 1.25f, 1.5f)

class FakeTtsPlayer(
    private val bodyLength: Int,
    private val scope: CoroutineScope,
    private val onPositionChanged: (Int) -> Unit,
    private val onFinished: () -> Unit,
) {
    private val _state = MutableStateFlow(ListenUiState(bodyLength = bodyLength))
    val state: StateFlow<ListenUiState> = _state.asStateFlow()

    private var tickJob: Job? = null
    private var voiceIndex = 0

    /** Start speaking from a char offset (resume-from-audio-position). */
    fun play(fromPositionChars: Int) {
        val from = fromPositionChars.coerceIn(0, bodyLength)
        _state.update { it.copy(isPlaying = true, isPaused = false, positionChars = from) }
        onPositionChanged(from)
        tickJob = scope.launch {
            while (isActive) {
                delay(50)
                val s = _state.value
                if (!s.isPlaying) break
                // ~120 chars/sec scaled by rate — fast enough to demo, slow enough to follow.
                val step = (6 * s.rate).toInt().coerceAtLeast(1)
                val next = (s.positionChars + step).coerceAtMost(bodyLength)
                _state.update { it.copy(positionChars = next) }
                onPositionChanged(next)
                if (next >= bodyLength) {
                    finish()
                    break
                }
            }
        }
    }

    fun pause() {
        tickJob?.cancel()
        tickJob = null
        _state.update { it.copy(isPlaying = false, isPaused = true) }
    }

    fun resume() {
        if (_state.value.isPaused) play(_state.value.positionChars)
    }

    fun toggle() {
        if (_state.value.isPlaying) pause() else play(_state.value.positionChars)
    }

    fun seekTo(positionChars: Int) {
        val clamped = positionChars.coerceIn(0, bodyLength)
        _state.update { it.copy(positionChars = clamped) }
        onPositionChanged(clamped)
        if (clamped >= bodyLength) finish()
    }

    fun setRate(rate: Float) = _state.update { it.copy(rate = rate) }

    fun cycleRate() {
        val next = (LISTEN_RATES.indexOf(_state.value.rate) + 1) % LISTEN_RATES.size
        _state.update { it.copy(rate = LISTEN_RATES[next]) }
    }

    fun cycleVoice() {
        voiceIndex = (voiceIndex + 1) % LISTEN_VOICES.size
        _state.update { it.copy(voice = LISTEN_VOICES[voiceIndex]) }
    }

    fun stop() {
        tickJob?.cancel()
        tickJob = null
        _state.update { it.copy(isPlaying = false, isPaused = false) }
    }

    private fun finish() {
        tickJob?.cancel()
        tickJob = null
        _state.update { it.copy(isPlaying = false, isPaused = false) }
        onFinished()
    }
}
