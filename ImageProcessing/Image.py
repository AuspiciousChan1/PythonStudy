from matplotlib import image, pyplot
import numpy
import os

from utils import vector


class Image:
    # __image用矩阵保存图片， 根据图片特点不同，每个像素点用[R, G, B, A]或[R, G, B]储存
    # 右下角像素点的坐标为（__length-1, width-1）
    __image: numpy.ndarray
    __length: int
    __width: int

    def __init__(self, path: str):
        self.__image = numpy.array(image.imread(path))
        self.__length = len(self.__image[:, 0, 0])
        self.__width = len(self.__image[0, :, 0])

    def __out_of_range(self, x: int, y: int) -> bool:
        return x >= self.__length or x < 0 or y >= self.__width or y < 0

    def show(self):
        numpy.where(self.__image[:, :, 0] < 1, numpy.zeros((self.__length, self.__width)), self.__image[:, :, 0])
        pyplot.imshow(self.__image)
        pyplot.show()

    def has_alpha(self):
        return True if len(self.__image[0, 0, :]) == 4 else False

    def length(self) -> int:
        return self.__length

    def width(self) -> int:
        return self.__width

    def rgba_array(self) -> numpy.ndarray:
        if self.has_alpha():
            return self.__image
        else:
            rgb = self.__image
            alpha = numpy.ones([self.length(), self.width(), 1])
            return numpy.concatenate((rgb, alpha), axis=2)

    def rgb_array(self) -> numpy:
        return self.__image[:, :, 0:3]

    def red_array(self) -> numpy.ndarray:
        return self.__image[:, :, 0]

    def green_array(self) -> numpy.ndarray:
        return self.__image[:, :, 1]

    def blue_array(self) -> numpy.ndarray:
        return self.__image[:, :, 2]

    def alpha_array(self) -> numpy.ndarray:
        return self.__image[:, :, 3] if self.has_alpha() else numpy.array([])

    # 颜色的角相似度
    def color_angle_similarity(self, x0: int, y0: int, x1: int, y1: int) -> float:
        if self.__out_of_range(x0, y0) or self.__out_of_range(x1, y1):
            print("out of range")
            return -1
        v0 = self.__image[x0, y0, 0: 3]
        v1 = self.__image[x1, y1, 0: 3]
        return vector.cosine(v0, v1)

    # 红绿蓝占比
    def rgb_proportion(self, x: int, y: int) -> tuple:
        if self.__out_of_range(x, y):
            print("out of range")
            return -1, -1, -1
        return vector.normalize(self.__image[x, y, 0: 3])

    def red_proportion(self, x: int, y: int) -> float:
        return self.rgb_proportion(x, y)[0]

    def green_proportion(self, x: int, y: int) -> float:
        return self.rgb_proportion(x, y)[1]

    def blue_proportion(self, x: int, y: int) -> float:
        return self.rgb_proportion(x, y)[2]

    def normalize_rgb_array(self):
        img = numpy.reshape(self.__image, (-1, 4))
        color_array = img[:, 0: 3]
        for i in range(len(color_array[:])):
            color_array[i] = vector.normalize(color_array[i])
        return color_array
