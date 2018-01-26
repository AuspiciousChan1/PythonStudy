import os
class UnlockPhone:
    __device_id__ = ''
    __password__ = ''

    def __init__(self, device_id: str, password: str):
        self.__device_id__ = device_id
        self.__password__ = password

    def unlock(self):
        device_id = self.__device_id__
        head = 'adb -s %s ' % device_id
        os.system(head + "shell input keyevent 82")
        os.system(head + "shell input text %s" % self.__password__)