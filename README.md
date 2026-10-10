# ⚡ SelfHostStack

> **The Open-Source Knowledge Hub & Directory for Self-Hosted Applications, Privacy Tools, and Homelab Architectures.**

[![Project Status](https://img.shields.io/badge/status-active-success.svg)](#)
[![Team](https://img.shields.io/badge/team-Cosmic__Coder-blueviolet.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](#)
[![SEO Performance](https://img.shields.io/badge/SEO-Optimized-brightgreen.svg)](#)

----

## 📖 Overview

**SelfHostStack** is an academic research and technical documentation initiative designed to explore and demonstrate data-driven organic search architecture, topic cluster modeling, and reproducible Linux server deployments for self-hosted software.

The platform provides developers, sysadmins, and homelab enthusiasts with verified Docker Compose recipes, benchmarked hardware footprints, and in-depth software comparisons across privacy-first applications.

---

## 🎯 Key Pillars & Features

- **Topical Silo Architecture**: Three dedicated content silos engineered to eliminate keyword cannibalization:
  - **Knowledge & Productivity**: Open-source alternatives to SaaS suites (AppFlowy, Docmost, AFFiNE, SiYuan, Anytype).
  - **Privacy & Security**: Zero-knowledge password management (Vaultwarden) and web archival bookmark managers (Linkding, Karakeep, Linkwarden).
  - **Homelab & VPS Guides**: Hardened Ubuntu 24.04 LTS deployment blueprint with UFW, SSH keys, Docker Engine, and Nginx reverse proxy.
- **Data-Backed SEO Implementation**:
  - Keyword targeting verified with **KD < 20** for high organic search acquisition.
  - Semantic HTML5 with breadcrumbs and Schema.org structured data (`TechArticle`, `HowTo`).
  - Featured snippet captures with Markdown tables and bulleted matrices.
- **Infrastructure & Deployment Ready**:
  - Cloudflare Full (Strict) SSL / TLS 1.3 configuration.
  - Automated LEMP stack deployment scripts with WP-CLI automation.
  - Static site optimized for sub-second Core Web Vitals (LCP < 0.8s, 0 CLS).

---

## 🚀 Running the Website Locally

You can preview the live static website locally using Python's built-in HTTP server:

```bash
# Clone the repository
git clone https://github.com/bhupendrasinghh/SelfHostStack.git
cd SelfHostStack

# Serve the static website
python3 -m http.server 8000 --directory site
```

Visit **https://selfhoststackfinal.onrender.com** in your browser.

---

## 📂 Repository Structure

```text
├── site/                           # Production static website
│   ├── index.html                  # Homepage (Core Silos & Directory)
│   ├── about/                      # E-E-A-T & Methodology documentation
│   ├── category/                   # Silo landing pages
│   │   ├── productivity-apps/
│   │   ├── privacy-tools/
│   │   └── homelab-guides/
│   ├── blog/                       # In-depth technical articles & guides
│   │   ├── open-source-notion-alternatives/
│   │   ├── how-to-self-host-on-vps/
│   │   ├── vaultwarden-docker-compose-setup/
│   │   └── self-hosted-bookmark-managers/
│   └── assets/                     # Modular CSS design system & typography
├── docs/                           # Phase-by-phase strategic documentation (Phases 1-14)
├── PROJECT_EVIDENCE/               # Research artifacts, server configs, and terminal logs
│   ├── configuration/              # LEMP deployment scripts & WP import XML
│   ├── research/                   # Keyword & competitor matrix CSVs
│   ├── terminal_logs/              # SSH & deployment logs
│   └── final_report/               # Comprehensive academic final report
├── KEYWORD_PAGE_MAPPING.md         # Keyword-to-URL governance and intent mapping
├── SERP_ANALYSIS.md                # SERP breakdown, PAA queries & Featured Snippet targeting
├── CONTENT_GAP_ANALYSIS.md         # Direct competitor evaluation matrix
├── CLOUDFLARE_CONFIGURATION.md     # DNS, edge caching, and SSL hardening specs
├── VPS_DEPLOYMENT.md               # Production Linux VPS setup logs
└── README.md                       # Repository overview and documentation
```

---

## 👥 Maintained By

Designed, developed, and maintained by **Team Cosmic_Coder**.

- **Course**: CSET489: Search Engine Optimization
- **Repository**: [https://github.com/bhupendrasinghh/SelfHostStack](https://github.com/bhupendrasinghh/SelfHostStack)
