---
domain: java-tools
subdomain: http-client
concept: declarative-rest-client
title: Easy HTTP Requests with Retrofit
sources:
  - title: "Easy HTTP Requests with Retrofit"
    url: "https://developer.squareup.com/blog/easy-http-requests-with-retrofit"
    author: "Jake Wharton"
---

# Easy HTTP Requests with Retrofit

Retrofit is Square's open-source library that simplifies HTTP communication by converting remote APIs into declarative, type-safe interfaces. Developers define an interface where each method represents a single API endpoint, and annotations such as @GET and @Path describe how the method maps to an HTTP request, including URL replacement blocks and response body types. The article demonstrates this by defining a GitHubService interface with a method to list repository contributors, plus a simple Contributor model class.

- Retrofit turns REST APIs into Java interfaces with methods annotated to describe HTTP requests.
- Annotations like @GET and @Path map method parameters to URL segments, making requests declarative.
- RestAdapter builds a concrete implementation of the API interface, hiding HTTP details behind testable Java objects.
- Retrofit was Square's oldest open source project, first committed by Bob Lee in 2010.