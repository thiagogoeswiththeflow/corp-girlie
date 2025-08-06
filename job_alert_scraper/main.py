from filters import filter_and_score_jobs
from notion_api import push_to_notion
import datetime

def main():
    today = datetime.datetime.utcnow().date()

    # 🔧 Add dummy job
    all_jobs = [
        {
            "title": "Test Job Posting",
            "company": "Test Company",
            "location": "Remote",
            "url": "https://example.com/job/test",
            "source": "manual",
            "posted_at": str(today),
        }
    ]

    filtered_jobs = filter_and_score_jobs(all_jobs)
    push_to_notion(filtered_jobs)

if __name__ == "__main__":
    main()
