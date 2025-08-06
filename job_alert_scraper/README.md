# Job Alert Scraper

This script scrapes job listings from selected platforms, filters them based on your profile, and sends results directly into a Notion database.

## 🔧 Setup Instructions

### 1. Install Python dependencies
```
pip install -r requirements.txt
```

### 2. Update Notion API token and database ID
Edit `notion_api.py` and replace:
- `NOTION_TOKEN` with your internal integration token
- `DATABASE_ID` with the ID of your Notion database

These are already pre-filled for you.

### 3. Run the script
```
python main.py
```

The script will:
- Scrape test jobs from Remote OK and Built In
- Filter based on your job criteria
- Push jobs (with match % and CV tweak suggestions) into your Notion database

---

## 📌 Coming Next
- LinkedIn, Glassdoor, Indeed, Welcome to the Jungle scrapers
- Automation (daily run with GitHub Actions or cron)

For now, this is a local MVP setup. Full automation will follow once validated.
