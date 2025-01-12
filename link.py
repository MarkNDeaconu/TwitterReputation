from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time  # Import time for adding delay

def receive_link(tweet_id):
    link = 'https://x.com/user/status/' + tweet_id

    def get_redirected_url_js(original_url):
        # Configure Selenium with Chrome driver
        options = Options()
        options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--disable-gpu')
        
        # Replace the path with the location of your ChromeDriver
        service = Service("C:/Users/Mark/Downloads/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)
        
        try:
            driver.get(original_url)
            time.sleep(0.8)  # Wait for 5 seconds before retrieving the current URL
            new_url = driver.current_url  # Get the current URL after the redirect
            return new_url
        except Exception as e:
            return f"Error: {e}"
        finally:
            driver.quit()

    # Example usage
    new_url = get_redirected_url_js(link)
    print(f"Redirected URL: {new_url}")

