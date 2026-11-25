# ── APP METADATA ───────────────────────────────────────────────────────────────
app_name = "primers_desk"
app_title = "Primer’s Solution"
app_publisher = "Primer’s Solution"
app_description = "Professional white-label theme for Frappe/ERPNext"
app_email = "sales@primers.com"
app_license = "MIT"
app_color = "#E8610A"
app_icon = "octicon octicon-paintcan"
app_version = "3.2.0"

required_apps = []

# ── PUBLIC LOGIN ASSETS ────────────────────────────────────────────────────────
web_include_css = ["/assets/primers_desk/css/login.css?v=12"]
web_include_js = ["/assets/primers_desk/js/login_theme.js?v=9"]

# ── AUTHENTICATED DESK ASSETS ──────────────────────────────────────────────────
# Query versions are bumped whenever an asset changes to invalidate browser cache.
app_include_css = [
    "/assets/primers_desk/css/primers_desk.css?v=68",
    "/assets/primers_desk/css/sidebar.css?v=39",
    "/assets/primers_desk/css/command_palette.css?v=5",
    "/assets/primers_desk/css/smart_home.css?v=9",
    "/assets/primers_desk/css/progressive_forms.css?v=4",
    "/assets/primers_desk/css/notification_center.css?v=4",
    "/assets/primers_desk/css/polish.css?v=4",
    "/assets/primers_desk/css/dark_mode.css?v=19",
    "/assets/primers_desk/css/module_cards.css?v=5",
    "/assets/primers_desk/css/density.css?v=4",
    "/assets/primers_desk/css/theme_studio.css?v=22",
    "/assets/primers_desk/css/grid_row_slide_panel.css?v=2",
    "/assets/primers_desk/css/workspace_layout.css?v=8",
    "/assets/primers_desk/css/announcements.css?v=3",
    "/assets/primers_desk/css/activity_panel.css?v=1",
    "/assets/primers_desk/css/stat_buttons.css?v=1",
    "/assets/primers_desk/css/dashboard_filter.css?v=2",
    "/assets/primers_desk/css/invoice_tabs.css?v=1",
    "/assets/primers_desk/css/white_label.css?v=1",
]
app_include_js = [
    "/assets/primers_desk/js/frappe_compat.js?v=5",
    "/assets/primers_desk/js/dark_mode.js?v=12",
    "/assets/primers_desk/js/personalization.js?v=1",
    "/assets/primers_desk/js/primers_desk.js?v=72",
    "/assets/primers_desk/js/sidebar.js?v=3",
    "/assets/primers_desk/js/command_palette.js?v=10",
    "/assets/primers_desk/js/progressive_forms.js?v=4",
    "/assets/primers_desk/js/notification_center.js?v=5",
    "/assets/primers_desk/js/module_cards.js?v=12",
    "/assets/primers_desk/js/theme_runtime.js?v=13",
    "/assets/primers_desk/js/chart_runtime.js?v=5",
    "/assets/primers_desk/js/grid_row_slide_panel.js?v=1",
    "/assets/primers_desk/js/workspace_layout.js?v=7",
    "/assets/primers_desk/js/announcements.js?v=3",
    "/assets/primers_desk/js/activity_panel.js?v=1",
    "/assets/primers_desk/js/stat_buttons.js?v=2",
    "/assets/primers_desk/js/dashboard_filter.js?v=2",
    "/assets/primers_desk/js/quick_entry_extras.js?v=1",
    "/assets/primers_desk/js/invoice_tabs.js?v=1",
    "/assets/primers_desk/js/white_label.js?v=2",
]

# ── BOOT / INSTALL / DOCUMENT LIFECYCLE HOOKS ──────────────────────────────────
boot_session = "primers_desk.boot.add_boot_data"

after_install = "primers_desk.setup.after_install"
after_migrate = "primers_desk.setup.after_migrate"

# Notification read state: see primers_desk/notifications.py
override_whitelisted_methods = {
    "frappe.desk.doctype.notification_log.notification_log.get_notification_logs": "primers_desk.notifications.get_notification_logs",
}

doc_events = {
    "Theme Settings": {
        "on_update": "primers_desk.events.theme_settings_on_update",
    },
    "Company": {
        "after_insert": "primers_desk.events.company_after_insert",
    },
}
