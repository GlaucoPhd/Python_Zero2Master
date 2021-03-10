# Assert is the easy way to test if is correct
# assert 'Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title
# Selector to grab info from body

from selenium import webdriver

chrome_browser = webdriver.Chrome('chromedriver.exe')

# chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
# print('Easy Demo - Simple Form to Automate using Selenium')
assert 'Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title
# button = chrome_browser.find_element_by_class_name('btn-default')
button_text = chrome_browser.find_element_by_class_name('btn-default')
# print(button) # Find the Object NAme

print(button_text.get_attribute('innerHTML'))




