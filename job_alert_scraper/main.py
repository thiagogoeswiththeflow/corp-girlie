# job_alert_scraper/main.py

from scraper_remoteok import get_remoteok_jobs
from scraper_builtin import get_builtin_jobs
from filters import filter_and_score_jobs
from notion_api import push_to_notion
import datetime

def main():
    today = datetime.datetime.utcnow().date()

    # Step 1: Scrape jobs (currently Remote OK + Built In, with upcoming support for LinkedIn, Indeed, Glassdoor, Welcome to the Jungle, Otta, and Wellfound)
    remoteok_jobs = get_remoteok_jobs()
    builtin_jobs = get_builtin_jobs()

    # Step 2: Filter and score
    all_jobs = remoteok_jobs + builtin_jobs
    filtered_jobs = filter_and_score_jobs(all_jobs)

    # Step 3: Push to Notion
    push_to_notion(filtered_jobs)

if __name__ == "__main__":
    main()
