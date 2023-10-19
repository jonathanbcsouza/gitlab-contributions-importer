## GitLab Contributions Importer

### Overview

This fun experiment facilitates the migration or mirroring of contributions between GitLab and another VCS platform. While GitLab likely offers an API for more efficient management, this tool explores web scraping and data parsing techniques as an alternative approach. It's designed to mirror publicly visible contributions and histories from GitLab into another platform using three different stages:

| Task                                     | Script                          |
| :--------------------------------------- | :------------------------------ |
| Collect GitLab data and create HTML file | `contributions_page_scraper.py` |
| Extract patch data from HTML             | `data_parser.py`                |
| Generate commits from patch file         | `contributions_register.py`     |

These scripts scrape user contribution information from the `https://gitlab.com/users/user_name/activity` and generate commit messages with corresponding contributions and timestamps.

### Features

- Allows selection of a GitLab username to download data from.
- Provides progress updates during the scraping process.
- Generates an HTML file locally containing GitLab user's contribution data.
- Parses the data and creates a `.patch` file (`gitlab_contributions.patch`).
- Uses the `.patch` file to create commits.
- Aims to ensure that GitLab contributions are mirrored on the target platform's contribution chart.

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

1. **View Your Contributions**:
   Create a new repository in your desired plataform. E.g, GitHub.
2. **Clone Your New Repository**:
   After creating your repository, clone it to your local machine using the following command:

```bash
git clone [URL-of-your-repository]

```

3. **Copy the Content**:
   Copy the contents of the GitLab Contributions Importer repository into the folder of your newly cloned repository.

4. **Run the Importer**:

The `main.py` script is designed as a driver script that internally calls the other mentioned scripts in sequence. It streamlines the process, allowing users to run a single command to achieve the desired outcome. Specifically:

1. It first uses contributions_page_scraper.py to scrape GitLab data and create an HTML file.
1. Then, data_parser.py takes over to extract patch data from the HTML.
1. Finally, contributions_register.py generates the commits from the patch file

Simply run:

```bash
python main.py
```

The `main.py` script acts as a driver, calling the other scripts in sequence. This streamlines the process, allowing users to run a single command for the desired result:

1. First, contributions_page_scraper.py scrapes GitLab data, producing an HTML file.
2. Next, data_parser.py extracts patch data from the HTML.
3. Finally, contributions_register.py generates commits from the patch file.

To execute:

```python
python main.py
```

5. **View Your Contributions**:

Push the changes and examine your GitHub repository's contribution chart to see the mirrored contributions from GitLab 😎.

### Note

Before running the `main.py` script, ensure your local git configuration is set correctly and that your GitHub repository has been properly initialized.
