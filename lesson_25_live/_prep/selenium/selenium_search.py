from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://google.com")

element = driver.find_element(By.TAG_NAME, 'input')  # Finding the search input field
element.send_keys('Python')  # Typing Python in the input field
element.send_keys(Keys.RETURN)  # Pressing enter
images_link = driver.find_element_by_link_text("Mai multe imagini")
images_link.click()

from bs4 import BeautifulSoup

soup = BeautifulSoup(driver.page_source)  # accessing the HTML of the page
print([a.get('src') for a in soup.find_all('img')])
driver.quit()
