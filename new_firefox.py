from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True

fp = webdriver.FirefoxProfile()
fp.set_preference('webdriver.firefox.bin', '/Applications/Firefox.app/Contents/MacOS/firefox-bin');

sys.path.append("/Users/lkloh/Downloads/wires")

browser = webdriver.Firefox(capabilities=caps)
browser.get('http://localhost:8000')

