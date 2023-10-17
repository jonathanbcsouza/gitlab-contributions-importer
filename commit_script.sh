#!/bin/bash

if [ ! -f contributions.txt ]; then
    touch contributions.txt
fi

# Extract dates and times from lines starting with "Date: " in github_contributions.patch
dates=($(grep '^Date: ' gitlab_contributions.patch | cut -d' ' -f2))
times=($(grep '^Date: ' gitlab_contributions.patch | cut -d' ' -f3))
commit_message="Migrate contributions"
source="Gitlab"
origin="GitHub"

combined_dates=()
for i in "${!dates[@]}"; do
    combined_dates+=("${dates[$i]} ${times[$i]}")
done

for line in "${combined_dates[@]}"; do

  # Add the contribution to the contributions.txt file
  echo "$commit_message from $source | $line" >> contributions.txt

  git add contributions.txt
  git commit -m "task: migrate contributions from $source on $line" --date="$line"

  echo "Executed: git commit -m \"$commit_message from $source | $line\" --date=\"$line\""

done

git push origin main

echo "Success! All contributions from $source have been successfully migrated and will soon be visible on your $origin profile."
