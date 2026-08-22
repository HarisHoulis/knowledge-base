plugins {
    alias(libs.plugins.kb.android.app)
}

android {
    namespace = "io.kb.app"

    defaultConfig {
        applicationId = "io.kb.app"
        versionCode = 1
        versionName = "0.1.0"
    }
}

dependencies {
    implementation(projects.shared)
    implementation(libs.androidx.activity.compose)
}
