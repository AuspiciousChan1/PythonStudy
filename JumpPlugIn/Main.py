import numpy
import time
from matplotlib import pyplot
from PIL import Image
from numpy import random
from JumpPlugIn.HeadModule import HeadTop

from JumpPlugIn import ImageHanlder
from Adb.AdbCommands import AdbCommands

cmd = AdbCommands("SQR7N17224002692")
width = cmd.screen_width()
length = cmd.screen_length()
head_top_data = HeadTop(length, width)
while True:
    time.sleep(1.5 + (random.random_integers(0, 63, 1)[0] / 128))
    cmd.shot_pull_rm("../Sources/Shot.png")
    img: Image.Image = Image.open("../Sources/Shot.png")

    # 灰度图
    img_gray0 = ImageHanlder.grayscale(img)

    # 去掉不重要的上下区域
    img_gray = ImageHanlder.remain_center_height(img_gray0)

    xc, yc = ImageHanlder.get_center(img_gray)

    xb, yb = ImageHanlder.get_begin(img_gray, yc > width/2)
    is_begin_left = (yb < width/2)

    img_gray_arr = numpy.array(img_gray)
    if (not head_top_data.insert(img_gray_arr[xb - 200: xb, yb], is_begin_left)) or xc >= xb:
        # ig0 = img_gray
        ig0 = ImageHanlder.horizontal_border(img_gray)
        ig0 = ImageHanlder.mark_square(ig0, xb, yb, 255)
        ig0 = ImageHanlder.mark_square(ig0, xb - 200, yb, 200)
        ig0 = ImageHanlder.mark_square(ig0, xc, yc, 200)
        pyplot.imshow(numpy.array(ig0))
        pyplot.show()

        is_begin_left = not is_begin_left
        xc, yc = ImageHanlder.get_center(img_gray_arr[:, int(width/2): width] if is_begin_left else img_gray_arr[:, 0: int(width/2)])
        yc = yc + int(width/2) if is_begin_left else yc
        xb, yb = ImageHanlder.get_begin(img_gray, yc > width / 2)
        if (not head_top_data.insert(img_gray_arr[xb - 200: xb, yb], is_begin_left)) or xc >= xb:
            # ig1 = img_gray
            ig1 = ImageHanlder.horizontal_border(img_gray)
            ig1 = ImageHanlder.mark_square(ig1, xb, yb, 255)
            ig1 = ImageHanlder.mark_square(ig1, xb - 200, yb, 200)
            ig1 = ImageHanlder.mark_square(ig1, xc, yc, 200)
            pyplot.imshow(numpy.array(ig1))
            pyplot.show()
            break

    print("起点坐标：(%d, %d)" % (xb, yb))
    print("终点坐标：(%d, %d)" % (xc, yc))

    dist = numpy.math.sqrt((xc - xb) ** 2 + (yc - yb) ** 2)

    duration = round(dist/200*1.2*228)
    print("按压时间：%d" % duration)

    x = random.random_integers(820, 996, 1)[0]
    y = random.random_integers(1303, 1612, 1)[0]
    cmd.swipe(x, y, x, y, duration)
