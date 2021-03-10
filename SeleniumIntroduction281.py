# Selenium work with drivers because of the kind o driver the browsers use
# Create a new instance of the Browser

from selenium import webdriver


chrome_browser = webdriver.Chrome('chromedriver.exe')
chrome_browser.maximize_window()


