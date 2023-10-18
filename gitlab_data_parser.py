from datetime import datetime
from bs4 import BeautifulSoup

def extract_data_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    event_items = soup.find_all('div', class_='event-item')
    
    extracted_data = []
    
    for item in event_items:
        # Extracting the date
        time_element = item.find('time', class_='js-timeago')
        date_str = ' '.join(time_element['title'].split()[:4])  # Extracting: "Sep 28, 2023 11:55pm"
        
        # Convert date to the desired format
        date_obj = datetime.strptime(date_str, '%b %d, %Y %I:%M%p')
        formatted_date = date_obj.strftime('%Y-%m-%d %H:%M:%S')
        
        # Extracting the contribution type
        event_title_div = item.find('div', class_='event-title d-flex flex-wrap')
        icon_element = event_title_div.find('svg', class_='s14', attrs={"data-testid": True})
        icon_type = icon_element['data-testid'] if icon_element else "unknown-icon"
        
        extracted_data.append((formatted_date, icon_type))
        
    return extracted_data

def generate_patch(data):
    patch_content = ""
    for date_str, icon_type in data:
        patch_entry = f"""From 1234567 {date_str}
From: User <user@example.com>
Date: {date_str}
Subject: [PATCH] Contribution on {date_str} ({icon_type})

---
 contributions.txt | 1 +
 1 file changed, 1 insertion(+)

diff --git a/contributions.txt b/contributions.txt
index 1234567..1234567 100644
--- a/contributions.txt
+++ b/contributions.txt
@@ -1,0 +2 @@
+Contribution on {date_str} ({icon_type})

"""
        patch_content += patch_entry
        
    return patch_content

if __name__ == "__main__":
    # For simplicity, read the HTML content from a local file
    with open('mock_gitlab_data.html', 'r') as f:
        html_content = f.read()
        
    data = extract_data_from_html(html_content)
    patch = generate_patch(data)
    
    with open('gitlab_contributions.patch', 'w') as f:
        f.write(patch)
