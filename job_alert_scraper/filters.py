# job_alert_scraper/filters.py

from datetime import datetime
import re

# Define your keyword clusters
KEYWORDS = [
    "customer success", "account manager", "implementation specialist",
    "onboarding manager", "customer support manager", "customer experience manager",
    "account executive", "project coordinator",
    "associate", "junior", "lead", "senior"
]

INDUSTRY_TERMS = [
    "SaaS", "startup", "mental health", "climate", "carbon", "non-profit",
    "education", "mission-driven", "tech"
]

LOCATION_KEYWORDS = [
    "remote", "barcelona", "spain", "emea", "europe", "global"
]

def calculate_match_score(job):
    """Assigns a rough match score (0–100) based on how closely the job matches target profile."""
    text = (job.get("Job Title", "") + " " + job.get("Company", "") + " " + job.get("Location", ""))
    text = text.lower()

    keyword_hits = sum(1 for kw in KEYWORDS if kw in text)
    industry_hits = sum(1 for term in INDUSTRY_TERMS if term in text)
    location_hits = sum(1 for loc in LOCATION_KEYWORDS if loc in text)

    score = min(100, 50 + keyword_hits * 10 + industry_hits * 5 + location_hits * 5)
    return score

def generate_cv_suggestion(job, match_score):
    """Suggests a small CV tweak based on missing match elements."""
    title = job.get("Job Title", "").lower()
    suggestions = []

    if "implementation" in title and "project" not in title:
        suggestions.append("Add detail about implementation timelines or cross-team coordination.")
    if "account" in title and "client" not in title:
        suggestions.append("Clarify client-facing or revenue-support experience.")
    if "success" in title and "onboarding" not in title:
        suggestions.append("Mention onboarding or churn reduction experience.")
    if "junior" in title and "associate" not in title:
        suggestions.append("Include the word 'associate' if applicable to past roles.")
    if match_score < 80:
        suggestions.append("Reframe past work to include relevant industry terms like 'SaaS' or 'climate'.")

    return " ".join(suggestions) or "No major changes needed."

def filter_and_score_jobs(job_list):
    filtered = []
    for job in job_list:
        posted = job.get("Posted Date")
        if not posted:
            continue
        try:
            post_date = datetime.strptime(posted, "%Y-%m-%d").date()
            if (datetime.utcnow().date() - post_date).days > 1:
                continue
        except:
            continue

        score = calculate_match_score(job)
        suggestion = generate_cv_suggestion(job, score)

        job["Match %"] = score
        job["Suggested CV Tweaks"] = suggestion
        filtered.append(job)

    # sort by date, then match score desc
    filtered.sort(key=lambda x: (x.get("Posted Date"), -x["Match %"]), reverse=True)
    return filtered
