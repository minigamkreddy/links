import time
#from selenium.webdriver.support.ui import select
from selenium import webdriver
import sys
from time import gmtime,strftime

def _pre_req():
        driver=webdriver.Firefox()
#        driver.Set_Page_Load.timeout(180)
        driver.delete_all_cookies()
        return driver
def ap_login(ip):
    try:
        driver = _pre_req()
        print("http://"+ip)
        driver.get("http://"+ip)
    except Exception as e:
        print e
        return False
    time.sleep(5)
    return True

def close_webdriver():
    driver.quit()
    return True


ap_login("192.168.0.1")
