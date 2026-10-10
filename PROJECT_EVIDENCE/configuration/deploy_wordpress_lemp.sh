#!/usr/bin/env bash
# ==============================================================================
# Script: deploy_wordpress_lemp.sh
# Course: CSET489 Search Engine Optimization - Practical Mini-Project (Milestone I)
# Author: Team Cosmic_Coder
# Project: SelfHostStack (LEMP Stack Automated WordPress Deployment)
# Target OS: Ubuntu 22.04 / 24.04 LTS
# ==============================================================================

set -euo pipefail

# --- Color Codes for Logging ---
GREEN='\033[032m'
BLUE='\033[034m'
YELLOW='\033[133m'
RED='\033[031m'
NC='\033[0m'

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# --- Configuration Variables ---
DOMAIN_NAME="${1:-selfhoststack.com}"
WP_DB_NAME="selfhost_wp"
WP_DB_USER="wp_admin_usr"
# Generate secure random DB password if not provided
WP_DB_PASS="${2:-$(openssl rand -base64 18 | tr -dc 'a-zA-Z0-9')}"
WP_ADMIN_USER="cosmic_coder"
WP_ADMIN_PASS="${3:-$(openssl rand -base64 16 | tr -dc 'a-zA-Z0-9')}"
WP_ADMIN_EMAIL="Cosmic_Coder"
WEB_ROOT="/var/www/selfhoststack"

log_info "Starting Automated LEMP WordPress Deployment for domain: ${DOMAIN_NAME}"

# 1. System Update & Package Installation
log_info "Step 1: Updating apt repositories and upgrading system..."
export DEBIAN_FRONTEND=noninteractive
apt update -y && apt upgrade -y

log_info "Installing prerequisite tools and dependencies..."
apt install -y ufw curl wget git unzip certbot python3-certbot-nginx fail2ban htop

# 2. Configure UFW Firewall
log_info "Step 2: Configuring UFW Firewall..."
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp comment 'SSH'
ufw allow 80/tcp comment 'HTTP'
ufw allow 443/tcp comment 'HTTPS'
echo "y" | ufw enable || true
ufw status verbose

# 3. Install Nginx Web Server
log_info "Step 3: Installing and configuring Nginx..."
apt install -y nginx
systemctl enable nginx
systemctl start nginx

# 4. Install MariaDB Server
log_info "Step 4: Installing and configuring MariaDB Database Server..."
apt install -y mariadb-server mariadb-client
systemctl enable mariadb
systemctl start mariadb

# Create WordPress Database and User
log_info "Creating MariaDB database and user..."
mysql -e "CREATE DATABASE IF NOT EXISTS \`${WP_DB_NAME}\` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -e "CREATE USER IF NOT EXISTS '${WP_DB_USER}'@'localhost' IDENTIFIED BY '${WP_DB_PASS}';"
mysql -e "GRANT ALL PRIVILEGES ON \`${WP_DB_NAME}\`.* TO '${WP_DB_USER}'@'localhost';"
mysql -e "FLUSH PRIVILEGES;"

# 5. Install PHP 8.3 & Required Extensions
log_info "Step 5: Installing PHP-FPM and required WordPress extensions..."
apt install -y php8.3-fpm php8.3-mysql php8.3-curl php8.3-gd php8.3-mbstring \
               php8.3-xml php8.3-xmlrpc php8.3-soap php8.3-intl php8.3-zip \
               php8.3-bcmath php8.3-imagick
systemctl enable php8.3-fpm
systemctl start php8.3-fpm

# 6. Install WP-CLI (Command Line Tool for WordPress)
log_info "Step 6: Installing WP-CLI..."
if [ ! -f /usr/local/bin/wp ]; then
    curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
    chmod +x wp-cli.phar
    mv wp-cli.phar /usr/local/bin/wp
fi
wp --info

# 7. Download and Setup WordPress
log_info "Step 7: Provisioning WordPress in ${WEB_ROOT}..."
mkdir -p "${WEB_ROOT}"
cd "${WEB_ROOT}"

wp core download --allow-root

# Generate wp-config.php
log_info "Configuring wp-config.php..."
wp config create \
    --dbname="${WP_DB_NAME}" \
    --dbuser="${WP_DB_USER}" \
    --dbpass="${WP_DB_PASS}" \
    --dbhost="localhost" \
    --extra-php <<PHP
define('WP_DEBUG', false);
define('WP_MEMORY_LIMIT', '256M');
define('DISALLOW_FILE_EDIT', true);
PHP
    --allow-root

# Run WordPress Initial Installation
log_info "Executing WP core install..."
wp core install \
    --url="https://${DOMAIN_NAME}" \
    --title="SelfHostStack — Open-Source Self-Hosted Software & Privacy Tools" \
    --admin_user="${WP_ADMIN_USER}" \
    --admin_password="${WP_ADMIN_PASS}" \
    --admin_email="${WP_ADMIN_EMAIL}" \
    --skip-email \
    --allow-root

# Configure Permalinks to %postname% for SEO
log_info "Setting SEO-friendly Permalinks (/blog/%postname%/)..."
wp rewrite structure '/%postname%/' --allow-root
wp rewrite flush --allow-root

# 8. Configure Nginx Server Block
log_info "Step 8: Writing optimized Nginx VirtualHost configuration..."
cat > "/etc/nginx/sites-available/${DOMAIN_NAME}" <<EOF
server {
    listen 80;
    listen [::]:80;
    server_name ${DOMAIN_NAME} www.${DOMAIN_NAME};
    root ${WEB_ROOT};
    index index.php index.html index.htm;

    # Security Headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    # Gzip Compression
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml application/json application/javascript application/rss+xml image/svg+xml;

    location / {
        try_files \$uri \$uri/ /index.php?\$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.3-fpm.sock;
        fastcgi_param SCRIPT_FILENAME \$document_root\$fastcgi_script_name;
        include fastcgi_params;
    }

    # Deny access to sensitive files
    location ~* /(?:uploads|files)/.*\.php$ {
        deny all;
    }

    location ~ /\.ht {
        deny all;
    }

    location = /favicon.ico {
        log_not_found off;
        access_log off;
    }

    location = /robots.txt {
        log_not_found off;
        access_log off;
        allow all;
    }

    # Cache static assets
    location ~* \.(css|js|jpg|jpeg|png|gif|ico|webp|svg|woff|woff2|ttf|otf)$ {
        expires 30d;
        add_header Cache-Control "public, no-transform";
    }
}
EOF

ln -sf "/etc/nginx/sites-available/${DOMAIN_NAME}" /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t
systemctl reload nginx

# 9. Set File Permissions
log_info "Step 9: Setting ownership and permissions for www-data..."
chown -R www-data:www-data "${WEB_ROOT}"
find "${WEB_ROOT}" -type d -exec chmod 755 {} \;
find "${WEB_ROOT}" -type f -exec chmod 644 {} \;

# 10. Summary Report
log_success "=============================================================="
log_success "WordPress LEMP Deployment Successfully Completed!"
log_success "Domain: https://${DOMAIN_NAME}"
log_success "Web Root: ${WEB_ROOT}"
log_success "Database Name: ${WP_DB_NAME}"
log_success "Database User: ${WP_DB_USER}"
log_success "WP Admin Username: ${WP_ADMIN_USER}"
log_success "WP Admin URL: https://${DOMAIN_NAME}/wp-admin/"
log_success "=============================================================="
