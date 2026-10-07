# Phase 4: Direct Competitor Analysis

**Course**: CSET489: Search Engine Optimization  
**Project**: SelfHostStack  
**Author**: Ashirwad Pratap Singh (Roll No: E23CSEU0221)  
**Milestone**: Milestone I (Evaluation Weight: 2 Marks — Target: Excellent 2.0/2.0)  

---

## 1. Selected Direct Competitors
To benchmark our SEO strategy against live authority in the self-hosted software and homelab publishing space, two prominent direct competitors were audited:

1. **Competitor 1**: `noted.lol` (Niche Editorial Tech Publication & Review Blog)
2. **Competitor 2**: `selfh.st` (Ecosystem Aggregator, Directory & Weekly Publication)

---

## 2. In-Depth Competitor Audits

### Competitor 1: Noted.lol
* **Domain**: `noted.lol`
* **Founder / Editorial Lead**: Jeremy
* **Core Content Model**: Hands-on software reviews, container walkthroughs, personal homelab updates, and offline Kiwix `.zim` archives.
* **Site Architecture**: Standard Ghost/CMS blog layout with horizontal tag navigation (`/tag/self-hosted`, `/tag/guides`). Lacks hierarchical topical silos.
* **Top-Ranking Keywords**:
  * `"noted lol"` (Navigational, Vol: 1,400)
  * `"docmost review"` (Commercial, Vol: 350)
  * `"linkwarden docker"` (Transactional, Vol: 480)
  * `"self-hosting 101"` (Informational, Vol: 290)
* **Backlink Profile**: Strong organic backlinks from Reddit (`r/selfhosted`), GitHub repositories, and tech enthusiast newsletters. Estimated referring domains: ~450–700.
* **Strengths**: High topical authority, rapid coverage of new GitHub releases, active community Discord.
* **Weaknesses**:
  1. *Flat Architecture*: Articles are presented chronologically; lack of strict parent-child topical clustering causes keyword cannibalization between multiple reviews of similar apps.
  2. *Absence of Comparative Benchmarks*: Reviews evaluate apps in isolation without objective side-by-side spec comparison tables (e.g. idle RAM, database engine, storage footprint).
  3. *Assumes Intermediate Knowledge*: Setup guides frequently omit firewall, SSL origin, and DNS reverse-proxy prerequisites, frustrating beginners.

---

### Competitor 2: Selfh.st
* **Domain**: `selfh.st`
* **Founder / Curator**: Ethan Sholly
* **Core Content Model**: Weekly curated newsletter (*Self-Host Weekly*), searchable software directory (`selfh.st/apps`), dashboard icon library (`selfh.st/icons`), and annual community survey.
* **Site Architecture**: Custom web application featuring directory databases, tag filters, and newsletter archive posts.
* **Top-Ranking Keywords**:
  * `"selfh st"` (Navigational, Vol: 2,900)
  * `"self host weekly"` (Navigational, Vol: 850)
  * `"self hosted apps directory"` (Commercial, Vol: 720)
  * `"homelab dashboard icons"` (Transactional, Vol: 1,100)
* **Backlink Profile**: Very strong backlink equity from integrations; popular homelab dashboard projects (Homepage, Homarr, Glance) link directly to `selfh.st/icons`. Estimated referring domains: ~1,200+.
* **Strengths**: Exceptional minimalist UX/UI, high brand loyalty, authoritative index of open-source projects.
* **Weaknesses**:
  1. *Thin Content on App Pages*: Directory listings contain only a 2-sentence summary, license tag, and GitHub link. They do not rank for informational search intent like "how to install..." or "best... for team collaboration".
  2. *Zero Deployment Guides*: Does not provide Docker Compose templates, configuration troubleshooting, or terminal walkthroughs.
  3. *Uncaptured Long-Tail Queries*: Missing out on hundreds of high-value "how-to", "alternative to", and "vs" long-tail search queries.

---

## 3. Head-to-Head Competitor Comparison Table

| Feature / SEO Metric | Competitor 1 (`noted.lol`) | Competitor 2 (`selfh.st`) | Our Project (`SelfHostStack`) |
|---|---|---|---|
| **Primary Content Format** | In-depth editorial reviews | Software directory & newsletter | Educational tutorials + Siloed clusters + Decision tables |
| **Site Architecture** | Flat chronological blog | Directory web app | Rigid hierarchical topic clusters (Silos) |
| **Target Audience Focus** | Intermediate homelabbers | Broad community / developers | Students & engineers seeking practical deployment |
| **Comparative Tables** | Sparse / rare | Tag filters only | Systematic side-by-side matrices on all MoFU pages |
| **Tested Docker Configurations** | Included in body text | None | Standardized, syntax-validated copyable blocks |
| **Hardware & RAM Telemetry** | Qualitative | None | Quantitative empirical RAM/CPU measurements |
| **Internal Linking Depth** | Weak (tag-based) | Moderate (directory tags) | Strict parent-child breadcrumbs & contextual sibling links |
| **Mobile Speed & Usability** | Moderate | Fast | Ultra-fast (LiteSpeed / clean responsive theme) |
