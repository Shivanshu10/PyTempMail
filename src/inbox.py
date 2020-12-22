class Inbox():
    def __init__(self):
        self.__inbox=[]
    
    def putEmails(self, mail):
        self.__inbox.append(mail)

    def getEmail(self, mail_number):
        return self.__inbox[mail_number]

    @property
    def emails(self):
        return self.__inbox

    def __del__(self):
        del self.__inbox