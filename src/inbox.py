class Inbox():
    def __init__(self):
        self.__inbox=[]
    
    def putMail(self, mail):
        self.__inbox.append(mail)

    def getMail(self, mail_number):
        return self.__inbox[mail_number]

    @property
    def getInboxSize(self):
        return len(self.__inbox)

    @property
    def mails(self):
        return self.__inbox

    def resetInbox(self):
        del self.__inbox
        self.__inbox=[]

    def __del__(self):
        del self.__inbox