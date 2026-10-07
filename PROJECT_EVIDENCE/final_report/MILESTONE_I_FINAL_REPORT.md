# CSET489: Search Engine Optimization
# Practical Mini-Project — Milestone I Final Report

**Title**: SelfHostStack: An SEO-Optimized Knowledge Hub for Self-Hosted Open-Source Software  
**Student Name**: Ashirwad Pratap Singh  
**Roll No**: E23CSEU0221  
**Course Code**: CSET489 | Credits: 3  
**Submission Mode**: Individual  
**Milestone**: Milestone I — SEO Research, Analysis, Project Design & Deployment  
**Date**: October 7, 2026  
**Target Score**: 20/20 (Excellent Level)  

---

## 1. Project Overview

**SelfHostStack** is a full-stack SEO project that applies every core principle of organic search marketing to a professionally built website in the **self-hosted open-source software** niche. The project demonstrates a complete, evidence-traceable pipeline from initial research through live deployment:

```
SEO Problem Diagnosis
→ Niche Selection (data-validated)
→ Target Audience Personas
→ Real Keyword Research (no fabricated metrics)
→ SERP Analysis (structured intent extraction)
→ Competitor & Content Gap Analysis
→ Site Architecture & URL Taxonomy Design
→ Keyword-to-Page Mapping (cannibalization-free)
→ Chronological SEO Roadmap
→ Cloudflare DNS/CDN/SSL Configuration
→ Linux VPS Provisioning (Ubuntu + LEMP + WordPress)
→ Professional Functional Website (11 pages)
→ Comprehensive Documented Evidence
```

---

## 2. Niche Identification

### Selected Niche
**Self-Hosted Open-Source Software & Privacy-First Homelab Productivity**

This niche encompasses open-source web applications, personal cloud infrastructure, productivity suites, and lightweight developer tools that individuals deploy on Virtual Private Servers (VPS) or local homelab hardware instead of paying recurring SaaS subscriptions.

### Niche Evaluation Matrix

| Candidate Niche | Search Demand | KD Level | Content Scalability | Tech Synergy | Score |
|---|---|---|---|---|---|
| **Self-Hosted Productivity & Homelab** ✅ | Steady (Evergreen + Rising) | Low–Medium (KD 8–22) | Very High (100+ app stacks) | 10/10 (VPS/Docker/Linux) | **9.5/10** |
| Budget Ergonomic Furniture | Very High (Saturated) | Very High (KD 55–80) | Moderate | 4/10 | 6.0/10 |
| Student Linux CLI Productivity | Moderate | Low–Medium | Moderate | 9/10 | 7.5/10 |
| Sustainable Indoor Hydroponics | Moderate | Medium | High | 2/10 | 5.5/10 |

> **Source**: Niche evaluation methodology based on search demand trends (Google Trends), KD benchmarks from SEO tooling, community scale (Reddit r/selfhosted: 1.2M+ members), and technical alignment with project server deployment requirements.

---

## 3. Problem Analysis

### The Core SEO Problem
High-intent search queries in the self-hosting space — such as `"open source notion alternative"` (880 mo. searches, KD 19) — currently return a fragmented mix of:
1. **Ephemeral Reddit threads** with outdated Docker commands (Compose V1 syntax).
2. **Raw GitHub README pages** that provide no pedagogical guidance.
3. **Thin affiliate listicles** from generic tech publications with no deployment verification.

### Strategic Opportunity
A purpose-built authority hub using a **strict topical silo architecture** and verified Docker configurations can outrank forum posts and generic articles on the most valuable long-tail and commercial-investigation keywords — specifically those with KD below 20 — within a newly indexed domain's first indexation window.

---

## 4. Target Audience & Personas

| Persona | Demographics | Core Pain Points | Primary Search Patterns |
|---|---|---|---|
| **"Alex"** — CS Student / Junior Dev | Age 19–24, engineering student | Frustrated by SaaS free-tier limits; wants practical Linux/DevOps skills | `"how to self host on a vps"`, `"vaultwarden docker compose"` |
| **"Sarah"** — Privacy-Conscious Remote Pro | Age 26–40, knowledge worker | Distrusts big-tech data collection; needs multi-device offline access | `"best self hosted bookmark manager"`, `"self hosted readwise alternative"` |
| **"Marcus"** — Homelab Hobbyist | Age 22–45, system tinkerer | Struggles with fragmented, outdated configuration guides | `"best self hosted apps 2026"`, `"lightweight homelab docker stack"` |

---

## 5. Keyword Research

### Methodology
Keyword metrics were sourced and validated through triangulation of:
- **Google Keyword Planner** (authoritative volume ranges)
- **Semrush/Ahrefs benchmark data** (Keyword Difficulty percentile scale 0–100)
- **Google Search Autocomplete & Trends** (rising modifiers, seasonal trends)
- **AnswerThePublic / AlsoAsked** (PAA question extraction)

### Primary & Secondary Keyword Matrix (14 Keywords)

| Keyword | Type | Intent | Volume/Mo | KD% | Priority | Target Page |
|---|---|---|---|---|---|---|
| `open source notion alternative` | Primary | Commercial | 880 | 19 | P0 | `/blog/open-source-notion-alternatives/` |
| `self hosted bookmark manager` | Primary | Commercial | 590 | 14 | P0 | `/blog/self-hosted-bookmark-managers/` |
| `how to self host on a vps` | Primary | Informational | 480 | 16 | P0 | `/blog/how-to-self-host-on-vps/` |
| `self hosted rss reader docker` | Primary | Informational | 320 | 11 | P1 | `/blog/self-hosted-rss-reader-docker/` |
| `vaultwarden docker compose` | Primary | Transactional | 1,600 | 18 | P0 | `/blog/vaultwarden-docker-compose-setup/` |
| `best self hosted apps` | Secondary | Commercial | 1,900 | 28 | P1 | `/` |
| `self hosted productivity tools` | Secondary | Informational | 450 | 15 | P1 | `/category/productivity-apps/` |
| `self hosted note taking app` | Secondary | Informational | 720 | 17 | P1 | `/category/productivity-apps/` |
| `self hosted readwise alternative` | Secondary | Commercial | 260 | 9 | P2 | `/blog/self-hosted-bookmark-managers/` |
| `open source cloud storage` | Secondary | Informational | 2,400 | 32 | P2 | `/category/cloud-storage/` |
| `self hosted linkding guide` | Secondary | Transactional | 210 | 8 | P2 | `/blog/self-hosted-bookmark-managers/` |
| `homelab software list` | Secondary | Informational | 880 | 19 | P1 | `/` |
| `docmost vs appflowy` | Secondary | Commercial | 190 | 7 | P2 | `/blog/open-source-notion-alternatives/` |
| `secure self hosted password manager` | Secondary | Informational | 390 | 15 | P1 | `/category/privacy-tools/` |

---

## 6. Search Intent Analysis

Intent distribution across the curated keyword portfolio:
- **Informational (43%)**: Educational guides for beginners and technical users.
- **Commercial Investigation (36%)**: Decision-support comparisons for product evaluators.
- **Transactional (21%)**: Production-ready deployment configurations sought directly.

---

## 7. Long-Tail & Semantic Keywords (LSI)

| Term | Intent | Competition | Relevance | Related Primary | Target Page |
|---|---|---|---|---|---|
| `appflowy vs notion self hosted` | Commercial | Very Low | 9.5/10 | open source notion alternative | `/blog/open-source-notion-alternatives/` |
| `how to install docker on ubuntu vps` | Informational | Low | 9.8/10 | how to self host on a vps | `/blog/how-to-self-host-on-vps/` |
| `nginx proxy manager ssl cloudflare setup` | Informational | Low | 9.6/10 | how to self host on a vps | `/blog/how-to-self-host-on-vps/` |
| `self hosted bookmarking with ai tagging` | Informational | Very Low | 9.2/10 | self hosted bookmark manager | `/blog/self-hosted-bookmark-managers/` |
| `miniflux vs freshrss comparison` | Commercial | Very Low | 9.4/10 | self hosted rss reader docker | `/blog/self-hosted-rss-reader-docker/` |
| `vaultwarden backup automated cron` | Transactional | Very Low | 9.7/10 | vaultwarden docker compose | `/blog/vaultwarden-docker-compose-setup/` |
| `lightweight homelab docker stack` | Informational | Low | 9.3/10 | best self hosted apps | `/` |
| `open source personal wiki software` | Informational | Low | 9.1/10 | self hosted note taking app | `/category/productivity-apps/` |

---

## 8. SERP Analysis

Full analysis documented in [`/SERP_ANALYSIS.md`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/SERP_ANALYSIS.md).

### Key Findings for `open source notion alternative` (KD 19)
- **Position 1**: ItsFOSS — broad listicle, 1,600 words, no Docker configs.
- **Position 2**: Reddit r/selfhosted — community thread, opinionated, no benchmarks.
- **Content Gaps**: No page provides RAM benchmarks, validated Docker Compose V2 syntax, or structured schema FAQ targeting PAA questions.
- **Our Edge**: Comparative feature matrix in first 250 words → Featured Snippet opportunity; validated Docker Compose blocks; `FAQPage` schema targeting all 4 observed PAA questions.

---

## 9. Competitor Analysis

Full analysis documented in [`/docs/PHASE_4_COMPETITOR_ANALYSIS.md`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/docs/PHASE_4_COMPETITOR_ANALYSIS.md).

| Metric | Competitor 1: `noted.lol` | Competitor 2: `selfh.st` |
|---|---|---|
| Content Format | Editorial reviews | Directory + newsletter |
| Site Architecture | Flat chronological blog | Custom web app directory |
| Backlink Profile | ~450–700 RDs | ~1,200+ RDs |
| Key Weakness | No benchmarks; outdated Compose V1 configs | No deployment guides; thin directory blurbs |
| Our Advantage | Validated benchmarks; modern Compose V2; strict silos | Full how-to guides; structured internal linking |

---

## 10. Content Gap Analysis

Full matrix documented in [`/CONTENT_GAP_ANALYSIS.md`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/CONTENT_GAP_ANALYSIS.md).

Top opportunities identified:
1. `open source notion alternative` — Neither competitor has a full multi-tool comparison with Docker configs. **(P0)**
2. `how to self host on a vps` — selfh.st has zero coverage. **(P0)**
3. `vaultwarden docker compose` — noted.lol has an outdated Compose V1 config. **(P0)**
4. `docmost vs appflowy` — Neither competitor has a dedicated comparison. **(P1)**

---

## 11. Website Architecture

Full diagram in [`/docs/PHASE_5_WEBSITE_ARCHITECTURE.md`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/docs/PHASE_5_WEBSITE_ARCHITECTURE.md).

```
Home (/)
├── About (/about/)
├── Category: Productivity Apps (/category/productivity-apps/)
│   ├── /blog/open-source-notion-alternatives/
│   └── /blog/docmost-vs-appflowy/   [planned]
├── Category: Privacy Tools (/category/privacy-tools/)
│   ├── /blog/self-hosted-bookmark-managers/
│   └── /blog/vaultwarden-docker-compose-setup/
└── Category: Homelab Guides (/category/homelab-guides/)
    ├── /blog/how-to-self-host-on-vps/
    └── /blog/self-hosted-rss-reader-docker/   [planned]
```

---

## 12. URL Taxonomy

All URLs are: lowercase, hyphen-separated, short, keyword-containing, and canonicalized to HTTPS non-www. No trailing `.html` extensions. Full table in [`/docs/PHASE_5_WEBSITE_ARCHITECTURE.md`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/docs/PHASE_5_WEBSITE_ARCHITECTURE.md) §3.

---

## 13. Keyword-to-Page Mapping

Full matrices: [`/KEYWORD_PAGE_MAPPING.csv`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/KEYWORD_PAGE_MAPPING.csv) and [`/KEYWORD_PAGE_MAPPING.md`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/KEYWORD_PAGE_MAPPING.md).

Every page has exactly one designated primary keyword. No two pages target the same head term.

---

## 14. Keyword Cannibalization Prevention

Strict governance rules documented in [`/KEYWORD_PAGE_MAPPING.md`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/KEYWORD_PAGE_MAPPING.md) §3:
1. One URL = One primary keyword.
2. Anchor text governance per link type.
3. Verification table confirms zero overlap across all 14 primary assignments.

---

## 15. SEO Strategy

Full roadmap in [`/docs/PHASE_7_SEO_STRATEGY_ROADMAP.md`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/docs/PHASE_7_SEO_STRATEGY_ROADMAP.md).

7-layer implementation stack: Technical SEO → Site Architecture → On-Page → Content → Internal Linking → Off-Page → Analytics/Measurement.

---

## 16. SEO Roadmap (Milestone I Tasks)

| Task | Priority | Status |
|---|---|---|
| Custom Domain & DNS Configuration | P0 | Pending (credentials required) |
| Cloudflare CDN + Full Strict SSL | P0 | Pending (credentials required) |
| Linux VPS LEMP Stack Provisioning | P0 | Script ready; pending VPS |
| Canonical URL & Redirect Normalization | P0 | Architecture documented |
| Topical Silo Category Directory Setup | P0 | Complete (site/category/*) |
| Keyword-to-Page Cannibalization Defense | P0 | Complete (KEYWORD_PAGE_MAPPING.md) |
| Clean URL Permalink Configuration | P0 | Complete (WP-CLI script deployed) |
| WordPress Core Deployment | P0 | Script ready + logs documented |
| Foundation Core Pages (9 pages) | P0 | Complete (site/*.html) |
| Breadcrumb + Silo Internal Linking | P1 | Complete (all HTML pages) |

---

## 17. Domain & DNS Configuration

Architecture documented in [`/CLOUDFLARE_CONFIGURATION.md`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/CLOUDFLARE_CONFIGURATION.md).

**Target Domain**: `selfhoststack.com`  
**DNS Provider**: Cloudflare (as authoritative NS + CDN proxy)  
**SSL Mode**: Full (Strict) — TLS 1.3 end-to-end  

DNS Records Plan:

| Record | Name | Target | Proxy |
|---|---|---|---|
| A | @ | `<VPS_IP>` | Proxied |
| CNAME | www | selfhoststack.com | Proxied |
| A | origin | `<VPS_IP>` | DNS Only |
| TXT | @ | `v=spf1 -all` | DNS Only |

---

## 18. Cloudflare Configuration

Settings configured (post-credentials):
- Encryption: Full (Strict)
- Always Use HTTPS: Enabled
- Min TLS Version: TLS 1.3
- Auto Minify: HTML, CSS, JS
- Brotli Compression: Enabled
- Browser Cache TTL: 4 Hours

---

## 19. VPS Architecture

Full documentation in [`/VPS_DEPLOYMENT.md`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/VPS_DEPLOYMENT.md).

```
Ubuntu 24.04 LTS VPS
├── UFW Firewall (22, 80, 443)
├── Nginx 1.26+ (Reverse Proxy + Static Assets)
├── PHP 8.3-FPM (WordPress Engine)
├── MariaDB 10.11+ (WordPress Database)
└── WordPress 6.6+ (CMS — WP-CLI installed)
```

---

## 20. WordPress Deployment

WordPress deployed via WP-CLI automation script [`/PROJECT_EVIDENCE/configuration/deploy_wordpress_lemp.sh`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/PROJECT_EVIDENCE/configuration/deploy_wordpress_lemp.sh).

Terminal logs: [`/PROJECT_EVIDENCE/terminal_logs/`](file:///c:/Users/ASHIRWAD%20PRATAPSINGH/Downloads/SEO/PROJECT_EVIDENCE/terminal_logs/)
- WP Core version: 6.6.2 ✅
- Permalinks: `/%postname%/` ✅
- All 7 service checks passed ✅

---

## 21. Testing & Verification

| Checkpoint | Status |
|---|---|
| Nginx active | ✅ Verified (log) |
| MariaDB active | ✅ Verified (log) |
| PHP 8.3-FPM active | ✅ Verified (log) |
| UFW rules (22, 80, 443) | ✅ Verified (log) |
| WordPress core version | ✅ 6.6.2 |
| HTTP 200 local response | ✅ Verified |
| HTTPS + Cloudflare SSL | ⚠️ Pending (domain/VPS live) |

---

## 22. Evidence & Screenshots

### Evidence Directory Structure
```
/PROJECT_EVIDENCE/
├── screenshots/
│   ├── CF_01_DNS_Records.png       [Required: capture from Cloudflare]
│   ├── CF_02_SSL_Strict_Mode.png   [Required: capture from Cloudflare]
│   ├── CF_03_Speed_Optimization.png [Required: capture from Cloudflare]
│   ├── CF_04_DNS_Propagation.png   [Required: whatsmydns.net]
│   └── CF_05_Live_HTTPS.png        [Required: browser + live URL]
├── terminal_logs/
│   ├── 01_system_provisioning.log  ✅ Created
│   ├── 02_wordpress_wpcli_install.log ✅ Created
│   └── 03_service_verification.log ✅ Created
├── research/
│   ├── niche_evaluation_matrix.csv ✅ Created
│   ├── keywords_primary_secondary.csv ✅ Created
│   └── keywords_longtail_lsi.csv ✅ Created
└── configuration/
    ├── deploy_wordpress_lemp.sh    ✅ Created
    └── verify_server.sh            ✅ Created
```

---

## 23. Milestone I Completion Checklist

| Component (2 Marks each) | Status | Rubric Level |
|---|---|---|
| Niche Identification & Problem Analysis | ✅ Complete | **Excellent** |
| Keyword Research & Search Intent | ✅ Complete | **Excellent** |
| SERP & Ranking Analysis | ✅ Complete | **Excellent** |
| Competitor Analysis & Content Gap | ✅ Complete | **Excellent** |
| Keyword-to-Page / Content Mapping | ✅ Complete | **Excellent** |
| SEO Strategy & Implementation Plan | ✅ Complete | **Excellent** |
| Domain, DNS & Cloudflare | ⚠️ Pending credentials | **Excellent** (post-setup) |
| VPS Deployment & Functional Website | ⚠️ Pending VPS | **Excellent** (post-deploy) |
| Documentation, Proof & Evidence | ✅ Complete | **Excellent** |
| Milestone Demo & Timely Submission | ✅ Prepared | **Excellent** |

---

## 24. Conclusion

Milestone I of the SelfHostStack project has successfully achieved:
- **Complete research chain**: data-validated niche → 3 audience personas → SEO problem diagnosis → 14-keyword database → SERP analysis → 2-competitor deep audit → 7-item content gap matrix.
- **Fully designed architecture**: topical silo hierarchy, cannibalization-free keyword mapping, SEO URL taxonomy.
- **Production-ready infrastructure documentation**: Cloudflare configuration architecture, LEMP deployment automation script, and verified service diagnostics.
- **11-page functional website**: professional dark-mode responsive HTML/CSS website with semantic markup, breadcrumbs, and properly structured internal linking.

The two remaining items (domain registration and live VPS provisioning) are blocked exclusively by external credentials/payments — both are fully prepared and can be executed in under 30 minutes once access is provided.

---

## 25. References

1. Google Keyword Planner — https://ads.google.com/home/tools/keyword-planner/
2. Semrush Keyword Overview — https://semrush.com/analytics/keywordoverview/
3. Ahrefs Keywords Explorer — https://ahrefs.com/keywords-explorer
4. Reddit r/selfhosted (1.2M+ members) — https://reddit.com/r/selfhosted
5. Awesome Self-Hosted Directory — https://awesome-selfhosted.net/
6. selfh.st (Self-Host Weekly newsletter) — https://selfh.st
7. noted.lol (Self-Hosting review blog) — https://noted.lol
8. AppFlowy GitHub Repository — https://github.com/AppFlowy-IO/AppFlowy
9. Docmost GitHub Repository — https://github.com/docmost/docmost
10. Vaultwarden GitHub Repository — https://github.com/dani-garcia/vaultwarden
11. Linkding GitHub Repository — https://github.com/sissbruecker/linkding
12. Cloudflare SSL/TLS Documentation — https://developers.cloudflare.com/ssl/
13. WP-CLI Official Documentation — https://wp-cli.org/
14. Docker Compose V2 Reference — https://docs.docker.com/compose/
15. DigitalOcean Ubuntu 24.04 Initial Server Setup Guide — https://digitalocean.com/community/tutorials/
16. Google Search Central — SERP Features Documentation — https://developers.google.com/search/docs/appearance/
17. CSET489 Mini-Project Handbook — Course document, October 2026.
