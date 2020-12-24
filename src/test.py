from tempmailapi import TempMailAPI
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options=Options()
options.headless=True

driver=webdriver.Firefox(options=options, executable_path="/home/shivanshu/Documents/Projects/PyTempMail/src/resource/geckodriver/linux_64/geckodriver")
driver.set_window_size(1366, 728)

t=TempMailAPI(driver)
t._TempMailAPI__open()
t.getSS("/home/shivanshu/Documents/Projects/PyTempMail/src/resource/screenshots/ss.png")
t.getEmail()