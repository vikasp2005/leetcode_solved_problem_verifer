from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup




def findcount(url,driver):
    value=None
    try:
        # Navigate to LeetCode
        driver.get(url)

        time.sleep(5)

        # Wait for the complete page load using JavaScript
        WebDriverWait(driver, 20).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

        # Take a screenshot after the page is fully loaded
        screenshot_path = "leetcode_screenshot.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        # Get the page's HTML content
        html_content = driver.page_source

    

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'lxml')

        # Find the element with the specified class attributes
        element = soup.find('span', class_='text-[30px] font-semibold leading-[32px]')

        # Extract the value from the element
        if element:
            value = element.text.strip()
            print(f"Extracted value: {value}")
            return value
        else:
            print("Element not found")
            return None
    finally:
        return value
