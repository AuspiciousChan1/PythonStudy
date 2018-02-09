import numpy
import time
from matplotlib import pyplot
from PIL import Image
from JumpPlugIn import ImageHanlder
from Adb.AdbCommands import AdbCommands

cmd = AdbCommands("SQR7N17224002692")
width = cmd.screen_width()
length = cmd.screen_length()

while True:
    time.sleep(2)
    cmd.shot_pull_rm("../Sources/Shot.png")
    img: Image.Image = Image.open("../Sources/Shot.png")

    # 灰度图
    img_gray0 = ImageHanlder.grayscale(img)

    # 去掉不重要的上下区域
    img_gray = ImageHanlder.remain_center_height(img_gray0)

    xc, yc = ImageHanlder.get_center(img_gray)

    xb, yb = ImageHanlder.get_begin(img_gray, yc>width/2)

    img_gray = ImageHanlder.horizontal_border(img_gray)

    img_gray = ImageHanlder.mark_square(img_gray, xb, yb, 200)
    img_gray = ImageHanlder.mark_square(img_gray, xc, yc, 200)

    dist = numpy.math.sqrt((xc - xb) ** 2 + (yc - yb) ** 2)

    duration = round(dist/200*1.2*230)
    print(duration)
    cmd.swipe(1000, 1000, 1000, 1000, duration)

    pyplot.imshow(numpy.array(img_gray))
    pyplot.show()
