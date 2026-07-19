# Substack Private RSS Feeds for Paid Subscribers

## Question

Does Substack provide paid subscribers with a private RSS feed URL (containing an auth token) that unlocks subscriber-only articles (written posts)? Or do you need to use headers/cookies for authentication?

## Sources

- [Is there an RSS feed for my publication? (Substack Help Center)](https://support.substack.com/hc/en-us/articles/360038239391-Is-there-an-RSS-feed-for-my-publication)
- [Will my Podcast RSS feed show paid-only content? (Substack Help Center)](https://support.substack.com/hc/en-us/articles/360041722272-Will-my-Podcast-RSS-feed-show-paid-only-content)
- [How do I listen to episodes on my podcast app? (Substack Help Center)](https://support.substack.com/hc/en-us/articles/4519588148244-How-do-I-listen-to-episodes-on-my-podcast-app)
- [How do I add audience-specific content to a post on Substack? (Substack Help Center)](https://support.substack.com/hc/en-us/articles/50558240901268-How-do-I-add-audience-specific-content-to-a-post-on-Substack)
- [How do I listen to paid episodes on Spotify? (Substack Help Center)](https://support.substack.com/hc/en-us/articles/25303480158228-How-do-I-listen-to-paid-episodes-on-Spotify)
- [ByteByteGo public RSS feed](https://blog.bytebytego.com/feed)

## Findings

### 1. Public written-content RSS feeds show only the "Not subscribed" version

Substack provides a single public RSS feed for written (newsletter) content at `https://your.substack.com/feed`. According to the audience-specific content help article:

> "RSS feeds and search engine crawlers see the **Not subscribed** version of any audience section."

This means the public feed only ever serves content visible to unauthenticated / non-subscribed users. Paid-only content is excluded. Confirmed by inspecting `https://blog.bytebytego.com/feed` — it contains full-article content for free articles but omits subscriber-only posts.

### 2. Private RSS feeds exist only for podcasts — not for written posts

Substack's help center explicitly states that **podcast** subscribers receive a unique private RSS feed:

> "Each subscriber gets a private Podcast RSS feed that's unique to them. Depending on whether or not they have a paid subscription, the feed might include public episodes or public and paid episodes."
> — *Will my Podcast RSS feed show paid-only content?*

The steps to access this private podcast feed are documented in *How do I listen to episodes on my podcast app?*:
1. Sign into Substack and go to the Manage Subscription page (or `https://substack.com/settings`).
2. Scroll to the **"Private podcast feeds"** section and click "Set up podcast".
3. Copy the unique feed URL and paste it into a podcast app.

### 3. No equivalent private RSS feed for written / newsletter posts

There is **no Substack help article** describing a private RSS feed for written (non-podcast) content. The only article about newsletter RSS feeds is *Is there an RSS feed for my publication?*, which simply documents the public `https://your.substack.com/feed` URL. There is no mention of per-subscriber auth tokens, private feed URLs, or cookie-based RSS authentication for written content anywhere in Substack's official documentation.

### 4. Authentication for paid written content requires browser session / cookies

The Substack settings page (`https://substack.com/settings`) lists a **"Private podcast feeds"** section for podcast feeds only. For written content, access to subscriber-only posts is controlled through the web session (cookies) when logged in on the Substack website or app. Substack does not document any RSS-based method for authenticating as a paid subscriber to access paid-written articles programmatically.

## Conclusion

**No.** Substack does **not** provide a private RSS feed URL (with an auth token) for written newsletter posts. Private per-subscriber RSS feeds exist **only for podcasts**. For written posts, the only available feed is the public `https://your.substack.com/feed`, which serves only the "Not subscribed" version of all content — paid-only posts are entirely absent.

To access subscriber-only written content programmatically, you would need to use cookies/session authentication against Substack's web API, not RSS. There is no official Substack documentation describing an RSS-based authentication mechanism for paid subscribers of written publications.
