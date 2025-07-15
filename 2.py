import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.ChromiumEdge()
driver.get("https://varzesh3.com")
inputs=driver.find_elements(By.CLASS_NAME,"search-btn")
main=driver.find_element(By.CLASS_NAME,"main-search")
input=inputs.click()
main.send_keys("بارسلونا")
time.sleep(5)