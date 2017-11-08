# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "candidate_registration"
app_title = "Candidate Registration"
app_publisher = "Frappe"
app_description = "App for managing Candidate Details for Interviews"
app_icon = "oction oction-book"
app_color = "#589494"
app_email = "info@frappe.io"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/candidate_registration/css/candidate_registration.css"
# app_include_js = "/assets/candidate_registration/js/candidate_registration.js"

# include js, css files in header of web template
# web_include_css = "/assets/candidate_registration/css/candidate_registration.css"
# web_include_js = "/assets/candidate_registration/js/candidate_registration.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "candidate_registration.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "candidate_registration.install.before_install"
# after_install = "candidate_registration.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "candidate_registration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"candidate_registration.tasks.all"
# 	],
# 	"daily": [
# 		"candidate_registration.tasks.daily"
# 	],
# 	"hourly": [
# 		"candidate_registration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"candidate_registration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"candidate_registration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "candidate_registration.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "candidate_registration.event.get_events"
# }

