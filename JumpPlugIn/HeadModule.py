import numpy


class HeadTop:
    average_region_left: numpy.ndarray
    average_region_right: numpy.ndarray
    screen_len: int
    screen_wid: int
    count_left: int
    count_right: int

    def __init__(self, screen_len: int, screen_wid: int):
        self.average_region_left = numpy.zeros(int(200), dtype=numpy.uint8)
        self.average_region_right = numpy.zeros(int(200), dtype=numpy.uint8)
        self.screen_len = screen_len
        self.screen_wid = screen_wid
        self.count_left = 0
        self.count_right = 0

    def insert(self, data: numpy.ndarray, is_left: bool)-> bool:
        if data is None or data.size != self.average_region_left.size:
            return False
        else:
            if is_left:
                if self.__distance(data, True) < 700 or self.count_left < 1:
                    self.average_region_left = (self.average_region_left * self.count_left + data) / (self.count_left + 1)
                    self.count_left += 1
                    return True
                else:
                    return False
            else:
                if self.__distance(data, False) < 700 or self.count_right < 1:
                    self.average_region_right = (self.average_region_right * self.count_right + data) / (self.count_right + 1)
                    self.count_right += 1
                    return True
                else:
                    return False

    def get_data(self, is_left: bool):
        return self.average_region_left if is_left else self.average_region_right

    def get_count(self):
        return self.count

    def data_len(self):
        return self.average_region_left.size

    def __distance(self, data: numpy.ndarray, is_left: bool)-> float:
        if data is None or data.size != self.average_region_left.size:
            return -1
        else:
            if is_left:
                data = numpy.abs(data - self.average_region_left)
                dis = numpy.linalg.norm(data)
            else:
                data = numpy.abs(data - self.average_region_right)
                dis = numpy.linalg.norm(data)
            print("欧拉距离： %f" % dis)
            return dis
