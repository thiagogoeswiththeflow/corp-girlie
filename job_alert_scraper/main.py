from notion_api import push_to_notion
import datetime

def main():
    today = datetime.datetime.utcnow().date()

    all_jobs = [
        {
            "Job Title": "Customer Success Manager (Test)",
            "Company": "Notion Tester Inc.",
            "Location": "Remote",
            "Remote/Hybrid": "Remote",
            "Platform": "Manual",
            "Link": "https://example.com/job",
            "Posted Date": str(today),
            "Match %": 95,
            "Suggested CV Tweaks": "No changes needed – this is a test row."
        }
    ]

    push_to_notion(all_jobs)

if __name__ == "__main__":
    main()
