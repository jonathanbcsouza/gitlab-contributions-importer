### VCS Contributions Migrator Tool

#### Overview

The is a shell script designed to facilitate the migration or mirroring of commits between different repositories or version control systems (VCSs). This tool is useful for mirroring contribution charts and commit histories across multiple VCS platforms, such as GitLab and GitHub.

#### Features

- Scans a `.patch` file containing commit metadata from GitLab.
- Creates commits based on the commit dates from the patch file.
- Pushes these commits to a target GitHub repository.
- Helps ensure that contributions made on GitLab are accurately reflected on GitHub's contribution chart.

#### Usage

To use this tool, follow these simple steps:

1. **Download the Script:**

   Download the `vcs_contributions_migrator.sh` script file from this repository.

2. **Save it in Your Repository:**

   Save the downloaded script within the root folder of the repository.

3. **Make the Script Executable:**

   Ensure that the script is executable by running:

   ```shell
   chmod +x vcs_contributions_migrator.sh
   ```

   This step allows you to run the script.

4. **Execute the Script:**

   Run the script by entering the following command:

   ```shell
   ./vcs_contributions_migrator.sh
   ```
