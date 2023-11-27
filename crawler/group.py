import re
import time
import random
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Group(object):
    def __init__(self, browser, depth):
        self.browser = browser
        self.depth = int(depth)
        self.data = []

    # Scroll down depth-times and wait delay seconds to load between scrolls


    def scroll_web_apge(self):
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

    def find_post_author(self, post):
        author_name = post.find_element_by_xpath(".//a[@data-hovercard-referer]").text
        return author_name

    def find_fb_profile(self, post):
        facebook_profile_link = post.find_element_by_xpath(".//a[@data-hovercard-referer]").get_attribute("href")
        if  "profile.php" in facebook_profile_link:
            facebook_profile_link = re.sub(r'\&.*', '', facebook_profile_link)
        else:
            facebook_profile_link = re.sub(r'\?.*', '', facebook_profile_link)
        print("profile link::::",facebook_profile_link)
        return facebook_profile_link

    # Creating a time entry.
    def find_post_time(self, post):
        time_element = post.find_element_by_css_selector("abbr")
        utime = time_element.get_attribute("data-utime")
        return utime

    def find_post_text(self, post):
        text = post.find_element_by_class_name("userContent").text
        return text

    def collect_groups(self, group):
        self.browser.get('https://www.facebook.com/groups/' + group + '/')
        self.scroll_web_apge()

        # Once the full page is loaded, we can start scraping
        # posts = self.browser.find_elements_by_class_name("userContentWrapper")
        # posts = self.browser.find_element_by_class_name

        posts = self.browser.find_elements_by_xpath("//div[@role='article']")
        print("posts.len: ", len(posts))

        analysis = []

        for count, post in enumerate(posts):

            post, flag = self.find_actual_post(post)
            print(post)

            try:
                # author_name = self.find_post_author(post)
                # fb_profile = self.find_fb_profile(post)
                # utime = self.find_post_time(post)
                text = self.find_post_text(post)
                # gender=self.scrape_gender(fb_profile)
                # print("Gender-----",gender)
                # analysis.append([author_name, fb_profile, utime, text])
                print(analysis)
            except Exception as e:
                print(e)
                continue

            if flag:
                self.browser.close()
                self.browser.switch_to.window(window_name=self.browser.window_handles[0])

        return analysis

def get_data_and_close_last_tab(self):
    if (len(self.driver.window_handles) == 2):
        self.driver.switch_to.window(window_name=self.driver.window_handles[-1])
        self.driver.close()
        self.driver.switch_to.window(window_name=self.driver.window_handles[0])
