import numpy
import scipy
from collections import Iterable
from sklearn import cluster, externals
from ImageProcessing import Image


class MyCluster:
    __data: numpy.ndarray

    def __init__(self, data: Iterable):
        self.__data = numpy.array(data)
