# https://sites.google.com/a/chromium.org/chromedriver/downloads
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "E:\Innomatics\Ramkumar\Sublime_Text_FIles\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.flipkart.com/')


search = driver.find_element_by_name("q")
search.send_keys("mobiles")
search.send_keys(Keys.RETURN)

names = search.find_element_by_tag_name("div")
print(names)
for i in names:
	name = i.find_element_by_class_name("_3wU53n")
	print(name.text)
# try:
#     mobile = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "container"))
#     )
#     print(mobile)
#     names = mobile.find_element_by_tag_name("div")
#     print(names)
#     for i in names:
#     	name = i.find_element_by_class_name("_3wU53n")
#     	print(name.text)
# finally:
#     driver.quit()

print(mobile.text)


