from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/Users/lkloh/firefox-48/firefox/firefox-bin')
fp = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_binary=binary)


driver.get('https://www.google.com/')

