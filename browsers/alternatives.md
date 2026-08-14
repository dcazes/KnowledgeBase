---
type: Reference
title: "Browsers — Alternatives"
description: "Side-by-side comparison of the four browser/scraping programs documented in this vault — Firecrawl, Camofox, CloakBrowser, and SurfSense — and the alternatives each source lists."
resource: "https://github.com/firecrawl/firecrawl"
tags: [browsers, alternatives, comparison]
generated: { by: "agent:fixer", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "agent:fixer", at: "2026-08-13T00:00:00Z" } ]
status: draft
stale_after: 2027-02-09
sources:
  - id: s1
    resource: "https://github.com/firecrawl/firecrawl"
    title: "Firecrawl — Alternatives"
    author: human:daniel
  - id: s2
    resource: "https://github.com/daijro/camoufox"
    title: "Camofox — Alternatives"
    author: human:daniel
  - id: s3
    resource: "https://github.com/cloakhq/cloakbrowser"
    title: "CloakBrowser — Alternatives"
    author: human:daniel
  - id: s4
    resource: "https://github.com/modsetter/surfsense"
    title: "SurfSense — Alternatives"
    author: human:daniel
---

# Browsers — Alternatives

The browser/scraping programs documented under `browsers/` are alternatives to one another in the loose sense that they overlap in the job they do — turning web content into usable data for agents — while differing in base engine, stealth posture, and delivery model. This doc compares them side by side and summarizes the alternatives each program's own doc lists. Where a source is thin or silent, that is stated plainly.

## Comparison matrix

| Program | Primary purpose | Key differentiators | Best for | Notable alternatives |
|---|---|---|---|---|
| **Firecrawl** | All-in-one, agent-ready web context API (search + scrape + crawl + extract), self-hostable | Unified API + stack; partial anti-bot (no Fire-engine self-host per source) | Unified search/scrape/crawl/extract for agents | Crawl4AI, ScraperAPI, Apify, Playwright, Jina AI |
| **Camofox** | Firefox-based anti-detection, watchable browser server for agents | Firefox/Camoufox base, strong anti-detection, watchable via noVNC, Playwright-compatible | Agent browser backend; fragile/anti-bot flows | Raw Camoufox, Playwright, Puppeteer, Undetected-Chromedriver, CloakBrowser |
| **CloakBrowser** | Brave/Chromium browser driven via CDP for automation/stealth | Brave/Chromium base, CDP on :9222, persistent profiles | Chromium automation + persistent profiles | Camofox, Playwright, Puppeteer, Undetected-Chromedriver |
| **SurfSense** | Scraped personal graph + AI Q&A with MCP; platform scrapers (Reddit/YouTube/Instagram/TikTok/Maps/Indeed) plus its own knowledge base | Self-hosted, graph-based, agent-accessible; described as "RUNNING here" | Personal-web capture / personal knowledge assistant | Obsidian, Supermemory, Mem0/MemOS, Rewind, Firecrawl + vector/graph backend |

A few cross-cutting observations from the sources:

- **Camofox and CloakBrowser name each other as alternatives** — the Camofox doc lists CloakBrowser (a separate stealth browser server already in the stack) and the CloakBrowser doc lists Camofox, each framed as "pick whichever fits the workflow." Neither source claims one is strictly better; both are stealth-oriented, with Camofox on Firefox and CloakBrowser on Chromium.
- **Playwright, Puppeteer, and Undetected-Chromedriver recur across sources** as the non-stealth / Chromium-stealth automation options. All sources agree these are detectable as automation by default and best for non-anti-bot work.
- **SurfSense's alternatives doc does not actually compare against other browser/scraping programs.** Its source file (type `Comparison`) positions it against personal-knowledge tools — Obsidian, Supermemory, Mem0/MemOS, Rewind — plus a DIY Firecrawl + vector/graph pipeline. The only browser-side overlap in the sources is the Firecrawl doc, which lists SurfSense as *complementary* for social-platform capture rather than a direct alternative.

## Firecrawl

Source scope: Firecrawl is compared against **Crawl4AI, ScraperAPI, Apify, Playwright (raw), and Jina AI** — scraping/crawling services and libraries, not stealth browsers.

Tradeoffs summarized from the source:

- **Crawl4AI** — lightweight open-source Python library for LLM-ready crawling (markdown, chunking, structured extraction). Cheaper and simpler inside a Python/RAG app, but you build orchestration/queues yourself and it is weaker at scale/anti-bot than Firecrawl cloud.
- **ScraperAPI** — hosted proxy API (IP rotation, CAPTCHAs, JS rendering). Zero infra and strong anti-bot, but paid/cloud, no crawl orchestration, and data leaves to the vendor.
- **Apify** — hosted platform with prebuilt "Actors" and a queue/store. Managed scale and a large actor ecosystem, but cloud, cost at scale, and heavier to learn.
- **Playwright (raw)** — scriptable browser automation; the engine under Firecrawl's playwright-service. Total control, free, but you implement everything (queues, retries, parsing) and it is not agent-ready by itself.
- **Jina AI** — hosted reader + embedding API for clean article text and vectors. Trivial clean-read and good for RAG ingestion, but reader-only (no crawl/search/extract orchestration) and cloud.

The source's decision guide picks Firecrawl as the central extraction engine (already deployed, wired to SearXNG), and notes SurfSense fills a different niche for social-platform capture.

See also: [Firecrawl index](./firecrawl/index.md)

## Camofox

Source scope: Camofox is compared against **raw Camoufox, Playwright, Puppeteer, Undetected-Chromedriver, and CloakBrowser** — stealth browsers and automation libraries.

Tradeoffs summarized from the source:

- **Camoufox (raw library)** — the engine under Camofox, used directly in Python (Playwright-compatible). Same stealth with no server overhead and full code control, but you build the API/VNC/serving layer yourself.
- **Playwright** — mature, multi-browser (Chromium/Firefox/WebKit) automation; what Firecrawl uses for rendering. Good for normal automation and bulk extraction, but detectable as automation and not for anti-bot sites.
- **Puppeteer** — Chromium automation for Node. Excellent Chromium control from JS, but detectable, Chromium-only, and no stealth by default.
- **Undetected-Chromedriver** — patches Selenium/ChromeDriver to evade detection. Chromium stealth without a Firefox fork, but a cat-and-mouse game with Chrome updates and less consistent fingerprinting than Camoufox.
- **CloakBrowser** — a separate stealth browser server already in the stack. Integrated stealth browsing service, but distinct from Camofox; evaluate which fits a given task.

The source's bottom line: Camofox is the pick for agent-facing, watchable, Firefox anti-detection (used as a Hermes backend here); raw Camoufox when you want the stealth engine in your own code; Playwright/Puppeteer for non-stealth automation; Undetected-Chromedriver for stealth Chrome specifically.

See also: [Camofox index](./camofox/index.md)

## CloakBrowser

Source scope: CloakBrowser is compared against **Camofox, Playwright, Puppeteer, and Undetected-Chromedriver**.

Tradeoffs summarized from the source:

- **Camofox** — Firefox-based anti-detection with a Playwright-compatible API and watchable/VNC experience. The choice when Firefox stealth or noVNC watchability matters more than Chromium.
- **Playwright** — general multi-browser automation (Chromium/Firefox/WebKit) via its native API. Great for non-stealth scraping (Firecrawl uses it for rendering), less stealthy out of the box than CloakBrowser or Camofox.
- **Puppeteer** — Node Chromium automation over CDP. The source describes it as essentially the low-level tool CloakBrowser builds on; use it directly for full control without the wrapper.
- **Undetected-Chromedriver** — patched ChromeDriver to dodge bot detection. Chromium-only stealth with more cat-and-mouse than CloakBrowser's Brave base.

The source's decision guide: CloakBrowser for Chromium agent browsing via CDP with persistent profiles; Camofox for Firefox anti-detection; Playwright/Puppeteer for general automation; Undetected-Chromedriver for stealth Chrome specifically.

See also: [CloakBrowser index](./cloakbrowser/index.md)

## SurfSense

Source scope: this source file is thin on browser alternatives — it is a `Comparison` doc that pits SurfSense against **Obsidian, Supermemory, Mem0/MemOS, Rewind, and a DIY Firecrawl + vector/graph pipeline**, i.e. personal knowledge assistants rather than other browser/scraping programs.

Tradeoffs summarized from the source:

- **Obsidian** — local-first Markdown PKM (this vault); full control, Dataview/plugins, but manual/curated rather than automatic.
- **Supermemory** — personal AI memory with browser capture, local-first desktop; simple end-user memory, but "installed but idle here."
- **Mem0 / MemOS** — developer memory platforms (APIs/MCP) aimed at agent memory, not personal-web memory.
- **Rewind** — screen-recording memory that captures everything visually; heavy with a privacy trade-off.
- **Firecrawl + Weaviate** (see the architecture docs) — a self-hosted scrape→vector stack; more control over the pipeline, but you build it yourself.

The source's bottom line: SurfSense for automatic personal-web memory with AI and agent access (already deployed on this machine), Obsidian for curated manual knowledge, Mem0/MemOS for developer/agent memory, and a Firecrawl + vector/graph backend for a DIY pipeline. The source does not discuss other browser programs; the Firecrawl doc (included above) is the only cross-reference, positioning SurfSense as complementary for social-platform capture.

See also: [SurfSense index](./surfsense/index.md)
