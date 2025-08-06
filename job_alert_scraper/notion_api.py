# job_alert_scraper/notion_api.py

import requests
import json
import os

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")


HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def push_to_notion(jobs):
    for job in jobs:
        data = {
            "parent": {"database_id": DATABASE_ID},
            "properties": {
                "Job Title": {"title": [{"text": {"content": job["Job Title"]}}]},
                "Company": {"rich_text": [{"text": {"content": job["Company"]}}]},
                "Location": {"rich_text": [{"text": {"content": job["Location"]}}]},
                "Remote/Hybrid": {"select": {"name": job["Remote/Hybrid"]}},
                "Platform": {"rich_text": [{"text": {"content": job["Platform"]}}]},
                "Link": {"url": job["Link"]},
                "Posted Date": {"date": {"start": job["Posted Date"]}},
                "Match %": {"number": job["Match %"]},
                "Suggested CV Tweaks": {"rich_text": [{"text": {"content": job["Suggested CV Tweaks"][:2000]}}]},
            }
        }

        response = requests.post("https://api.notion.com/v1/pages", headers=HEADERS, data=json.dumps(data))

        if response.status_code != 200:
            print(f"Failed to push job: {job['Job Title']} at {job['Company']}. Status: {response.status_code}")
            print(response.text)
