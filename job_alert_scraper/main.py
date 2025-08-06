from filters import filter_and_score_jobs
from notion_api import push_to_notion
import datetime

def main():
    today = datetime.datetime.utcnow().date()

    # TEMP: Empty job list (no scraping logic yet)
    all_jobs = []

    filtered_jobs = filter_and_score_jobs(all_jobs)
    push_to_notion(filtered_jobs)

if __name__ == "__main__":
    main()
