import time
import subprocess
import sys

set_default_prompt_color = "\033[0m"
set_green_color = "\033[32m"
set_red_color = "\033[31m"

def scrape_gitlab_activity_page():
    print("Scraping GitLab Activity Page...")
    subprocess.run([python_executable, "contributions_page_scraper.py"])
    print(f"{set_green_color}Scraping completed.{set_default_prompt_color}\n")

def run_data_parser():
    print("Running Data Parser...")
    subprocess.run([python_executable, "data_parser.py"])
    print(f"{set_green_color}Data parsing completed.{set_default_prompt_color}\n")

def run_contributions_register():
    print("Running Contributions Register...")
    subprocess.run([python_executable, "contributions_register.py"])
    print(f"{set_green_color}Contributions registration completed.{set_default_prompt_color}\n")  # Added "\n" for a line break
    

if __name__ == "__main__":
    try:
        # Use the which command to find the path to Python executable
        python_executable = subprocess.check_output(["which", "python3"]).decode().strip()
    except subprocess.CalledProcessError:
        print(f"{set_red_color}Error: Python3 not found.{set_default_prompt_color}\n")
        sys.exit(1)

    scrape_gitlab_activity_page()
    run_data_parser()
    run_contributions_register()
