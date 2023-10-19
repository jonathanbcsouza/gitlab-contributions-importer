import subprocess
import sys

default_color = "\033[0m"
green_color = "\033[32m"
red_color = "\033[31m"

tasks_and_files = [
    ('"Collect GitLab Data and Create HTML File"', 'contributions_page_scraper.py'),
    ('"Extract Patch Data from HTML"', 'data_parser.py'),
    ('"Generate Contribution from Patch File"', 'contributions_register.py'),
]

def execute_task(task, file_name):
    print(f"Executing {file_name}...")
    subprocess.run([python_executable, file_name])
    print(f"{green_color}{task} task completed.{default_color}\n")    

if __name__ == "__main__":
    try:
        # Use the which command to find the path to Python executable
        python_executable = subprocess.check_output(["which", "python3"]).decode().strip()
    except subprocess.CalledProcessError:
        print(f"{red_color}Error: Python3 not found.{default_color}\n")
        sys.exit(1)

    for task, file_name in tasks_and_files:
        execute_task(task, file_name)
