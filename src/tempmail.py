class TempMail():
    def __init__(self, email_id, inbox):
        self.__email_id=email_id
        self.__inbox=inbox
    
    @property
    def email_id(self):
        return self.__email
    
    def getMail(self, msg_num=-1):
        return self.__inbox[msg_num]

    def addMail(self, mail):
        self.__inbox.putEmail(mail)

    @property
    def getInbox(self):
        return self.__inbox.getEmail()
    
    def setEmailID(self, email_id):
        self.__email_id.setEmail(email_id)

    def resetInbox(self):
        self.__inbox.resetInbox()

    def resetEmail(self):
        self.__email_id.resetEmail()

    def __del__(self):
        del self.__email_id
        del self.__inbox