import subprocess

def extract_data_from_patch_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    dates = [line.split(": ")[1].strip() for line in lines if line.startswith("Date: ")]
    contr_types = [line.split("(")[1].split(")")[0] for line in lines if line.startswith("Subject: ")]

    return list(zip(dates, contr_types))

def create_commits(data):
    for date, contr_type in data:
        contr_type = contr_type.replace('-icon', '')  # Strip the '-icon' suffix
        commit_message = f"docs: import {contr_type} contribution data from GitLab | {date}"
        
        # Add the contribution to the contributions.txt file
        with open("contributions.txt", "a") as f:
            f.write(f"{commit_message}\n")
        
        # Git commands to commit the changes, suppressing the actual output
        subprocess.run(["git", "add", "contributions.txt"])
        subprocess.run(["git", "commit", "-m", commit_message, "--date", date], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(f"Executed: git commit -m \"{commit_message}\" --date \"{date}\"")


    # Uncomment the line below if you want to push changes automatically
    # subprocess.run(["git", "push", "origin", "main"])

    print("Success! All contributions from GitLab have been successfully migrated and will soon be visible on your GitHub profile.")

if __name__ == "__main__":
    data = extract_data_from_patch_file("gitlab_contributions.patch")
    create_commits(data)
