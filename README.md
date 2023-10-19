## VCS Contributions Importer Tool

### Overview

This tool facilitates the migration or mirroring of commits between different version control systems (VCSs). It's especially useful for mirroring contribution charts and histories across platforms such as GitLab and GitHub. The tool comprises three Python scripts:

- `gitlab_page_scraper.py`
- `gitlab_data_parser.py`
- `contributions_register.py`

These scripts collaborate to scrape and generate user contribution information from the `https://gitlab.com/users/user_name/activity` Gitlab page, subsequently creating corresponding commits on GitHub.

### Features

- Provides updates on the terminal about the script's progress, showing the date of the most recent contribution scanned.
- Parses a local HTML file containing GitLab contribution data.
- Generates a `.patch` file (`gitlab_contributions.patch`) using parsed data.
- Extracts data from the `.patch` file to create commits with corresponding contribution type messages and dates.
- Optionally pushes these commits to a target GitHub repository.
- Ensures that contributions made on GitLab are refected on GitHub's contribution chart.

### Requirements

#### System Requirements

1. **Python**: Must have Python (3.x or above) installed. [Download Python](https://www.python.org/downloads/).
2. **Git**: Git should be installed and configured correctly. [Install Git](https://git-scm.com/downloads).

#### Python Libraries

Install the following Python libraries to run the scripts:

1. **Selenium**: Used for web scraping.

   ```bash
   pip install selenium
   ```

2. **BeautifulSoup4**: Essential for parsing HTML content.
   ```bash
   pip install beautifulsoup4
   ```

#### Additional Tools

- **Selenium WebDriver**: The `gitlab_page_scraper.py` script needs the Selenium WebDrive.

- **Git Configuration**: Before using the `contributions_register.py` script, verify your local git configuration and GitHub repository initialization.

#### Optional

- **Virtual Environment**: It's recommended to operate Python scripts in a virtual environment to prevent version clashes and maintain system Python integrity. Consider tools like `virtualenv` or the native `venv` module.

  Create a virtual environment:

  ```bash
  python -m venv myenv
  ```

  Activation:

  - Windows:

    ```bash
    .\myenv\Scripts\activate
    ```

  - macOS and Linux:
    ```bash
    source myenv/bin/activate
    ```

  With the environment activated, install the necessary libraries.

### Usage

1. **Scrape GitLab Activity Page**:

   - Ensure Python and Selenium WebDriver are installed.
   - Store the `gitlab_page_scraper.py` script in your project directory.
   - Execute the script:
     ```bash
     python gitlab_page_scraper.py
     ```

   It will save an HTML file of your GitLab contribution data locally..

2. **Run the Contributions Register Script**:

   - Store the `gitlab_data_parser.py` script in your project directory.
   - Execute the script:
     ```bash
     python gitlab_data_parser.py
     ```
   - This generates a `gitlab_contributions.patch` file based on your GitLab contribution data.

3. **Run the Contributions Register Script**:

   - Save the `contributions_register.py` script in root folder of your project directory the produced `.patch` file.
   - Execute the script:
     ```python
     python contributions_register.py
     ```

   This script processes the `gitlab_contributions.patch` file, creates commits from the parsed data, and optionally sends these commits to your GitHub repository. It also creates a `contributions.txt` file summarizing all commits prepared for push. Review this in your repo before executing `git push`.

4. **View Your Contributions**:

   After finalizing and pushing the changes, inspect your GitHub repository's contribution chart to observe the transferred contributions from GitLab 😎.

### Note

Before executing the `contributions_register.py` script, double-check your local git configuration and ensure your GitHub repository has been initialized properly.
