package io.kb.app.data

class FakeConceptRepository : ConceptRepository {
    override suspend fun domains(): List<Domain> = listOf(
        Domain(
            id = "d1",
            name = "AI Workflows",
            slug = "ai-workflows",
            subdomains = listOf(
                Subdomain(id = "s1", name = "RAG", slug = "rag", conceptCount = 12),
                Subdomain(id = "s2", name = "LLM", slug = "llm", conceptCount = 8),
            ),
        ),
    )

    override suspend fun concepts(
        domain: String?,
        subdomain: String?,
        statuses: List<ProgressStatus>,
        page: Int,
        limit: Int,
    ): ConceptListPage = ConceptListPage(
        page = page,
        limit = limit,
        total = 1,
        items = listOf(
            ConceptSummary(
                id = "c1",
                title = "Attention Is All You Need",
                domainSlug = "ai-workflows",
                subdomainSlug = "llm",
                progress = Progress(ProgressStatus.IN_PROGRESS, 1840),
            ),
        ),
    )

    override suspend fun concept(id: String): ConceptDetail = ConceptDetail(
        id = id,
        title = "Attention Is All You Need",
        concept = "attention-is-all-you-need",
        domainSlug = "ai-workflows",
        subdomainSlug = "llm",
        body = "The Transformer is a sequence model based on self-attention.",
        takeaways = listOf("Self-attention replaces recurrence."),
        sources = emptyList(),
        progress = Progress(ProgressStatus.IN_PROGRESS, 1840),
    )

    override suspend fun search(query: String, page: Int, limit: Int): SearchPage =
        SearchPage(
            q = query,
            page = page,
            limit = limit,
            total = 0,
            items = emptyList(),
        )

    override suspend fun writeProgress(id: String, write: ProgressWrite) = Unit
}
