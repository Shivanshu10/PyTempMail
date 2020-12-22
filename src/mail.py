class Mail():
    def __init__(self, from_id, to_id, msg, attach):
        self.__from_id=from_id
        self.__to_id=to_id
        self.__msg=msg
        self.__attach=attach

    @property
    def from_id(self):
        return self.__from_id

    @property
    def to_id(self):
        return self.__to_id

    @property
    def msg(self):
        return self.__msg

    @property
    def links(self):
        pass

    def _checkAttachment(self):
        pass

    @property
    def attachment(self):
        pass

    def __del__(self):
        del self.__from_id
        del self.__to_id
        del self.__msg
        del self.__attach