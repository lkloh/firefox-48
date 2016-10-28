from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
rom selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from xvfbwrapper import Xvfb

# def init_driver():
# 	driver = webdriver.Firefox()
# 	driver.wait = WebDriverWait(driver, 5)
# 	return driver

def init_driver():
	firefox_capabilities = DesiredCapabilities.FIREFOX
	firefox_capabilities['marionette'] = True

	vdisplay = Xvfb(width=1280, height=720)
	vdisplay.start()

	driver = webdriver.Firefox(capabilities=firefox_capabilities)
	driver.wait = WebDriverWait(driver, 2)

	return driver




def lookup(driver):
	driver.get('https://www.ece.cmu.edu/~ece734/')




if __name__ == '__main__':
	driver = init_driver()
	lookup(driver)
	time.sleep(2)
	driver.quit()






