import json
import os

import pymongo
from pymongo import MongoClient
from matplotlib import image, pyplot
import numpy
from sklearn import cluster, externals

from ImageProcessing import Image
from Clusters import MyCluster

img = Image.Image("Sources/Left.png")
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
# mark = ['sk', 'gray', 'brown', 'sr', 'chocolate', 'tan', 'sy', 'sg', 'slime', 'sc', 'cyan', 'navy', 'sb', 'sm']
mark = ['sk', 'gray', 'brown', 'sr', 'chocolate', 'tan', 'darkgoldenrod', 'sy', 'sg', 'sc', 'cyan', 'navy', 'sb', 'indigo', 'sm', 'pink']
for i in numpy.linspace(0, img_len - 1, 100):
    for j in numpy.linspace(0, img_wid - 1, 50):
        try:
            pyplot.plot(int(j), -int(i), mark[img_res[int(i), int(j)]])
        except ValueError:
            print(mark[img_res[int(i), int(j)]])

pyplot.axis("equal")
pyplot.show()
