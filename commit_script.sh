#!/bin/bash

if [ ! -f contributions.txt ]; then
    touch contributions.txt
fi

# Extract dates and times from lines starting with "Date: " in github_contributions.patch
file_name="gitlab_contributions.patch"

dates=($(grep '^Date: ' $file_name | cut -d' ' -f2))
times=($(grep '^Date: ' $file_name | cut -d' ' -f3))
contr_type=($(grep '^Subject: ' $file_name | awk -F'(' '{print $2}' | cut -d')' -f1))
source="GitLab"
origin="GitHub"

combined_dates=()
for i in "${!dates[@]}"; do
    combined_dates+=("${dates[$i]} ${times[$i]}")
done                              

for i in "${!combined_dates[@]}"; do
  line="${combined_dates[$i]}"
  commit_type="${contr_type[$i]}"
  commit_message="docs: import $commit_type contribution data from $source"

  # Add the contribution to the contributions.txt file
  echo "$commit_message | $line" >> contributions.txt

  # git add contributions.txt
  # git commit -m "$line" --date="$line"

  echo "Executed: git commit -m \"$commit_message | $line\" --date=\"$line\""

done

# git push origin main

echo "Success! All contributions from $source have been successfully migrated and will soon be visible on your $origin profile."
