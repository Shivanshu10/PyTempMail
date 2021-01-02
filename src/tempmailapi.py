from selenium.common.exceptions import NoSuchElementException
from emailid import EmailID
from tempmail import TempMail
import consts
from emailid import EmailID
from inbox import Inbox
from time import sleep
from mail import Mail
import logging
from threading import Thread
from timer import Clock
from timerexcep import TimerException

class TempMailAPI():
    __URL=consts.URL

    def __open(self):
        self.__driver.get(TempMailAPI.__URL)
        logging.info("opened site")
        self.__getEmail(self.timeout, self.sleep_time)
        self.__getInbox()

    @property
    def email_id(self):
        return self.__temp_mail.email_id

    def getSS(self, ss_path):
        logging.info("taking screenshot")
        self.__driver.save_screenshot(ss_path)
        logging.info("took screenshot")

    @staticmethod
    def _find_by_xpath(driver, xpath):
        return driver.find_element_by_xpath(xpath)

    def checkMail(self, mail_num=-1):
        self.__temp_mail.getMail(mail_num).click()
        self.__driver.back()
        return self.__parseMail()

    def __getEmail(self, timeout, sleep_time):
        logging.info("Getting email")
        logging.info("staring timer process")
        clock=Clock()
        clock_thread=Thread(target=clock.run, args=(timeout,))
        clock_thread.start()
        email=TempMailAPI._find_by_xpath(self.__driver, consts.email_selector) .get_attribute('value')
        while (email.startswith("Loading")):
            if (clock_thread.is_alive()==False):
                logging.info("Could not finish in given timeout")
                raise TimerException("Couldn't finish task in given timeout")
            logging.info("dont found email")
            sleep(sleep_time)
            logging.info("trying again for email")
            email=TempMailAPI._find_by_xpath(self.__driver, consts.email_selector).get_attribute('value')
        print(email)
        logging.debug(email)
        logging.info("Found email")
        logging.info("closing timer process")
        clock.terminate()
        logging.info("associating email with object")
        self.__temp_mail.setEmailID(email)
        logging.info("associated email with object")

    def __init__(self, driver_obj, session=0, timeout=20, sleep_time=1):
        logging.info("creating api object")
        self.__driver=driver_obj
        self.timeout=timeout
        self.sleep_time=sleep_time
        if (session != 0):
            self.__driver.session_id=session
        self.__temp_mail=TempMail(EmailID(), Inbox())
        self.__open()
        logging.info("Created api object")

    def refresh(self):
        TempMailAPI._find_by_xpath(self.__driver, consts.refresh_button_selector).click()
        self.__getInbox()

    def changeEmail(self):
        TempMailAPI._find_by_xpath(self.__driver, '//*[@id="click-to-change"]').click()
        self.__temp_mail.resetInbox()
        self.__temp_mail.resetMail()
        self.__getEmail(self.timeout, self.sleep_time)
        return self.__driver.session_id
    
    def delEmail(self):
        TempMailAPI._find_by_xpath(self.__driver, '//*[@id="click-to-delete"]').click()
        self.__temp_mail.resetInbox()
        self.__temp_mail.resetMail()
        self.__getEmail(self.timeout, self.sleep_time)

    @property
    def session_id(self):
        return (self.__driver.session_id)

    def __getMails(self):
        mail='/html/body/main/div[1]/div/div[3]/div[2]/div/div[1]/div/div[4]/ul/li[' 
        place=']/div[3]/div[2]/a/svg'
        i=2
        while (True):
            try:
                xpath=mail+str(i)+place
                yield TempMailAPI._find_by_xpath(self.__driver, xpath)
                i+=1
            except NoSuchElementException:
                 # print(i)
                 break

    def __getInbox(self):
        self.__getMails()
        for mail in self.__getMails():
            self.__temp_mail.addMail(mail)

    def __parseMail(self):
        sender_name=TempMailAPI._find_by_xpath(self.__driver, consts.sender_name)
        date_time=TempMailAPI._find_by_xpath(self.__driver, consts.mail_date_time)
        sender_email=TempMailAPI._find_by_xpath(self.__driver, consts.sender_email)
        subject=TempMailAPI._find_by_xpath(self.__driver, consts.mail_subject)
        text=TempMailAPI._find_by_xpath(self.__driver, consts.mail_text)
        #attach=TempMailAPI._find_by_xpath(self.__driver, consts.mail_attach).click()
        return Mail(sender_email, sender_name, date_time, subject, text)
    
    def __del__(self):
        del self.__driver
        del self.__temp_mail