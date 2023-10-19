## VCS Contributions Importer Tool

### Overview

This fun experiment facilitates the migration or mirroring of commits between version control systems (VCSs). While GitLab likely offers an API to manage these tasks more efficiently, this tool provides an alternative approach by exploring web scraping and data parsing techniques. It's designed to mirror publicly visible contributions and histories on GitLab over to GihHUb through three Python scripts:

- `contributions_page_scraper.py`
- `data_parser.py`
- `contributions_register.py`

These scripts work together to scrape user contribution information from the `https://gitlab.com/users/user_name/activity` Gitlab page and create corresponding commits on GitHub.

### Features

- Provides updates about script progression, showcasing the date of the last contribution scanned.
- Parses a local HTML file that contains GitLab contribution data.
- Generates a `.patch` file (`gitlab_contributions.patch`) from parsed data.
- Uses the `.patch` file to generate commits with cooresponding contribution messages and timestamps.
- Aims to ensure that GitLab contributions mirror those on GitHub's contribution chart.

### Requirements

#### System Requirements

1. **Python**: Python (3.x or above) is essential. [Download Python](https://www.python.org/downloads/).
2. **Git**: Ensure Git is installed and appropriately configured. [Install Git](https://git-scm.com/downloads).

#### Python Libraries

The following Python libraries are required:

1. **Selenium**: Used for web scraping.

   ```bash
   pip install selenium
   ```

2. **BeautifulSoup4**: For HTML content parsing.
   ```bash
   pip install beautifulsoup4
   ```

#### Additional Tools

- **Selenium WebDriver**: `contributions_page_scraper.py` relies on this.
- **Git Configuration**: Ensure you've configured git locally and initialized your GitHub repository before using `contributions_register.py`.

#### Optional

- **Virtual Environment**: It's always a good practice to run Python scripts in a virtual environment to avoid version conflicts and keep your system Python clean. You can use tools like `virtualenv` or the built-in `venv` module.

  Set up a virtual environment:

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

  Once activated, install the necessary libraries within this virtual environment.

### Usage

1. **Scrape GitLab Activity Page**:

   - Ensure Python and Selenium WebDriver are installed.
   - Copy and paste `contributions_page_scraper.py` in your project directory.
   - Run the script:
     ```bash
     python contributions_page_scraper.py
     ```

   This saves a local HTML file with your GitLab contribution data.

2. **Run the Contributions Register Script**:

   - Copy and paste `data_parser.py` in your project directory.
   - Run the script:
     ```bash
     python data_parser.py
     ```

   This produces a `gitlab_contributions.patch` file based on your GitLab contribution data.

3. **Run the Contributions Register Script**:

   - Copy and paste `contributions_register.py` is your project directory.
   - Run the script:
     ```python
     python contributions_register.py
     ```

   This script processes the `gitlab_contributions.patch` file, creates commits from the data, and optionally pushes these commits to your GitHub repository. It also generates a `contributions.txt` file summarizing all commits set for push. Review this file in your repo before performing a `git push`.

4. **View Your Contributions**:

   After pushing the changes, inspect your GitHub repository's contribution chart to see the contributions inserted from GitLab 😎.

### Note

Before running the `contributions_register.py` script, ensure your local git configuration is set correctly and that your GitHub repository has been properly initialized.
