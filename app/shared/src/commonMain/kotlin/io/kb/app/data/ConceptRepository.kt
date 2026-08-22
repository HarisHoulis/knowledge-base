package io.kb.app.data

interface ConceptRepository {
    suspend fun domains(): List<Domain>

    suspend fun concepts(
        domain: String? = null,
        subdomain: String? = null,
        statuses: List<ProgressStatus> = emptyList(),
        page: Int = 1,
        limit: Int = 20,
    ): ConceptListPage

    suspend fun concept(id: String): ConceptDetail

    suspend fun search(query: String, page: Int = 1, limit: Int = 20): SearchPage

    suspend fun writeProgress(id: String, write: ProgressWrite)
}
