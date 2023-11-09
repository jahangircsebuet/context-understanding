import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time, re
from .gender import CollectGender


class Group(object):

    def __init__(self, browser, depth):
        self.browser = browser
        self.depth = int(depth)
        self.data = []

    def scrape_gender(self, profile_link):
        print("gender scraping start")
        collect_gender = CollectGender(self.browser)
        gender = collect_gender.scrape_genger(profile_link)
        return gender

    def find_fb_profile(self, facebook_profile_link):
        if "profile.php" in facebook_profile_link:
            facebook_profile_link = re.sub(r'\&.*', '', facebook_profile_link)
        else:
            facebook_profile_link = re.sub(r'\?.*', '', facebook_profile_link)

        return facebook_profile_link

    def closingTabTactics(self):

        baseWin = self.browser.window_handles
        self.browser.findElementBy("home-button").click()

        for winHandle in self.browser.window_handles:
            if winHandle != baseWin:
                self.browser.switchTo().window(winHandle)
                newURL = self.browser.current_url

        # Perform necessary action

        self.browser.close()
        self.browser.switchTo().window(baseWin)
        self.browser.execute_script("window.focus();")

    def scroll_shim(self, object):
        x = object.location['x']
        y = object.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (
            x,
            y
        )
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
        self.browser.execute_script(scroll_by_coord)
        self.browser.execute_script(scroll_nav_out_of_way)

    def collect_groups(self, group):

        self.browser.get('https://www.facebook.com/groups/' + group + '/')

        for scroll in range(self.depth):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("scrol ", scroll)
            self.delay = random.randrange(1, 5)
            time.sleep(self.delay)

        posts = self.browser.find_elements_by_class_name("userContentWrapper")
        print(len(posts))
        analysis = []
        main_window = self.browser.current_window_handle

        for count, post in enumerate(posts):
            # Creating first CSV row entry with the poster name (eg. "Donald Trump")
            # analysis = [poster_names[count].text]
            flag = False

            # handles = self.browser.window_handles
            # self.browser.current_url

            try:
                # self.driver.execute_script("$(\"li:contains('Narendra')\").click()");
                link = post.find_element_by_xpath(".//span[@class='text_exposed_link']//a")
                WebDriverWait(post, 10).until(
                    EC.element_to_be_clickable((By.XPATH, ".//span[@class='text_exposed_link']//a")))

                if link:
                    href = link.get_attribute("href")

                    if '/notes' in href:
                        continue
                    elif '/donate' in href:
                        continue

                    self.scroll_shim(link)
                    actions = ActionChains(self.browser)
                    actions.move_to_element(link)
                    actions.click()
                    actions.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
                    self.browser.maximize_window()
            except Exception as e:
                print("error", e)

            try:
                if (len(self.browser.window_handles) >= 2):
                    self.browser.switch_to.window(window_name=self.browser.window_handles[-1])
                    self.browser.maximize_window()
                    flag = True
                    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
                    driver = self.browser
                    wait = WebDriverWait(driver, 10,ignored_exceptions=ignored_exceptions)
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "userContentWrapper")))
                    post = self.browser.find_element_by_class_name("userContentWrapper")
            except Exception as e:
                print(e)
                continue

            # self.delay = random.randrange(1, 3)
            # time.sleep(self.delay)

            row = []
            try:
                row.append(post.find_element_by_xpath(".//a[@data-hovercard-referer]").text)
            except Exception as e:
                print(e)
                continue

            facebook_profile_link = post.find_element_by_xpath(".//a[@data-hovercard-referer]").get_attribute("href")
            facebook_profile_link = re.sub(r'\?.*', '', facebook_profile_link)
            row.append(facebook_profile_link)

            # Creating a time entry.
            time_element = post.find_element_by_css_selector("abbr")
            utime = time_element.get_attribute("data-utime")
            row.append(utime)

            # Creating post text entry
            text = ""
            try:
                text = post.find_element_by_class_name("userContent").text
            except Exception as e:
                print(e)
                continue

            row.append(text)
            analysis.append(row)
            if flag:
                self.browser.close()
                self.browser.switch_to.window(window_name=self.browser.window_handles[0])



        return analysis


    def closeBrowser(self,main_window):
        if (len(self.browser.window_handles) >= 2):
            for handle in self.browser.window_handles:
                if handle != main_window:
                    self.waitRandomTime()
                    self.browser.switch_to.window(handle)
                    self.browser.close()
        self.browser.switch_to.window(main_window)

    def waitRandomTime(self):
        self.delay = random.randrange(1, 2)
        time.sleep(self.delay)

    def get_data_and_close_last_tab(self):
        if (len(self.driver.window_handles) == 2):
            self.driver.switch_to.window(window_name=self.driver.window_handles[-1])
            self.driver.close()
            self.driver.switch_to.window(window_name=self.driver.window_handles[0])


    def safe_find_element_by_id(self, elem_id):
        try:
            return self.browser.find_element_by_id(elem_id)
        except NoSuchElementException:
            return None


if __name__ == "__main__":
    pass
