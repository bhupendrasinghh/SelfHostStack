# Keyword-to-Page Mapping & Cannibalization Prevention Matrix

**Course**: CSET489: Search Engine Optimization  
**Project**: SelfHostStack  
**Author**: Team Cosmic_Coder  
**Milestone**: Milestone I (Evaluation Weight: 2 Marks — Target: Excellent 2.0/2.0)  

---

## 1. Executive Summary & Objective
Keyword-to-page mapping establishes a 1-to-1 contractual relationship between a target search query and its designated landing page. Without deliberate mapping, multiple pages on a website inevitably target the same primary query—a critical algorithmic penalty known as **Keyword Cannibalization**. 

This document defines the master keyword assignment matrix and documents the verification protocol ensuring that every page serves a distinct search intent.

---

## 2. Master Keyword-to-Page Mapping Matrix

| Page Name | Canonical URL | Primary Target Keyword | Secondary Target Keywords | Semantic / LSI Phrases | Search Intent | Priority | Content Purpose |
|---|---|---|---|---|---|---|---|
| **Homepage** | `/` | `best self hosted apps` | `homelab software list`, `lightweight homelab docker stack` | `top self hosted tools`, `open source personal cloud apps` | Commercial / Informational | **P0** | Central brand portal, curated software directory, site-wide pillar anchor. |
| **About Page** | `/about/` | `SelfHostStack testing lab` | `open source software testing methodology`, `self hosted benchmarks` | `hardware testbed`, `authoritative homelab reviews` | Informational (E-E-A-T) | **P1** | Establish author credibility (CS engineering student, server lab), testbed hardware specs. |
| **Category: Productivity** | `/category/productivity-apps/` | `self hosted productivity tools` | `self hosted note taking app`, `open source personal wiki software` | `digital workspace self hosted`, `markdown knowledge base` | Informational | **P1** | Pillar hub grouping knowledge management, wikis, and task tools. |
| **Article: Notion Alternatives** | `/blog/open-source-notion-alternatives/` | `open source notion alternative` | `appflowy vs notion self hosted`, `docmost notion alternative` | `self hosted block editor`, `local first markdown wiki` | Commercial Investigation | **P0** | In-depth comparison of AppFlowy, Docmost, and AFFiNE with copyable Docker Compose templates. |
| **Article: Docmost vs AppFlowy** | `/blog/docmost-vs-appflowy/` | `docmost vs appflowy` | `docmost review`, `appflowy self hosting guide` | `collaborative wiki vs desktop app`, `flutter rust vs nodejs wiki` | Commercial (Comparison) | **P2** | Direct head-to-head decision matrix for the two top contenders. |
| **Category: Privacy Tools** | `/category/privacy-tools/` | `secure self hosted password manager` | `self hosted privacy tools`, `homelab security stack` | `zero knowledge encryption`, `local data privacy` | Informational | **P1** | Pillar hub grouping password managers, bookmarkers, and ad-blockers. |
| **Article: Bookmark Managers** | `/blog/self-hosted-bookmark-managers/` | `self hosted bookmark manager` | `self hosted readwise alternative`, `self hosted linkding guide` | `self hosted bookmarking with ai tagging`, `linkwarden docker` | Commercial / Informational | **P0** | Evaluation of Linkding, Karakeep/Hoarder, and Linkwarden with browser sync. |
| **Article: Vaultwarden Setup** | `/blog/vaultwarden-docker-compose-setup/` | `vaultwarden docker compose` | `vaultwarden backup automated cron`, `self hosted bitwarden setup` | `vaultwarden sqlite backup`, `caddy reverse proxy vaultwarden` | Transactional (Deployment) | **P0** | End-to-end production deployment guide with backup scripts and SSL. |
| **Category: Homelab Guides** | `/category/homelab-guides/` | `vps homelab setup` | `linux server self hosting`, `cloud vps homelab guides` | `ubuntu server docker`, `reverse proxy caddy nginx` | Informational | **P1** | Pillar hub covering VPS provisioning, reverse proxies, and networking. |
| **Article: Self-Host on VPS** | `/blog/how-to-self-host-on-vps/` | `how to self host on a vps` | `how to install docker on ubuntu vps`, `nginx proxy manager ssl cloudflare setup` | `ssh key authentication`, `ufw firewall docker security` | Informational (Tutorial) | **P0** | Foundational zero-to-hero server provisioning and Docker setup guide. |
| **Article: RSS Reader Docker** | `/blog/self-hosted-rss-reader-docker/` | `self hosted rss reader docker` | `miniflux vs freshrss comparison`, `miniflux docker compose` | `lightweight feed reader self hosted`, `freshrss sqlite` | Informational / Transactional | **P1** | Comparative tutorial between Miniflux and FreshRSS with Docker configs. |

---

## 3. Keyword Cannibalization Audit & Prevention Protocol

### Strict Prevention Rules
1. **Single Primary Destination**: Under no circumstances may two URLs target identical primary keywords in their `<title>` tags or `<h1>` headers.
2. **Distinct Intent Partitioning**:
   * The Category page `/category/productivity-apps/` targets the broad plural informational query `self hosted productivity tools`.
   * The child article `/blog/open-source-notion-alternatives/` targets the specific comparison query `open source notion alternative`.
   * The child article `/blog/docmost-vs-appflowy/` targets the head-to-head decision query `docmost vs appflowy`.
   * Search intent does not overlap: a user searching for "productivity tools" wants a general directory, while a user searching for "docmost vs appflowy" has already filtered down to two specific applications.
3. **Anchor Text Governance**:
   * When linking to `/blog/open-source-notion-alternatives/`, internal links must strictly use variations of *"open source Notion alternatives"* or *"Notion self-hosted replacements"*.
   * Internal links pointing to `/` must use brand anchors (*"SelfHostStack"*) or broad directory anchors (*"best self hosted apps list"*).
   * Internal links pointing to `/blog/docmost-vs-appflowy/` must exclusively use the comparative anchor *"Docmost vs AppFlowy comparison"*.

### Verification Checklist

| Primary Keyword | Assigned Page | Secondary Mentions Permitted? | Cannibalization Risk |
|---|---|---|---|
| `best self hosted apps` | `/` (Homepage) | Contextual mentions only; never in H1/H2 of subpages | **Zero** |
| `open source notion alternative` | `/blog/open-source-notion-alternatives/` | Allowed as reference in `/category/productivity-apps/` | **Zero** |
| `docmost vs appflowy` | `/blog/docmost-vs-appflowy/` | Sibling link from Notion alternatives article | **Zero** |
| `self hosted bookmark manager` | `/blog/self-hosted-bookmark-managers/` | Allowed as list item on `/category/privacy-tools/` | **Zero** |
| `vaultwarden docker compose` | `/blog/vaultwarden-docker-compose-setup/` | Mentioned as recommended container in VPS guide | **Zero** |
| `how to self host on a vps` | `/blog/how-to-self-host-on-vps/` | Linked from all deployment guides as prerequisite | **Zero** |
