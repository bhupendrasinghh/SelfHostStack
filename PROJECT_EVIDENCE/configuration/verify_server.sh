#!/usr/bin/env bash
# ==============================================================================
# Script: verify_server.sh
# Course: CSET489 Search Engine Optimization - Practical Mini-Project (Milestone I)
# Author: Ashirwad Pratap Singh (Roll No: E23CSEU0221)
# Project: SelfHostStack Verification & Diagnostics Suite
# ==============================================================================

set -u

echo "=================================================================="
echo "    SelfHostStack: Milestone I Server Health & Verification       "
echo "    Date: $(date -u +"%Y-%m-%dT%H:%M:%SZ")                       "
echo "=================================================================="

TOTAL_CHECKS=0
PASSED_CHECKS=0

check_service() {
    local service_name="$1"
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    if systemctl is-active --quiet "$service_name"; then
        echo "[PASS] Service '$service_name' is running and active."
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
    else
        echo "[FAIL] Service '$service_name' is NOT running."
    fi
}

echo -e "\n--- 1. Web & Database Services Status ---"
check_service "nginx"
check_service "mariadb"
check_service "php8.3-fpm"

echo -e "\n--- 2. Firewall Status (UFW) ---"
TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
if ufw status | grep -q "Status: active"; then
    echo "[PASS] UFW Firewall is active."
    PASSED_CHECKS=$((PASSED_CHECKS + 1))
    ufw status numbered
else
    echo "[FAIL] UFW Firewall is NOT active."
fi

echo -e "\n--- 3. Database Connectivity ---"
TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
if mysqladmin ping -u root --silent; then
    echo "[PASS] MySQL daemon is responsive to local ping."
    PASSED_CHECKS=$((PASSED_CHECKS + 1))
else
    echo "[FAIL] MySQL daemon is not responsive."
fi

echo -e "\n--- 4. WordPress Installation & WP-CLI Diagnostics ---"
TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
if [ -f /usr/local/bin/wp ]; then
    WP_VERSION=$(wp core version --path=/var/www/selfhoststack --allow-root 2>/dev/null || echo "Unknown")
    echo "[PASS] WP-CLI is installed. WordPress Core version detected: $WP_VERSION"
    PASSED_CHECKS=$((PASSED_CHECKS + 1))
else
    echo "[FAIL] WP-CLI binary not found at /usr/local/bin/wp."
fi

echo -e "\n--- 5. Local Web Server HTTP Response ---"
TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost/ || echo "000")
if [ "$HTTP_CODE" -eq 200 ] || [ "$HTTP_CODE" -eq 301 ] || [ "$HTTP_CODE" -eq 302 ]; then
    echo "[PASS] Local HTTP endpoint returned status $HTTP_CODE."
    PASSED_CHECKS=$((PASSED_CHECKS + 1))
else
    echo "[FAIL] Local HTTP endpoint returned status $HTTP_CODE."
fi

echo -e "\n=================================================================="
echo " Verification Complete: $PASSED_CHECKS / $TOTAL_CHECKS Checks Passed."
echo "=================================================================="
