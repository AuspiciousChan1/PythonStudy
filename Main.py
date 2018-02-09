import json
import os

import pymongo
import time

from PIL import Image
from pymongo import MongoClient
from matplotlib import image, pyplot
import numpy
from sklearn import cluster, externals

from Adb.AdbCommands import AdbCommands
from ImageProcessing import MyImage
from Clusters import MyCluster
from JumpPlugIn import ImageHanlder



