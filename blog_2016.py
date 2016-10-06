from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():
	driver = webdriver.Firefox()
	driver.wait = WebDriverWait(driver, 5)
	return driver

def lookup(driver):
	driver.get('https://www.ece.cmu.edu/~ece734/')

if __name__ == '__main__':
	driver = init_driver()
	lookup(driver)
	time.sleep(5)
	driver.quit()

