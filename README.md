## GitLab Contributions Importer

### Overview

Want to showcase your GitLab contributions on GitHub? 👀

This tool is a fun experiment that enables you to reflect your contribution history based on public GitLab data. While GitLab might have an API offering similar functionalities, this project utilizes web scraping and data parsing techniques as a alternative approach. It's designed to mirror these contributions to another VCS platform through a three-stage process:

| Task                                                 | Script                          |
| :--------------------------------------------------- | :------------------------------ |
| Extracts GitLab data and create HTML file            | `contributions_page_scraper.py` |
| Create a patch file based on the HTML data           | `data_parser.py`                |
| Generate commits using metadata from the patch file. | `contributions_register.py`     |

These scripts scrape user contribution information from the `https://gitlab.com/users/user_name/activity` and generate commit messages with corresponding contributions and timestamps.

### Features

- Allows selection of a GitLab username to download data from.
- Provides progress updates during the execution.
- Generates an HTML file locally containing GitLab user's contribution data.
- Parses the data and creates a `.patch` file (`gitlab_contributions.patch`).
- Uses the created `.patch` file to generate commits.
- Aims to ensure that GitLab contributions are mirrored on the target platform's contribution chart.

### Requirements

##### System Requirements

Python (3.x or above). [Download Python](https://www.python.org/downloads/).

##### Python Libraries

1. **Selenium**: Used for web scraping.

   ```bash
   pip install selenium
   ```

2. **BeautifulSoup4**: For HTML content parsing.
   ```bash
   pip install beautifulsoup4
   ```

##### Additional Tools

- **Selenium WebDriver**: `contributions_page_scraper.py` relies on this.

##### Optional

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
   After creating your repository, clone it to your local machine:

```bash
git clone [URL-of-your-repository]

```

3. **Copy the Content**:
   Copy the content of this project into the root folder of your cloned repository.

4. **Run the Importer**:

The `main.py` script acts as a driver, calling the other scripts in sequence. This streamlines the process, allowing users to run a single command for the desired result:

1. First, `contributions_page_scraper.py` scrapes GitLab data, producing an HTML file.
2. Next, `data_parser.py` scans the data from the HTML and generate a patch file.
3. Finally, `contributions_register.py` creates commits using the metadata from the patch file.

To execute:

```python
python main.py
```

5. **View Your Contributions**:

Push the changes and examine your platform repository's contribution chart to see the mirrored contributions from GitLab 😎.

### Note

Before running the `main.py` script, ensure your local git configuration is set correctly and that your GitHub repository has been properly initialized.
