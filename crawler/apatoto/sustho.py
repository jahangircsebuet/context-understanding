from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from python_file.crawler.browser import Browser

browser = Browser(0).getBrowser()
browser.get('https://www.google.com?q=python#q=python')
browser.maximize_window()
first_result = WebDriverWait(browser, 15).until(lambda browser: browser.find_element_by_class_name('rc'))
first_link = first_result.find_element_by_tag_name('a')

# Save the window opener (current window)
main_window = browser.current_window_handle

# Open the link in a new window by sending key strokes on the element
first_link.send_keys(Keys.SHIFT + Keys.RETURN)
sleep(2)
# Get windows list and put focus on new window (which is on the 1st index in the list)
windows = browser.window_handles
print("opened windows length: ", len(windows))
browser.switch_to.window(windows[1])
browser.maximize_window()
# do whatever you have to do on this page, we will just got to sleep for now
sleep(3)

# Close current window
# browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
browser.close()

# Put focus back on main window
browser.switch_to.window(main_window)