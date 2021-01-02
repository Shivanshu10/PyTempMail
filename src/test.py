from tempmailapi import TempMailAPI
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.folderList', 2) # custom location
# profile.set_preference('browser.download.manager.showWhenStarting', False)
# profile.set_preference('browser.download.dir', '/home/shivanshu/Downloads')
# profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

options=Options()
options.headless=True

# driver=webdriver.Firefox(profile, options=options, executable_path="/home/shivanshu/Documents/Projects/PyTempMail/src/resource/geckodriver/linux_64/geckodriver")
#driver=webdriver.Firefox(executable_path="/home/shivanshu/Documents/Projects/PyTempMail/src/resource/geckodriver/linux_64/driver")
driver=webdriver.Firefox(executable_path="/home/shivanshu/Documents/Projects/PyTempMail/src/resource/geckodriver/linux_64/driver", options=options)
driver.set_window_size(1366, 728)

t=TempMailAPI(driver_obj=driver)
# t.getSS("/home/shivanshu/Documents/Projects/PyTempMail/src/resource/screenshots/ss.png")
# t.getEmail()
# t.getInbox()