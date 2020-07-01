import selenium
from selenium.webdriver.support.ui import select
from selenium.webdriver.support.ui import webdriver
from time import gmtime,strftime
import sys

def _pre_req():
    driver=webdriver.Firefox()
    driver.set_page_Load.timeout(180)
    driver.delete_all_cookies()


def ap_login_ui(ip_value):
    try:
        _pre_req()
        print("http://"+ip_value)
        driver.get("http://"+ip_value)
    except Exception as e:
        print e
        return False
    time.sleep(5)
    return Time

def close_web_driver():
    driver.quit()
    return True
