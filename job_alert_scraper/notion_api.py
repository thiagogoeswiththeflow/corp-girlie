import os
import requests

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

def push_to_notion(jobs):
    print(f"DEBUG: Received {len(jobs)} jobs")

    url = f"https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    for job in jobs:
        data = {
            "parent": {"database_id": DATABASE_ID},
            "properties": {
                "Job Title": {"title": [{"text": {"content": job["title"]}}]},
                "Company": {"rich_text": [{"text": {"content": job["company"]}}]},
                "Location": {"rich_text": [{"text": {"content": job["location"]}}]},
                "Remote/Hybrid": {"rich_text": [{"text": {"content": job["remote"]}}]},
                "Platform": {"rich_text": [{"text": {"content": job["platform"]}}]},
                "Link": {"url": job["url"]},
                "Posted Date": {"date": {"start": job["date_posted"]}},
            },
        }

        response = requests.post(url, headers=headers, json=data)
        print("DEBUG: Response status:", response.status_code)
        print("DEBUG: Response body:", response.text)
