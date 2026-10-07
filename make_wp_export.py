import xml.etree.ElementTree as ET
from datetime import datetime

# Build clean WordPress eXtended RSS (WXR) 1.2 XML file
xml_content = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
	xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:wp="http://wordpress.org/export/1.2/"
>
<channel>
	<title>SelfHostStack</title>
	<link>https://selfhoststack.com</link>
	<description>Best Self-Hosted Apps &amp; Homelab Software Directory</description>
	<pubDate>Wed, 07 Oct 2026 12:00:00 +0000</pubDate>
	<language>en-US</language>
	<wp:wxr_version>1.2</wp:wxr_version>
	<wp:base_site_url>https://selfhoststack.com</wp:base_site_url>
	<wp:base_blog_url>https://selfhoststack.com</wp:base_blog_url>

	<!-- Categories -->
	<wp:category>
		<wp:term_id>10</wp:term_id>
		<wp:category_nicename>productivity-apps</wp:category_nicename>
		<wp:category_parent></wp:category_parent>
		<wp:cat_name><![CDATA[Productivity Apps]]></wp:cat_name>
		<wp:category_description><![CDATA[Self-hosted note-taking, wikis, and task management applications.]]></wp:category_description>
	</wp:category>
	<wp:category>
		<wp:term_id>11</wp:term_id>
		<wp:category_nicename>privacy-tools</wp:category_nicename>
		<wp:category_parent></wp:category_parent>
		<wp:cat_name><![CDATA[Privacy & Security]]></wp:cat_name>
		<wp:category_description><![CDATA[Self-hosted password managers, bookmark archives, and encryption tools.]]></wp:category_description>
	</wp:category>
	<wp:category>
		<wp:term_id>12</wp:term_id>
		<wp:category_nicename>homelab-guides</wp:category_nicename>
		<wp:category_parent></wp:category_parent>
		<wp:cat_name><![CDATA[Homelab Guides]]></wp:cat_name>
		<wp:category_description><![CDATA[VPS provisioning, Docker Engine tutorials, and reverse proxy configuration.]]></wp:category_description>
	</wp:category>

	<!-- Page: About Us -->
	<item>
		<title>About SelfHostStack</title>
		<link>https://selfhoststack.com/about/</link>
		<pubDate>Wed, 07 Oct 2026 12:00:00 +0000</pubDate>
		<dc:creator><![CDATA[ashirwad_admin]]></dc:creator>
		<guid isPermaLink="false">https://selfhoststack.com/?page_id=2</guid>
		<description></description>
		<content:encoded><![CDATA[
<h2>About SelfHostStack: Mission, E-E-A-T &amp; Testing Methodology</h2>
<p><strong>SelfHostStack</strong> was created as an academic research and web engineering initiative under <strong>CSET489: Search Engine Optimization</strong>. The platform’s mission is to provide developers, computer science students, and privacy-conscious professionals with reproducible, benchmarked, and technically rigorous documentation for self-hosting open-source software.</p>
<h3>Our Testing Methodology &amp; Hardware Testbed</h3>
<p>Unlike content farms that republish scraped software descriptions, every guide on SelfHostStack is deployed and validated on live Linux servers:</p>
<ul>
<li><strong>Container Reproducibility:</strong> Validated Docker Compose manifests using Docker Engine 26+ and Compose V2 syntax.</li>
<li><strong>Resource Telemetry:</strong> Real RAM and CPU consumption measurements under idle and load using <code>docker stats</code>.</li>
<li><strong>Security Verification:</strong> Operation behind Nginx reverse proxies using Full (Strict) TLS 1.3 encryption.</li>
</ul>
<h3>Lead Strategist &amp; Author Profile</h3>
<p>Designed and maintained by <strong>Ashirwad Pratap Singh</strong>, Computer Science &amp; Engineering undergraduate (Roll No: <code>E23CSEU0221</code>).</p>
		]]></content:encoded>
		<wp:post_id>2</wp:post_id>
		<wp:post_date>2026-10-07 12:00:00</wp:post_date>
		<wp:post_name>about</wp:post_name>
		<wp:status>publish</wp:status>
		<wp:post_type>page</wp:post_type>
	</item>

	<!-- Post 1: Open Source Notion Alternatives -->
	<item>
		<title>Best Open Source Notion Alternatives to Self-Host (2026 Comparison)</title>
		<link>https://selfhoststack.com/blog/open-source-notion-alternatives/</link>
		<pubDate>Wed, 07 Oct 2026 12:30:00 +0000</pubDate>
		<dc:creator><![CDATA[ashirwad_admin]]></dc:creator>
		<guid isPermaLink="false">https://selfhoststack.com/?p=101</guid>
		<category domain="category" nicename="productivity-apps"><![CDATA[Productivity Apps]]></category>
		<content:encoded><![CDATA[
<p>If you have found yourself frustrated by Notion's rising subscription costs, lack of a true offline mode, or data sovereignty concerns, this guide evaluates the top open-source alternatives deployed on a live Ubuntu VPS.</p>
<h2>Comparison Summary</h2>
<table>
<thead><tr><th>Tool</th><th>Architecture</th><th>RAM (Idle)</th><th>Database Views</th><th>License</th></tr></thead>
<tbody>
<tr><td><strong>AppFlowy</strong></td><td>Rust + Flutter</td><td>~120 MB</td><td>Grid, Kanban, Calendar</td><td>AGPL-3.0</td></tr>
<tr><td><strong>Docmost</strong></td><td>Node + Postgres</td><td>~350 MB</td><td>Hierarchical Wiki</td><td>AGPL-3.0</td></tr>
<tr><td><strong>AFFiNE</strong></td><td>Node + Canvas</td><td>~420 MB</td><td>Whiteboard + Tables</td><td>MIT</td></tr>
<tr><td><strong>SiYuan</strong></td><td>Single binary</td><td>~110 MB</td><td>Relational Blocks</td><td>AGPL-3.0</td></tr>
</tbody>
</table>
<h2>1. AppFlowy — Closest Direct Alternative</h2>
<p>AppFlowy delivers native desktop performance with cross-platform synchronization, making it ideal for individual knowledge workers.</p>
<h2>2. Docmost — Best for Engineering Wikis</h2>
<p>Docmost specializes in real-time collaborative documentation, serving as an exceptional hybrid between Notion and Confluence.</p>
		]]></content:encoded>
		<wp:post_id>101</wp:post_id>
		<wp:post_date>2026-10-07 12:30:00</wp:post_date>
		<wp:post_name>open-source-notion-alternatives</wp:post_name>
		<wp:status>publish</wp:status>
		<wp:post_type>post</wp:post_type>
	</item>

	<!-- Post 2: How to Self-Host on a VPS -->
	<item>
		<title>How to Self-Host on a Cloud VPS: Zero-to-Production Blueprint</title>
		<link>https://selfhoststack.com/blog/how-to-self-host-on-vps/</link>
		<pubDate>Wed, 07 Oct 2026 13:00:00 +0000</pubDate>
		<dc:creator><![CDATA[ashirwad_admin]]></dc:creator>
		<guid isPermaLink="false">https://selfhoststack.com/?p=102</guid>
		<category domain="category" nicename="homelab-guides"><![CDATA[Homelab Guides]]></category>
		<content:encoded><![CDATA[
<p>A complete beginner-to-production guide covering cloud VPS provisioning, SSH Ed25519 authentication, UFW firewall configuration, Docker Engine installation, and Cloudflare Full Strict SSL integration.</p>
<h2>Step 1: SSH Key Generation</h2>
<pre><code>ssh-keygen -t ed25519 -C "admin@selfhoststack.com" -f ~/.ssh/id_ed25519_vps</code></pre>
<h2>Step 2: UFW Firewall Hardening</h2>
<pre><code>sudo ufw default deny incoming
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable</code></pre>
		]]></content:encoded>
		<wp:post_id>102</wp:post_id>
		<wp:post_date>2026-10-07 13:00:00</wp:post_date>
		<wp:post_name>how-to-self-host-on-vps</wp:post_name>
		<wp:status>publish</wp:status>
		<wp:post_type>post</wp:post_type>
	</item>

	<!-- Post 3: Self-Hosted Bookmark Managers -->
	<item>
		<title>Best Self-Hosted Bookmark Managers: Linkding vs Karakeep vs Linkwarden</title>
		<link>https://selfhoststack.com/blog/self-hosted-bookmark-managers/</link>
		<pubDate>Wed, 07 Oct 2026 13:30:00 +0000</pubDate>
		<dc:creator><![CDATA[ashirwad_admin]]></dc:creator>
		<guid isPermaLink="false">https://selfhoststack.com/?p=103</guid>
		<category domain="category" nicename="privacy-tools"><![CDATA[Privacy & Security]]></category>
		<content:encoded><![CDATA[
<p>Comparison of modern self-hosted bookmarking platforms evaluating Linkding (SQLite minimalism), Karakeep (AI automatic tagging), and Linkwarden (full-page PDF archiving).</p>
		]]></content:encoded>
		<wp:post_id>103</wp:post_id>
		<wp:post_date>2026-10-07 13:30:00</wp:post_date>
		<wp:post_name>self-hosted-bookmark-managers</wp:post_name>
		<wp:status>publish</wp:status>
		<wp:post_type>post</wp:post_type>
	</item>

	<!-- Post 4: Vaultwarden Docker Compose Setup -->
	<item>
		<title>Vaultwarden Docker Compose Setup with Automated Backups</title>
		<link>https://selfhoststack.com/blog/vaultwarden-docker-compose-setup/</link>
		<pubDate>Wed, 07 Oct 2026 14:00:00 +0000</pubDate>
		<dc:creator><![CDATA[ashirwad_admin]]></dc:creator>
		<guid isPermaLink="false">https://selfhoststack.com/?p=104</guid>
		<category domain="category" nicename="privacy-tools"><![CDATA[Privacy & Security]]></category>
		<content:encoded><![CDATA[
<p>Production deployment walkthrough for Vaultwarden running behind an Nginx reverse proxy with automated SQLite database snapshots via cron.</p>
		]]></content:encoded>
		<wp:post_id>104</wp:post_id>
		<wp:post_date>2026-10-07 14:00:00</wp:post_date>
		<wp:post_name>vaultwarden-docker-compose-setup</wp:post_name>
		<wp:status>publish</wp:status>
		<wp:post_type>post</wp:post_type>
	</item>
</channel>
</rss>
"""

out_path = r"C:\Users\ASHIRWAD PRATAPSINGH\Downloads\SEO\PROJECT_EVIDENCE\configuration\selfhoststack_wordpress_import.xml"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(xml_content.strip())
print(f"Generated WordPress WXR export file: {out_path} ({len(xml_content):,} bytes)")
