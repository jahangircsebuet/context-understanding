import time
import random
from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scroll_web_page(self):
    for scroll in range(self.depth):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("scroll ", scroll)
        self.delay = random.randrange(1, 5)
        time.sleep(self.delay)

        # Use WebDriverWait to wait for the presence of each element
        try:
            elements = WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-ad-preview='message']"))
            )

            for element in elements:
                # Click on "See more" button if present
                try:
                    see_more_button = element.find_element(By.XPATH, "//div[text() ='See more' and role='button' and tabindex='0']")
                    see_more_button.click()
                    print("Clicked on 'See more' button")
                except Exception as see_more_exception:
                    # Handle exception or log an error message
                    print(f"Error clicking 'See more' button: {see_more_exception}")

                # Get text in the div with data-ad-preview='message'
                ad_message_text = element.text
                print(ad_message_text)
                print(f"Text in the div with data-ad-preview='message': {ad_message_text}")
        except Exception as e:
            # Handle the exception or log an error message
            print(f"Error: {e}")

        # Add additional delay if needed
        time.sleep(self.delay)


for i in range(5):
    print("iteration")
    scroll_web_page()