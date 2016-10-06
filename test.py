from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys, os


caps = DesiredCapabilities.FIREFOX
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/Users/lkloh/Downloads/wires')
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
sys.path.append("/Users/lkloh/Downloads/wires")
print sys.path



driver = webdriver.Firefox(firefox_binary=binary)

# export PYTHONPATH="/Users/lkloh/Downloads/wires:$PYTHONPATH"
# export PATH="/Users/lkloh/Downloads/wires:$PATH"


driver.get('https://www.google.com/')

