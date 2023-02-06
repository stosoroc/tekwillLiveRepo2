from selenium import webdriver # selenium 3.14
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# https://www.selenium.dev/documentation/webdriver/
page = webdriver.Chrome('chromedriver.exe')

page.get("http://google.com")

input_element = page.find_element(by=By.TAG_NAME, value='input')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)
