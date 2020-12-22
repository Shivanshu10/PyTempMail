class TempMail():
    def __init__(self, email_id=0, inbox=0):
        self.__email_id=email_id
        self.__inbox=inbox
    
    @property
    def email_id(self):
        return self.__email
    
    @property
    def email(self, msg_num=-1):
        return self.__inbox[msg_num]

    def _add_mail(self, mail):
        self.__inbox.putEmail(mail)

    def refresh(self, mail):
        return self._add_mail(mail)

    @property
    def get_inbox(self):
        return self.__inbox.getEmail()
    
    def setEmailID(self, email_id):
        self.__email_id=email_id

    def delEmailID(self):
        del self.__email_id

    def __del__(self):
        del self.__email_id
        del self.__inbox