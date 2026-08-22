package io.kb.app.data

import io.ktor.client.HttpClient

expect fun createHttpClient(): HttpClient
