from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def scroll_down(browser):
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = browser.execute_script(
        "return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = browser.execute_script(
            "return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height


options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
browser = webdriver.Chrome(chrome_options=options)
# scroll_down(browser)
userId = ""
browser.get('https://space.bilibili.com/' + userId + '/dynamic')
time.sleep(2)
for element in browser.find_elements_by_class_name('card'):
    try:
        content = element.find_element_by_class_name(
            'main-content').find_element_by_class_name('card-content')
        postContent = content.find_element_by_class_name('post-content').find_element_by_class_name(
            'original-card-content').find_element_by_class_name('description').find_element_by_class_name('content-full')
        if postContent:
            for element1 in postContent.find_elements_by_class_name('dynamic-link-hover-bg'):
                tmp = element1.get_attribute('click-title')
                if tmp and tmp == '抽奖详情':
                    browser.execute_script('$(".child-button")[1].click();')
                    time.sleep(0.5)
                    browser.execute_script(
                        '$(".bp-popup-ctnr").find(".bl-button--primary").click();')
                    time.sleep(1)
    except:
        continue
