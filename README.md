# VCS Contributions Importer Tool

## Overview

This tool facilitates the migration or mirroring of commits between different repositories or version control systems (VCSs), making it useful for mirroring contribution charts and commit histories across multiple VCS platforms, such as GitLab and GitHub. The tool comprises two Python scripts (`gitlab_data_parser.py` and `contributions_register.py`) that work together to generate and utilize a `.patch` file from GitLab data, creating corresponding commits on GitHub.

## Features

- Parses a local HTML file containing GitLab contribution data.
- Generates a `.patch` file (`gitlab_contributions.patch`) based on the extracted contribution data.
- Extracts data from the `.patch` file and creates commits with corresponding messages and dates.
- Optionally pushes these commits to a target GitHub repository.
- Helps ensure that contributions made on GitLab are accurately reflected on GitHub's contribution chart.

## Usage

1. **Prepare the HTML File:**

   Save an HTML file containing your GitLab contribution data locally.

2. **Run the GitLab Data Parser Script:**

   - Ensure you have Python installed on your machine.
   - Save the script `gitlab_data_parser.py` in your project directory.
   - Run the script by entering the following command:

   ```shell
   python gitlab_data_parser.py
   ```

   This will generate a `gitlab_contributions.patch` file based on your GitLab contribution data.

3. **Run the Contributions Register Script:**

   - Save the script `contributions_register.py` in your project directory alongside the generated `.patch` file.
   - Run the script by entering the following command:

   ```shell
   python contributions_register.py
   ```

   This script will read the `gitlab_contributions.patch` file, create commits based on the extracted data, and optionally push these commits to your GitHub repository.

4. **View Your Contributions:**

   Check your GitHub repository's contribution chart to see the migrated contributions from GitLab.

## Note

Make sure that your local git configuration is correctly set up, and your GitHub repository is properly initialized before running the `contributions_register.py` script.
