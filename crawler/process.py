import random
import time
from nntplib import GroupInfo

import numpy as np
from browser import Browser
from crawler.group import Group
from crawler.login import Login
from crawler.page import Page


# from python_file.crawler.gender import CollectGender
# from python_file.crawler.page import Page
# from python_file.crawler.login import Login
# from python_file.crawler.scraper import Group
# from python_file.database.genderInfo import GenderInfo
# from python_file.database.groupInfo import GroupInfo
# from python_file.database.groupStatus import GroupStatusinDB
# from python_file.utility.apostrophe import Apostrophe


class Process(object):
    def __init__(self, browser, group_or_page_name, depth, type):
        self.browser = browser
        self.group_or_page_name = group_or_page_name
        self.depth = depth
        self.type = type

    def start_data_collection(self, email, password):
        login_fb = Login(self.browser)
        login_fb.login(email, password)
        print("Login is done")
        self.collect_groups(self.group_or_page_name)

        # if self.type == 1:
        #     self.collect_groups(self.group_or_page_name)
        # elif self.type == 2:
        #     self.collect_page(self.group_or_page_name)
        # elif self.type == 3:
        #     print("gender scrapping is started")
        #     self.collect_gender()

    def collect_page(self, page):
        page_post = Page(self.browser)
        page_post.collect_page(page)

    def checkDimensional(self,analysis):
        array_list = np.array(analysis)
        dim = len(array_list.shape)
        return dim

    def collect_groups(self, group):
        group_post = Group(self.browser, self.depth)
        print("Scrapping start")
        analysis = group_post.collect_groups(group)
        print(analysis)
        # groupId = GroupInfo().findGroupID(self.group_or_page_name)
        # dimension = self.checkDimensional(analysis)
        # print("dimension is ", dimension)
        # if dimension == 1:
        #     print(len(analysis))
        #     status = Apostrophe().removeApostrophe(analysis[3])
        #     GroupStatusinDB().insertStatusInfo(analysis, status, groupId)
        # else:
        #     for post in analysis:
        #         status = Apostrophe().removeApostrophe(post[3])
        #         GroupStatusinDB().insertStatusInfo(post, status, groupId)

    def collect_gender(self):
        pass
        # genderInfo = GenderInfo().getGenderFromTableOnlyEmptyGender()
        # for count, row in enumerate(genderInfo):
        #     print("facebook profile", row[1])
        #     gender = CollectGender(self.browser).retrive_gender(row[1])
        #     time.sleep(random.randrange(1, 8))
        #     GenderInfo().updateGenderInfo(row[1], gender)


if __name__ == "__main__":
    browser = Browser(0).getBrowser()  # browser.get('https://whatismyipaddress.com')
    # Process(browser, "asdsad", 1, 1).find_gender_from_facebook_profile('buet.msc.cse', '---------')
    process = Process(browser, "1590338747870221", 1, 1)
    process.start_data_collection('EMAIL', 'PASSWORD')
    # pass

    # analysis = ['রুবাইয়াত বিনতে নাজমুল', 'https://www.facebook.com/ruba149', '1576072120',
    #             '৩৭ এর রিটেনের সময় আমরা আগের বিসিএসগুলার তুলনায় বেশ কম সময় পাইসিলাম। তবে এবারের চেয়ে বেশি সময় ছিল। জুনিয়র অনেকেই হতাশ এটার জন্য, দেখতেসি। but believe me, it can work in a positive way for u. আমরা বেশিরভাগ average Buetian ই কিন্তু শেষ সময়ে এসে পড়ে পাস করা মানুষ। ৩৭ এ পরীক্ষার হলে গিয়ে মনে হইসিল, মানুষ আরো সময় পেলে আরো কত কত ডাটা মুখস্ত করতো, আল্লাহ জানে! Have faith on your learning capability. আর প্রিলিতে যেমন সাধারণ জ্ঞান আসে, রিটেনে ওরকম তথ্য based প্রশ্নের চেয়ে কিছুটা সংজ্ঞা...\nContinue reading']

    # checkDBInfo(analysis)