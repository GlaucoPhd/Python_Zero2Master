from selenium import webdriver

chrome_browser = webdriver.Chrome('chromedriver')

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Glauco')
show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')

assert 'Glauco' in output_message.text

chrome_browser.quit()