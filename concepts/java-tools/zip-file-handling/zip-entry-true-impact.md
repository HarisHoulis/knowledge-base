---
domain: java-tools
subdomain: zip-file-handling
concept: zip-entry-true-impact
title: Calculating the true impact of zip file entries
sources:
  - title: "Calculating the true impact of zip file entries"
    url: "https://jakewharton.com/calculating-zip-file-entry-true-impact/"
---

# Calculating the true impact of zip file entries

The article addresses the challenge of determining each entry's real contribution to a zip file's size. Built-in Java APIs like `FileSystem`, `ZipInputStream`, and `ZipFile` expose only the compressed data size via `ZipEntry.getCompressedSize()`, which excludes per-entry metadata. For `FileSystem`, the situation is worse because only `Files.size(Path)` is available, which returns uncompressed size. Thus, simple summing of compressed sizes does not match the actual zip file size. ([source](https://jakewharton.com/calculating-zip-file-entry-true-impact/))

- `ZipEntry.getCompressedSize()` undercounts an entry's impact because it ignores local headers and central directory records.
- A more accurate formula adds 30 bytes plus name/extra lengths for the local header, plus 46 bytes plus name/extra/comment lengths for the central directory record.
- The end-of-directory record contributes 22 bytes plus the zip comment length to the total file size.
- This true-impact calculation helps predict size changes when adding/removing entries or comparing two zip versions.
- The calculation is approximate due to potential data descriptor trailers not exposed by the Java API.