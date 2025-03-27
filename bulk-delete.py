# Script: Jira Bulk User Deletion Tool (Standalone, Using `requests`)

# Attribution & Purpose
# This script deletes Jira users in bulk using a CSV export of users.
# It uses the `requests` library to interact with the Jira API.
# 
# Powered by **Jupytyzer GPT** and **A9 Consulting Group, Inc.**

import pandas as pd
import requests
from datetime import datetime

# === Configuration ===
CSV_PATH = "export-delete.csv"  # Path to your cleaned CSV file
JIRA_URL = "https://your-domain.atlassian.net"  # Base URL for your Jira instance
API_EMAIL = "you@example.com"  # Jira user email
API_TOKEN = "your_api_token"  # API token from Atlassian
LOG_FILE = f"jira_delete_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# === Read CSV ===
try:
    df = pd.read_csv(CSV_PATH)
    required_columns = ['User id', 'User name', 'email']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"CSV is missing required column: '{col}'")
except Exception as e:
    print(f"Failed to load CSV: {e}")
    exit(1)

# === Deletion Logic ===
headers = {
    "Authorization": f"Basic {requests.auth._basic_auth_str(API_EMAIL, API_TOKEN).split(' ')[1]}",
    "Accept": "application/json"
}

with open(LOG_FILE, 'w') as log:
    for _, row in df.iterrows():
        user_id = row['User id']
        user_name = row['User name']
        email = row['email']
        endpoint = f"{JIRA_URL}/rest/api/3/user?accountId={user_id}"
        response = requests.delete(endpoint, headers=headers)
        if response.status_code == 204:
            msg = f"✅ Deleted user {user_id} | {user_name} | {email}"
        else:
            msg = f"❌ Failed to delete {user_id} | {user_name} | {email}: {response.status_code} {response.text}"
        print(msg)
        log.write(msg + "\n")

print(f"\nLog saved to: {LOG_FILE}")
