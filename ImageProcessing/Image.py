from matplotlib import image, pyplot
import numpy
import os

from utils import vector


class Image:
    # __image用矩阵保存图片， 根据图片特点不同，每个像素点用[R, G, B, A]或[R, G, B]储存
    __image: numpy.ndarray
    __length: int
    __width: int
    def __init__(self, path: str):
        self.__image = numpy.array(image.imread(path))
        self.__length = len(self.__image[:, 0, 0])
        self.__width = len(self.__image[0, :, 0])

    def show(self):
        self.__image[1000:1250, 400:500, 0] = 0
        numpy.where(self.__image[:, :, 0] < 1, numpy.zeros((self.__length, self.__width)), self.__image[:, :, 0])
        pyplot.imshow(self.__image)
        pyplot.show()

    def has_alpha(self):
        return True if len(self.__image[0, 0, :]) == 4 else False

    def length(self)-> int:
        return self.__length

    def width(self)->int:
        return self.__width

    def red_array(self)-> numpy.ndarray:
        return self.__image[:, :, 0]

    def green_array(self)-> numpy.ndarray:
        return self.__image[:, :, 1]

    def blue_array(self)-> numpy.ndarray:
        return self.__image[:, :, 2]

    def alpha_array(self)-> numpy.ndarray:
        return self.__image[:, :, 3] if self.has_alpha() else numpy.array([])

    def color_angle_similarity(self, x0: int, y0: int, x1: int, y1: int)-> float:
        if numpy.maximum(x0, x1) >= self.__length or numpy.minimum(x0, x1) < 0 or numpy.maximum(y0, y1) >= self.__length or numpy.minimum(y0, y1) < 0:
            print("out of range")
            return 0
        v0 = self.__image[x0, y0, 0: 3]
        v1 = self.__image[x1, y1, 0: 3]
        return vector.cosine(v0, v1)