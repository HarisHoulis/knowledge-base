plugins {
    `kotlin-dsl`
}

dependencies {
    implementation(libs.android.application.plugin)
    implementation(libs.android.multiplatform.library.plugin)
    implementation(libs.compose.compiler.plugin)
    implementation(libs.compose.multiplatform.plugin)
    implementation(libs.kotlin.multiplatform.plugin)
    implementation(libs.kotlin.serialization.plugin)
}
