import subprocess

def scrape_gitlab_activity_page():
    print("Scraping GitLab Activity Page...")
    subprocess.run(["python", "contributions_page_scraper.py"])
    print("Scraping completed.")

def run_data_parser():
    print("Running Data Parser...")
    subprocess.run(["python", "data_parser.py"])
    print("Data parsing completed.")

def run_contributions_register():
    print("Running Contributions Register...")
    subprocess.run(["python", "contributions_register.py"])
    print("Contributions registration completed.")

def main():
    scrape_gitlab_activity_page()
    run_data_parser()
    run_contributions_register()

if __name__ == "__main__":
    main()
