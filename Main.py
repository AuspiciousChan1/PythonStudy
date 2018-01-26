import json
import os

import pymongo
import pymongo as pymongo
from pymongo import MongoClient
from Adb.UnlockPhone import UnlockPhone
from matplotlib import image, pyplot
import numpy

# MongoDB
# client = MongoClient('localhost', 27017)
# db_menus = client.menus
# col = db_menus.cao_master

# Adb
# d = 43.6
# t = int(d * 200 + 50)
# os.system("adb shell input swipe 500 500 500 500 %d" % t)

# Matplotlib
from ImageProcessing import Image

ima = Image.Image('Sources/Left.png')
# pyplot.imshow(ima)
ima.show()
print(type(ima))
