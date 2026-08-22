package io.kb.app.data

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
enum class ProgressStatus {
    @SerialName("NEW") NEW,
    @SerialName("IN_PROGRESS") IN_PROGRESS,
    @SerialName("CONSUMED") CONSUMED,
    @SerialName("REVISITING") REVISITING,
}

@Serializable
data class Progress(val status: ProgressStatus, val position: Int = 0)

@Serializable
data class Domain(
    val id: String,
    val name: String,
    val slug: String,
    val subdomains: List<Subdomain> = emptyList(),
)

@Serializable
data class Subdomain(
    val id: String,
    val name: String,
    val slug: String,
    val conceptCount: Int = 0,
)

@Serializable
data class ConceptListPage(
    val page: Int,
    val limit: Int,
    val total: Int,
    val items: List<ConceptSummary>,
)

@Serializable
data class ConceptSummary(
    val id: String,
    val title: String,
    val domainSlug: String,
    val subdomainSlug: String,
    val progress: Progress,
)

@Serializable
data class ConceptDetail(
    val id: String,
    val title: String,
    val concept: String,
    val domainSlug: String,
    val subdomainSlug: String,
    val body: String,
    val takeaways: List<String> = emptyList(),
    val sources: List<Source> = emptyList(),
    val progress: Progress,
)

@Serializable
data class Source(
    val url: String,
    val title: String,
    val author: String = "",
    val date: String = "",
    val position: Int = 0,
)

@Serializable
data class SearchPage(
    val q: String,
    val page: Int,
    val limit: Int,
    val total: Int,
    val items: List<SearchHit>,
)

@Serializable
data class SearchHit(
    val id: String,
    val title: String,
    val snippet: String,
    val rank: Double,
    val progress: Progress,
)

@Serializable
data class ProgressWrite(
    val status: ProgressStatus,
    val position: Int? = null,
)
