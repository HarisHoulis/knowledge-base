package io.kb.app.data

/** PROTOTYPE — pure status-transition model for the progress-tracking prototype (#130). */
object ProgressModel {

    /** How far the reader is through the body, 0f..1f. */
    fun fraction(position: Int, bodyLength: Int): Float {
        if (bodyLength <= 0) return 0f
        return (position.toFloat() / bodyLength).coerceIn(0f, 1f)
    }

    /** Char offset from a scroll fraction; clamps to body length. */
    fun positionForFraction(fraction: Float, bodyLength: Int): Int {
        if (bodyLength <= 0) return 0
        return (fraction.coerceIn(0f, 1f) * bodyLength).toInt().coerceIn(0, bodyLength)
    }

    fun label(status: ProgressStatus): String = when (status) {
        ProgressStatus.NEW -> "New"
        ProgressStatus.IN_PROGRESS -> "In progress"
        ProgressStatus.CONSUMED -> "Done"
        ProgressStatus.REVISITING -> "Re-reading"
    }

    /** Opening a concept: NEW starts the first pass; a CONSUMED one is re-read. */
    fun onOpen(status: ProgressStatus): ProgressStatus = when (status) {
        ProgressStatus.NEW -> ProgressStatus.IN_PROGRESS
        ProgressStatus.CONSUMED -> ProgressStatus.REVISITING
        else -> status
    }

    /** Scrolling past the end of the body finishes the pass. */
    fun onReachEnd(status: ProgressStatus): ProgressStatus = when (status) {
        ProgressStatus.NEW, ProgressStatus.IN_PROGRESS -> ProgressStatus.CONSUMED
        else -> status
    }

    fun isResumable(status: ProgressStatus): Boolean =
        status == ProgressStatus.IN_PROGRESS || status == ProgressStatus.REVISITING
}
