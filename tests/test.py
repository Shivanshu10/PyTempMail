import pytempmail
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

# profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.folderList', 2) # custom location
# profile.set_preference('browser.download.manager.showWhenStarting', False)
# profile.set_preference('browser.download.dir', '/home/shivanshu/Downloads')
# profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

options=Options()
options.headless=False

# driver=webdriver.Firefox(profile, options=options, executable_path="/home/shivanshu/Documents/Projects/PyTempMail/src/resource/geckodriver/linux_64/geckodriver")
#driver=webdriver.Firefox(executable_path="/home/shivanshu/Documents/Projects/PyTempMail/src/resource/geckodriver/linux_64/driver")
driver=webdriver.Firefox(executable_path="/home/shivanshu/Documents/Projects/PyTempMail/src/resource/geckodriver/linux_64/driver", options=options)
driver.set_window_size(1366, 728)


t=TempMailAPI(driver_obj=driver, timeout=50)

# print email id
# print(t.email_id)

# get SS
# t.getSS("/home/shivanshu/Documents/Projects/PyTempMail/src/resource/screenshots/ss.png")

# get browser session
# print(t.session_id)

# delete current email and get a new one
# t.delEmail()
# print(t.email_id)

# get two email id both working
# driver=webdriver.Firefox(executable_path="/home/shivanshu/Documents/Projects/PyTempMail/src/resource/geckodriver/linux_64/driver", options=options)
# driver.set_window_size(1366, 728)
# t=TempMailAPI(driver_obj=driver, timeout=50)
# print(t.email_id)

# refresh page
# t.refresh()

# pass current session to other browser get same emaild
# s=t.session_id
# print(t.email_id)
# t=TempMailAPI(driver_obj=driver, timeout=50, session=s)
# print(t.email_id)

# mail num out of range
# print(t.checkMail())

# get mail
while (t.inbox_size==0):
    t.getInbox()
mail=t.checkMail()
print(mail.from_id)
print(mail.date_time)
print(mail.msg)
print(mail.sender_name)
print(mail.subject)