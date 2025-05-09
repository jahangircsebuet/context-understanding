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


class PostFromFoxNews(object):
    def __init__(self, browser, depth):
        self.browser = browser
        self.depth = int(depth)
        self.data = []

    def scroll_web_page(self):
        for scroll in range(self.depth):
            try:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                print("scrol ", scroll)
                self.delay = random.randrange(1, 5)
                time.sleep(self.delay)
            except Exception as e:
                return False
                continue
        return True

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

    def find_post_text(self, post):
        # print(post)
        # text = post.find_element_by_class_name("userContent").text
        # post = post.find_element_by_xpath("//div[@data-ad-preview='message']")
        # print("text: ", post.text)
        return post.text

    def fetch_posts(self):
        texts = []
        # posts = self.browser.find_elements_by_xpath("//div[@role='article']")
        # print("posts.len: ", len(posts))

        posts = self.browser.find_elements_by_xpath("//div[@data-ad-preview='message']")
        if len(posts) == 0:
            return []

        for count, post in enumerate(posts):
            try:
                # post = post.find_element_by_xpath("//div[@data-ad-preview='message']")
                # print("post: ", post)
                # links = post.find_element_by_xpath("//a[@role='link']")
                # print("links.len: ", len(links))
                # for link in links:
                #     print("link: ", link)
                text = self.find_post_text(post)
                texts.append(text)
            except Exception as e:
                print(e)
                continue
        return texts

    def collect_posts_blog(self, url):
        self.browser.get(url)
        # posts = self.browser.find_element_by_xpath("//ul[@class='spcv_messages-list']")
        self.scroll_web_page()
        posts = []
        try:

            # // *[ @ data - spot - im - module - default - area = 'conversation']
            conversations = self.browser.find_elements_by_xpath(xpath="//div[@data-spot-im-module-default-area='conversation']")
            if len(conversations) > 0:
                conversation_div = conversations[0]
                # show_more = conversation_div.find_elements_by_xpath(
                #     "//div[contains(@class, 'spcv_loadMoreCommentsContainer')]")
                lis = conversation_div.find_elements_by_xpath("//li[@class='spcv_list-item']")
                print(len(lis))
                # show_more = conversation_div.find_elements_by_xpath("//div[@class = 'spcv_loadMoreCommentsContainer']")
                # print("show_more")
                # print(show_more)
        except Exception as e:
            print(e)

        return posts

    def collect_posts(self, depth, url, filename, gender, loginRequired, email, password):
        if loginRequired:
            login_fb = Login(self.browser)
            login_fb.login(email, password)
            print("Login is done")

        posts = []
        self.browser.get(url)

        # close the pop up
        if not loginRequired:
            time.sleep(5)
            btn = self.browser.find_element_by_xpath("//div[@tabindex=0 and @role='button' and @aria-label='Close']")
            btn.click()
        exceptioned = False
        for i in range(depth):
            print("depth: ", i)
            # scroll down
            if not exceptioned:
                self.scroll_web_page()
                time.sleep(10)

                posts.extend(self.fetch_posts())
                print("posts.len: ", len(posts))
                time.sleep(10)

        if len(posts) > 0:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                fields = ["status", "author"]

                writer.writerow(fields)
                for post in posts:
                    writer.writerow([str(post), gender])
        return posts


browser = Browser(0).getBrowser()
scraper = PostFromFoxNews(browser=browser, depth=5)


posts = scraper.collect_posts_blog("https://www.foxnews.com/politics/bidens-billion-dollar-plan-build-500000-ev-chargers-has-yet-yield-single-charger")
print(len(posts))

# posts = scraper.collect_posts(50,
#                               "https://www.facebook.com/profile.php?id=100017579682426",
#                               "dilruba.afroze.csv",
#                               "F",
#                               True,
#                               'EMAIL',
#                               'PASSWORD')
# print(len(posts))

# f = open("masumbillah.csv", "r")
# print(f.read())
