import os


class AdbCommands:
    __command_header = ""

    def __init__(self, device_id: str):
        self.__command_header = "adb -s %s" % device_id

    # 执行adb命令
    @staticmethod
    def __execute(cmd: str):
        os.system(cmd)

    # 将SD卡下的目录补充为完整目录
    @staticmethod
    def __to_phone_addr(addr: str)->str:
        if addr is None or len(addr) == 0:
            return "/sdcard"
        else:
            addr.replace('\\', '/')
            pre = "/sdcard" if addr[0] == '/' else "/sdcard/"
            return "%s%s" % (pre, addr)

    def tap(self, x: int, y: int):
        cmd = "%s shell input tap %d %d" % (self.__command_header, x, y)
        self.__execute(cmd=cmd)

    # 滑动屏幕
    def swipe(self, x0: int, y0: int, x1: int, y1: int, duration: int):
        cmd = "%s shell input swipe %d %d %d %d %d" % \
             (self.__command_header, x0, y0, x1, y1, duration)
        self.__execute(cmd=cmd)

    # 输入文字
    def input(self, text: str):
        if text is None:
            text = ""
        cmd = "%s shell input text %s" % (self.__command_header, text)
        self.__execute(cmd=cmd)

    # 截图并保存到SD卡的store_address目录下（/sdcard/%s) % store_address
    def screen_shot(self, store_address: str):
        store_address = self.__to_phone_addr(store_address)
        cmd = "%s shell /system/bin/screencap -p %s" % (self.__command_header, store_address)
        self.__execute(cmd=cmd)

    # 将安卓设备上的文件上传到电脑
    def file_to_computer(self, address_in_computer: str, address_in_phone=""):
        address_in_phone = self.__to_phone_addr(address_in_phone)
        cmd = "%s pull %s %s" % (self.__command_header, address_in_phone, address_in_computer)
        self.__execute(cmd=cmd)

    # 删除安卓设备上的文件
    def remove_file(self, address: str):
        address = self.__to_phone_addr(address)
        if address is None or len(address) < 1:
            cmd = ""
        else:
            cmd = "%s shell rm %s" % (self.__command_header, address)
        self.__execute(cmd)

# 组合函数
    # 截屏，上传到电脑，然后删除安卓端的截图
    def shot_pull_rm(self, store_address: str):
        self.screen_shot("/ScrShot.png")
        self.file_to_computer(store_address, "/ScrShot.png")
        while not os.path.exists(store_address):
            pass
        self.remove_file("ScrShot.png")
