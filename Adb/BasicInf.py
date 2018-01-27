class BasicInf:
    __device_id: ""
    __password = ""
    __screen_width = 0
    __screen_length = 0

    def __init__(self, device_id: str, password="", screen_width=0, screen_length=0):
        if device_id is not None:
            self.__device_id = device_id
        if password is not None:
            self.__password = password

        self.__screen_width = screen_width
        self.__screen_length = screen_length

    def to_string(self):
        d: dict
        d['device_id'] = self.__device_id
        d['password'] = self.__password
        d['screen_width'] = self.__screen_width
        d['screen_length'] = self.__screen_length
        return str(d)
