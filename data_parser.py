from datetime import datetime
from bs4 import BeautifulSoup

def extract_data_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    event_items = soup.find_all('li', class_='event-item gl-border-b-0 gl-pb-3 gl-list-none user-profile-activity !gl-pl-7')
    
    extracted_data = []
    
    for item in event_items:
        time_element = item.find('div', class_='event-item-timestamp gl-text-sm').find('time', class_='js-timeago')
        date_str = time_element['datetime'].replace('T', ' ').replace('Z', '')
        
        # Extracting the contribution type
        event_title_div = item.find('div', class_='system-note-image pushed-to-icon gl-rounded-full gl-bg-strong gl-leading-0')
        if event_title_div is not None:
            icon_element = event_title_div.find('svg', class_='s14', attrs={"data-testid": True})
            icon_type = icon_element['data-testid'] if icon_element else "unknown-icon"
        else:
            icon_type = "unknown-icon"
        
        extracted_data.append((date_str, icon_type))
        
    return extracted_data

def generate_patch(data):
    patch_content = ""
    for date_str, icon_type in data:
        patch_entry = f"""From 1234567 {date_str}
From: User <test@example.com>
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
    # Read content from scraped data
    with open('gitlab_data.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    data = extract_data_from_html(html_content)
    patch = generate_patch(data)
    
    with open('gitlab_contributions.patch', 'w') as f:
        f.write(patch)
