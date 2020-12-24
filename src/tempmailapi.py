from emailid import EmailID
from tempmail import TempMail
from os import environ, name
import consts
from emailid import EmailID
from inbox import Inbox
from time import sleep

class TempMailAPI():
    __URL=consts.URL
    
    @staticmethod
    def _checkSystemSpec():
        return name

    @staticmethod
    def _setEnviron(environ_var=consts.enviorn_var, environ_val=consts.environ_var_val):
        environ[environ_var]=environ_val

    def __open(self):
        self.__driver.get(TempMailAPI.__URL)

    def getSS(self, ss_path):
        self.__driver.save_screenshot(ss_path)

    @staticmethod
    def find_by_xpath(driver, xpath, attr):
        return driver.find_element_by_xpath(xpath).get_attribute(attr)

    def getEmail(self, sleep_time=1):     
        email=TempMailAPI.find_by_xpath(self.__driver, '//*[@id="mail"]', 'value') 
        while (email.startswith("Loading")):
            sleep(sleep_time)
            email=TempMailAPI.find_by_xpath(self.__driver, '//*[@id="mail"]', 'value')
        print(email)
        self.__temp_mail.setEmailID(email)

    def __init__(self, driver_obj, timeout=10, freq=1):
        os = TempMailAPI._checkSystemSpec()
        if (os!=consts.iden_win):
            TempMailAPI._setEnviron()
        self.__driver=driver_obj
        self.__temp_mail=TempMail(EmailID(), Inbox())
        self.__open()

    def refresh(self):
        pass

    def delEmail(self):
        pass

    def __getSession(self):
        return (self.__driver.session_id)

    def __getCookies(self):
        return (self.__driver.get_cookies())

    def __setSession(self, id):
        self.__driver.session_id=id

    def __setCookies(self):
        pass

    def __setEmail(self):
        pass

    def __setInbox(self):
        pass