import re
import time
import random
from browser import Browser
# from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from crawler.login import Login
import csv
from selenium.webdriver.common.action_chains import ActionChains


class PostFromPublicPage(object):
    def __init__(self, browser, depth):
        self.browser = browser
        self.depth = int(depth)
        self.data = []

    def find_post_text(self, post):
        return post.text

    def click_see_more(self, post):
        try:
            # Scroll into view of the parent element
            actions = ActionChains(self.browser)
            actions.move_to_element(post).perform()

            # Find the "See more" button by its text content
            see_more_button = post.find_element(By.XPATH, ".//div[text()='See more']")
            see_more_button.click()
        except Exception as e:
            print(f"Error clicking See more: {e}")

    def fetch_posts(self):
        texts = []
        posts = self.browser.find_elements_by_xpath("//div[@data-ad-preview='message']")

        for count, post in enumerate(posts):
            try:

                # Click "See more" for each post
                self.click_see_more(post)

                # Wait for the content to load after clicking "See more"
                WebDriverWait(self.browser, 10).until(
                    EC.invisibility_of_element_located((By.XPATH, ".//div[text()='See more']"))
                )

                text = self.find_post_text(post)
                texts.append(text)

            except Exception as e:
                print(e)
                continue

        return texts

    def scroll_web_page(self):
        for scroll in range(self.depth):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("scroll ", scroll)
            self.delay = random.randrange(1, 5)
            time.sleep(self.delay)

            # Use WebDriverWait to wait until the element is present
            try:
                elements = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-ad-preview='message']"))
                )
            except Exception as e:
                # Handle the exception or log an error message
                print(f"Error: {e}")

            # Add additional delay if needed
            time.sleep(self.delay)

    def scroll_web_page_old(self):
        for scroll in range(self.depth):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("scrol ", scroll)
            self.delay = random.randrange(1, 5)
            time.sleep(self.delay)

    def find_actual_post(self, post):
        flag = False
        try:
            link = post.find_element_by_xpath(".//span[@class='text_exposed_link']//a")
            link.click()
            if (len(self.browser.window_handles) == 2):
                self.browser.switch_to.window(window_name=self.browser.window_handles[-1])
                flag = True
                element = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "userContentWrapper")))
                post = self.browser.find_element_by_class_name("userContentWrapper")
        except Exception as e:
            pass

        return post, flag

    # def find_post_text(self, post):
    #     # print(post)
    #     # text = post.find_element_by_class_name("userContent").text
    #     # post = post.find_element_by_xpath("//div[@data-ad-preview='message']")
    #     # print("text: ", post.text)
    #     return post.text
    #
    # def fetch_posts(self):
    #     texts = []
    #     # posts = self.browser.find_elements_by_xpath("//div[@role='article']")
    #     # print("posts.len: ", len(posts))
    #     posts = self.browser.find_elements_by_xpath("//div[@data-ad-preview='message']")
    #
    #     for count, post in enumerate(posts):
    #         try:
    #             text = self.find_post_text(post)
    #             texts.append(text)
    #         except Exception as e:
    #             print(e)
    #             continue
    #     return texts

    def collect_posts(self, depth, url, filename, gender):
        posts = []
        self.browser.get(url)

        # close the pop up
        time.sleep(5)
        btn = self.browser.find_element_by_xpath("//div[@tabindex=0 and @role='button' and @aria-label='Close']")
        btn.click()

        for i in range(5):
            print("iteration: ", i)
            self.scroll_web_page()

        # for i in range(depth):
        #     print("depth: ", i)
        #     # scroll down
        #     self.scroll_web_page()
        #     time.sleep(10)
        #
        # posts.extend(self.fetch_posts())
        # print("posts.len: ", len(posts))
        # time.sleep(10)

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            fields = ["status", "author"]

            writer.writerow(fields)
            for post in posts:
                writer.writerow([str(post), gender])
        return posts


browser = Browser(0).getBrowser()
scraper = PostFromPublicPage(browser=browser, depth=5)

# https://www.facebook.com/arifkhandake
# posts = scraper.collect_posts(50, "https://www.facebook.com/arifkhandake", "arifkhandake.csv", "M")

# https://www.facebook.com/chamok.hasan/ - done
# posts = scraper.collect_posts(50, "https://www.facebook.com/chamok.hasan/", "chamok.hasan.csv", "M")

# https://www.facebook.com/shuruve.islam -done
# posts = scraper.collect_posts(20, "https://www.facebook.com/shuruve.islam/", "shuruve.islam.csv", "F")

# https://www.facebook.com/ragibhasan
# posts = scraper.collect_posts(50, "https://www.facebook.com/ragibhasan/", "ragibhasan.csv", "M")

# https://www.facebook.com/mamun3.14 - done
# posts = scraper.collect_posts(50, "https://www.facebook.com/mamun3.14/", "mamun3.14.csv", "M")

# https://www.facebook.com/aamunir.hasan
# posts = scraper.collect_posts(50, "https://www.facebook.com/aamunir.hasan/", "aamunir.hasan.csv", "M")

# https://www.facebook.com/DrNiazChowdhury

# https://www.facebook.com/superman.com.bd
# posts = scraper.collect_posts(50, "https://www.facebook.com/superman.com.bd/", "superman.com.bd.csv", "M")

# https://facebook.com/sohani.akter.9 - done
posts = scraper.collect_posts(5, "https://facebook.com/sohani.akter.9/", "test.csv", "F")

# https://www.facebook.com/people/Sayed-Sajib/100083328978432/
# posts = scraper.collect_posts(10, "https://www.facebook.com/people/Sayed-Sajib/100083328978432/", "Sayed-Sajib.csv", "M")

print("total posts.len: ", len(posts))

