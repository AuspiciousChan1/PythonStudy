import json
import os

import pymongo
from pymongo import MongoClient
from matplotlib import image, pyplot
import numpy
from sklearn import cluster, externals

from ImageProcessing import MyImage
from Clusters import MyCluster

img = MyImage.Image("Sources/Left.png")
# print("img: \n", img.rgb_array())
img_len = img.length()
img_wid = img.width()
g_arr = numpy.resize(img.green_array(), (img_len, img_wid, 1))
b_arr = numpy.resize(img.blue_array(), (img_len, img_wid, 1))
data = numpy.concatenate((g_arr, b_arr), axis=2)
# data = data1[img_len/4: img_len*3/4, :]#这一排希望把没用的上四分之一和下四分之一砍掉
data = numpy.reshape(data, (-1, 2))
# print("data:\n", data)
clu = cluster.MiniBatchKMeans(n_clusters=16, max_iter=len(data[:, :]))
result = clu.fit(data)
img_res = numpy.reshape(result.labels_, (img_len, img_wid))
print(img_res)


pyplot.axis("equal")
pyplot.show()
