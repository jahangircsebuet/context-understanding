import traceback
from python_file.crawler.process import Process
from python_file.crawler.browser import Browser

class Scraping():
    def __init__(self):
        pass

    def stratScraping(self,email, password, type, group_or_page_name, depth, proxyUse):
        try:
            browser = Browser(proxyUse).getBrowser()  # browser.get('https://whatismyipaddress.com')
            process = Process(browser, group_or_page_name, depth, int(type))
            process.start_data_collection(email, password)
            # process.find_gender_from_facebook_profile(file_name)

        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())

    def stratGenderScraping(self,email, password, type, group_or_page_name, depth, proxyUse):
        try:
            browser = Browser(proxyUse).getBrowser()  # browser.get('https://whatismyipaddress.com')
            process = Process(browser, group_or_page_name, depth, 3)
            process.start_data_collection(email,password)

        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())


