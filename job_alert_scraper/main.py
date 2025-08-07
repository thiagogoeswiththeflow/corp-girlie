from notion_api import push_to_notion

def main():
    dummy_jobs = [{
        "title": "Customer Success Manager (Test)",
        "company": "OpenAI",
        "location": "Remote",
        "remote": "Yes",
        "platform": "Manual Test",
        "url": "https://example.com",
        "date_posted": "2025-08-07"
    }]
    
    print("DEBUG: Calling push_to_notion with dummy job...")
    push_to_notion(dummy_jobs)

if __name__ == "__main__":
    main()
