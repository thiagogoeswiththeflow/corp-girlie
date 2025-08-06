from filters import filter_and_score_jobs
from notion_api import push_to_notion
import datetime

def main():
    today = datetime.datetime.utcnow().date()

    # Dummy job to test Notion push
    all_jobs = [
        {
            "Job Title": "Customer Success Manager (Test)",
            "Company": "Notion Tester Inc.",
            "Location": "Remote",
            "Remote/Hybrid": "Remote",
            "Platform": "Manual",
            "Link": "https://example.com/job",
            "Posted Date": str(today),
        }
    ]

    filtered_jobs = filter_and_score_jobs(all_jobs)
    push_to_notion(filtered_jobs)

if __name__ == "__main__":
    main()
