package io.kb.app.data

import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update

private data class Seed(
    val id: String,
    val title: String,
    val concept: String,
    val domainSlug: String,
    val subdomainSlug: String,
    val body: String,
    val takeaways: List<String>,
    val startStatus: ProgressStatus,
    val startFraction: Float,
) {
    fun summary(progress: Progress) = ConceptSummary(
        id = id,
        title = title,
        domainSlug = domainSlug,
        subdomainSlug = subdomainSlug,
        progress = progress,
    )

    fun detail(progress: Progress) = ConceptDetail(
        id = id,
        title = title,
        concept = concept,
        domainSlug = domainSlug,
        subdomainSlug = subdomainSlug,
        body = body,
        takeaways = takeaways,
        sources = emptyList(),
        progress = progress,
    )
}

/** PROTOTYPE — wipe me. In-memory store powering the progress-tracking prototype (#130). */
class FakeConceptRepository : ConceptRepository {

    private val seed: List<Seed> = listOf(
        Seed(
            id = "c-rag-vector",
            title = "Vector Search Essentials",
            concept = "vector-search-essentials",
            domainSlug = "ai-workflows",
            subdomainSlug = "rag",
            body = body(
                "Vector search turns text into coordinates so meaning can be measured as distance. " +
                    "An embedding model maps every document to a high-dimensional point, and the query is " +
                    "embedded into the same space; the nearest points are the most relevant results. " +
                    "The distance metric matters as much as the model: cosine similarity normalizes length " +
                    "so only direction counts, while Euclidean distance still penalizes magnitude. " +
                    "Approximate nearest neighbour indexes (ANN) trade a little recall for orders of magnitude " +
                    "fewer distance computations, and hybrid search adds a keyword fallback for exact terms " +
                    "embeddings often blur. In practice, ranking quality comes less from the index than from " +
                    "how the corpus is chunked and how the chunks are re-ranked after retrieval."
            ),
            takeaways = listOf("Embeddings map text to points; retrieval is nearest-neighbour search."),
            startStatus = ProgressStatus.IN_PROGRESS,
            startFraction = 0.2f,
        ),
        Seed(
            id = "c-rag-chunking",
            title = "Chunking Strategies for RAG",
            concept = "chunking-strategies-for-rag",
            domainSlug = "ai-workflows",
            subdomainSlug = "rag",
            body = body(
                "Retrieval quality is decided long before the query arrives: at chunking time. A chunk that " +
                    "is too small loses the context its meaning depends on; one that is too large drags in " +
                    "irrelevant passages that drown the signal. Fixed-size chunks are simple and predictable " +
                    "but split sentences and ideas mid-thought. Semantic chunking waits for a meaningful " +
                    "boundary — a paragraph or a topic shift — and produces passages that stand alone. " +
                    "Recursive splitting walks down a hierarchy of separators until every piece fits a budget. " +
                    "Overlap between neighbours keeps a concept that straddles a boundary from disappearing " +
                    "entirely. The right strategy depends on the corpus: dense manuals want small, " +
                    "self-contained units; narrative prose tolerates larger spans. Whatever the choice, " +
                    "the chunking decision should be made with the downstream re-ranker in view, because " +
                    "garbage in means garbage retrieved."
            ),
            takeaways = listOf("Chunk size is a recall trade-off; overlap preserves boundary-spanning ideas."),
            startStatus = ProgressStatus.REVISITING,
            startFraction = 0.65f,
        ),
        Seed(
            id = "c-rag-hybrid",
            title = "Hybrid Search in Practice",
            concept = "hybrid-search-in-practice",
            domainSlug = "ai-workflows",
            subdomainSlug = "rag",
            body = body(
                "Hybrid search fuses a dense and a sparse retrieval path so each covers the other's blind " +
                    "spots. The dense path understands meaning but struggles with exact identifiers, product " +
                    "codes, and rare terms; the sparse path is precise on keywords but blind to synonyms. " +
                    "Fusing the two score lists needs a shared scale: score normalization, reciprocal rank " +
                    "fusion, or a learned ranker. Normalization is the cheapest and works well at small scale; " +
                    "RRF is robust and parameter-light; a learned model adds the most accuracy and the most " +
                    "operational weight. When the top results agree across both paths the answer is almost " +
                    "certainly correct; disagreement is where the re-ranker earns its keep."
            ),
            takeaways = listOf("Dense + sparse cover each other's gaps; fusion is the hard part."),
            startStatus = ProgressStatus.NEW,
            startFraction = 0f,
        ),
        Seed(
            id = "c-llm-attention",
            title = "Attention Is All You Need",
            concept = "attention-is-all-you-need",
            domainSlug = "ai-workflows",
            subdomainSlug = "llm",
            body = body(
                "The Transformer replaced recurrence with attention, letting every position look at every " +
                    "other position in a single layer. Attention weights how much each input token should " +
                    "influence each output token, computed from learned query, key, and value vectors. " +
                    "Multi-head attention runs several of these in parallel so the model can attend to " +
                    "different kinds of relationships — syntax, coreference, position — at once. Because " +
                    "attention is position-agnostic, the model needs positional encodings to know the order " +
                    "of the sequence. The layer stack alternates attention with feed-forward networks, each " +
                    "wrapped in a residual connection and layer norm, which is what makes the deep stack " +
                    "trainable. The original paper trained on 3.5B words and beat the state of the art, and " +
                    "every modern language model descends from this architecture."
            ),
            takeaways = listOf("Attention replaces recurrence; position is injected via encodings."),
            startStatus = ProgressStatus.IN_PROGRESS,
            startFraction = 0.46f,
        ),
        Seed(
            id = "c-llm-bitter",
            title = "The Bitter Lesson",
            concept = "the-bitter-lesson",
            domainSlug = "ai-workflows",
            subdomainSlug = "llm",
            body = body(
                "Sutton's bitter lesson is that general methods that exploit computation have always " +
                    "defeated hand-crafted knowledge. Every hard-won insight in search, computer vision, " +
                    "and speech — carefully engineered features, heuristics, and representations — was " +
                    "eventually overtaken by more compute and simpler learning algorithms. The reason is " +
                    "that researchers are tempted to build in what they know rather than let the machine " +
                    "discover it; but the world is more complex than our models of it, and search over that " +
                    "space rewards scaling. The lesson applies to how we build systems too: prefer architectures " +
                    "that improve by simply getting bigger over ones that improve only by getting cleverer."
            ),
            takeaways = listOf("General compute-driven methods beat human-engineered features over time."),
            startStatus = ProgressStatus.NEW,
            startFraction = 0f,
        ),
        Seed(
            id = "c-llm-rope",
            title = "RoPE Explained",
            concept = "rope-explained",
            domainSlug = "ai-workflows",
            subdomainSlug = "llm",
            body = body(
                "Rotary position embeddings encode position by rotating query and key vectors by an angle " +
                    "proportional to the token index. The rotation is what makes the trick elegant: the dot " +
                    "product of two rotated vectors depends on their relative position, which is exactly the " +
                    "translation-invariance attention wants. RoPE is applied dimension by dimension, with a " +
                    "different frequency per pair so long-range and short-range relations are both representable. " +
                    "Because the rotation is relative, the model generalizes to longer sequences than it was " +
                    "trained on, especially when combined with interpolation. It has become the default " +
                    "positional scheme in modern LLMs because it is cheap, stable, and extrapolates well."
            ),
            takeaways = listOf("RoPE encodes position as a rotation, making attention relative."),
            startStatus = ProgressStatus.CONSUMED,
            startFraction = 1f,
        ),
        Seed(
            id = "c-culture-reading",
            title = "Reading Code Like a Senior Engineer",
            concept = "reading-code-like-a-senior-engineer",
            domainSlug = "engineering-culture",
            subdomainSlug = "practices",
            body = body(
                "Senior engineers read code the way editors read prose: for structure, not for every word. " +
                    "They start at the boundaries — the public API, the entry points, the tests — and form a " +
                    "hypothesis about how the pieces connect before reading any implementation. Reading is " +
                    "guided by questions: where does this data come from, what changes it, who consumes it. " +
                    "Naming is the cheapest documentation, so the first pass is often just a skim of names and " +
                    "types. Only when the shape is clear do they descend into the tricky parts — concurrency, " +
                    "mutation, error handling. The skill is less about speed and more about knowing which " +
                    "ten percent of a codebase carries ninety percent of the complexity."
            ),
            takeaways = listOf("Read boundaries first; form hypotheses; descend only into the tricky parts."),
            startStatus = ProgressStatus.NEW,
            startFraction = 0f,
        ),
        Seed(
            id = "c-culture-boring",
            title = "The Value of Boring Code",
            concept = "the-value-of-boring-code",
            domainSlug = "engineering-culture",
            subdomainSlug = "practices",
            body = body(
                "Boring code is code that could not surprise you. It uses the framework's normal patterns, " +
                    "does the obvious thing at each step, and keeps state changes visible. Excitement in code " +
                    "is usually a warning sign: a clever trick, an unusual abstraction, an unexplained magic " +
                    "constant. The reader's job is to reason about behavior under pressure, and surprising " +
                    "code makes that reasoning fail exactly when it matters most — during an incident. " +
                    "Favoring boring code is not a license to be sloppy; it is the discipline of spending " +
                    "cleverness on the problem rather than the code, and keeping every future reader's " +
                    "attention for the parts that genuinely need it."
            ),
            takeaways = listOf("Boring code is robust to the way we actually read and operate it."),
            startStatus = ProgressStatus.CONSUMED,
            startFraction = 1f,
        ),
    )

    private val domainsSeed = listOf(
        Domain(
            id = "d-ai",
            name = "AI Workflows",
            slug = "ai-workflows",
            subdomains = listOf(
                Subdomain(id = "s-rag", name = "RAG", slug = "rag", conceptCount = 3),
                Subdomain(id = "s-llm", name = "LLM", slug = "llm", conceptCount = 3),
            ),
        ),
        Domain(
            id = "d-culture",
            name = "Engineering Culture",
            slug = "engineering-culture",
            subdomains = listOf(
                Subdomain(id = "s-practices", name = "Practices", slug = "practices", conceptCount = 2),
            ),
        ),
    )

    private val initialProgress = seed.associate { s ->
        s.id to Progress(
            status = s.startStatus,
            position = if (s.startStatus == ProgressStatus.CONSUMED) s.body.length else (s.body.length * s.startFraction).toInt(),
        )
    }

    private val _progress = MutableStateFlow(initialProgress)
    val progress: StateFlow<Map<String, Progress>> = _progress.asStateFlow()

    private fun bodyLength(id: String) = seed.first { it.id == id }.body.length

    override suspend fun domains(): List<Domain> = domainsSeed

    override suspend fun concepts(
        domain: String?,
        subdomain: String?,
        statuses: List<ProgressStatus>,
        page: Int,
        limit: Int,
    ): ConceptListPage {
        val all = seed
            .filter { domain == null || it.domainSlug == domain }
            .filter { subdomain == null || it.subdomainSlug == subdomain }
            .filter { statuses.isEmpty() || statusOf(it.id) in statuses }
            .map { it.summary(progressOf(it.id)) }
        val from = (page - 1) * limit
        return ConceptListPage(
            page = page,
            limit = limit,
            total = all.size,
            items = all.drop(from).take(limit),
        )
    }

    override suspend fun concept(id: String): ConceptDetail =
        seed.first { it.id == id }.detail(progressOf(id))

    override suspend fun search(query: String, page: Int, limit: Int): SearchPage =
        SearchPage(
            q = query,
            page = page,
            limit = limit,
            total = 0,
            items = emptyList(),
        )

    override suspend fun writeProgress(id: String, write: ProgressWrite) {
        val normalized = when (write.status) {
            ProgressStatus.CONSUMED -> Progress(ProgressStatus.CONSUMED, bodyLength(id))
            ProgressStatus.NEW -> Progress(ProgressStatus.NEW, 0)
            else -> Progress(
                status = write.status,
                position = write.position ?: progressOf(id).position,
            )
        }
        _progress.update { it + (id to normalized) }
    }

    /** PROTOTYPE helpers (not on the API seam) */
    fun progressOf(id: String): Progress = _progress.value[id] ?: Progress(ProgressStatus.NEW)

    fun statusOf(id: String): ProgressStatus = progressOf(id).status

    fun groupedSummaries(): List<BrowseGroup> = domainsSeed.flatMap { domain ->
        domain.subdomains.map { sub ->
            val concepts = seed
                .filter { it.domainSlug == domain.slug && it.subdomainSlug == sub.slug }
                .map { it.summary(progressOf(it.id)) }
            BrowseGroup(
                domainName = domain.name,
                subdomainName = sub.name,
                subdomainSlug = sub.slug,
                concepts = concepts,
            )
        }
    }

    fun resumeSummaries(): List<ConceptSummary> = seed
        .filter { statusOf(it.id) in RESUME_STATUSES }
        .map { it.summary(progressOf(it.id)) }

    fun detail(id: String): ConceptDetail = seed.first { it.id == id }.detail(progressOf(id))

    companion object {
        val RESUME_STATUSES = listOf(ProgressStatus.IN_PROGRESS, ProgressStatus.REVISITING)
    }
}

data class BrowseGroup(
    val domainName: String,
    val subdomainName: String,
    val subdomainSlug: String,
    val concepts: List<ConceptSummary>,
)

private fun body(paragraph: String): String = buildString {
    repeat(14) { i ->
        append("${i + 1}. ")
        append(paragraph)
        append("\n\n")
    }
    append(paragraph.trim())
}
