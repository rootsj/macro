
from selenium import webdriver

driver = webdriver.Chrome("static/chromedriver.exe")
driver = driver.get("http://google.com")