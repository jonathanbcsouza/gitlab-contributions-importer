import time
from datetime import datetime
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome(options=chrome_options)

def check_user_exists(gitlab_username):
    response = requests.head(f'https://gitlab.com/users/{gitlab_username}/activity')
    return response.status_code == 200

def get_username():
    while True:
        gitlab_username = input("Please enter your GitLab username: ")
        if check_user_exists(gitlab_username):
            return gitlab_username
        else:
            print("User does not exist, try again.")

def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Extract the date from the latest timestamp before scrolling
        timestamp_elements = driver.find_elements(By.CSS_SELECTOR, '.js-timeago')
        if timestamp_elements:
            latest_timestamp = timestamp_elements[-1].get_attribute('datetime')
            date_obj = datetime.strptime(latest_timestamp, '%Y-%m-%dT%H:%M:%SZ')
            formatted_date = date_obj.strftime('%d/%m/%Y')
            print(f'Scanning contributions made before {formatted_date}...')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            wait = WebDriverWait(driver, 10)
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "any_css_selector")))
            except TimeoutException:
                print('Timeout reached, assuming all content is loaded.')
                break  # Assume all content has loaded
            print('No more new content, exiting...')
            break  # Or break here if the above exception handling isn't needed
        last_height = new_height

def save_html(page_source, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(page_source)
    print(f'HTML data saved to {file_path}')

def main():
    gitlab_username = get_username()  # Get a valid GitLab username from the user
    driver = setup_driver()
    driver.get(f'https://gitlab.com/users/{gitlab_username}/activity')
    
    start_time = time.time()
    scroll_to_bottom(driver)
    end_time = time.time()
    
    print(f'Scrolling completed in {end_time - start_time:.2f} seconds')
    
    page_source = driver.page_source
    driver.quit()
    
    file_path = 'gitlab_data.html'
    save_html(page_source, file_path)

if __name__ == "__main__":
    main()
