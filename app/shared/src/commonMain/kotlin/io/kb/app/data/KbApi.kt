package io.kb.app.data

import io.kb.app.ServerConfig
import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.request.get
import io.ktor.client.request.parameter
import io.ktor.client.request.put
import io.ktor.client.request.setBody
import io.ktor.http.ContentType
import io.ktor.http.contentType

class KbApi(
    private val baseUrl: String = ServerConfig.baseUrl,
    private val client: HttpClient = createHttpClient(),
) {
    suspend fun domains(): List<Domain> =
        client.get("$baseUrl/api/v1/domains").body()

    suspend fun concepts(
        domain: String? = null,
        subdomain: String? = null,
        statuses: List<ProgressStatus> = emptyList(),
        page: Int = 1,
        limit: Int = 20,
    ): ConceptListPage = client.get("$baseUrl/api/v1/concepts") {
        domain?.let { parameter("domain", it) }
        subdomain?.let { parameter("subdomain", it) }
        statuses.forEach { parameter("status", it.name) }
        parameter("page", page)
        parameter("limit", limit)
    }.body()

    suspend fun concept(id: String): ConceptDetail =
        client.get("$baseUrl/api/v1/concepts/$id").body()

    suspend fun search(query: String, page: Int = 1, limit: Int = 20): SearchPage =
        client.get("$baseUrl/api/v1/concepts/search") {
            parameter("q", query)
            parameter("page", page)
            parameter("limit", limit)
        }.body()

    suspend fun writeProgress(id: String, write: ProgressWrite) {
        client.put("$baseUrl/api/v1/concepts/$id/progress") {
            contentType(ContentType.Application.Json)
            setBody(write)
        }
    }
}
