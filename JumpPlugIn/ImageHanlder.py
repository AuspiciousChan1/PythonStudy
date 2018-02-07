from collections import Iterable

import numpy
from PIL import Image


def output_gray_img_array(arr: numpy.ndarray):
    f0 = open("../Sources/output.txt", "w")
    f0.write("")
    f0.close()
    f = open("../Sources/output.txt", "a")
    w, l = arr.shape
    for i in range(w):
        for j in range(l):
            f.write("%d " % int(arr[i, j]))
        f.write("\n")
    f.close()


# 返回灰度图
def grayscale(img: Image.Image)-> Image.Image:
    return img.convert("L")


# 保留y方向上中间的图片
def remain_center_height(img: Image.Image)-> Image.Image:
    w, l = img.size
    return img.crop((0, l/4, w, l*3/4))


def horizontal_border(img: numpy.ndarray)-> numpy.ndarray:
    if isinstance(img, Iterable) and isinstance(img[0], Iterable):
        w, l = img.shape
        img[0, :] = numpy.zeros((1, l), dtype=float)
        for i in range(w-1):
            img[i, :] -= img[i+1, :]
        img = numpy.abs(img)
    return img


def show_ndarray_as_image(img_arr: numpy.ndarray):
    img = Image.fromarray(img_arr)
    img.show()


def square_mark(img_arr: numpy.ndarray, x: int, y: int, light=255)->numpy.ndarray:
    w, l = img_arr.shape
    x_min = x-5 if x >= 5 else 0
    x_max = x+5 if x < w-5 else w-1
    y_min = y-5 if y >= 5 else 0
    y_max = y+5 if y < l-5 else l-1
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            img_arr[i, j] = light
    return img_arr


# 获取下一个块的顶点坐标
def get_top(img_gray: Image.Image)->tuple:
    img_arr = numpy.array(img_gray)
    img_arr = horizontal_border(img_arr)
    xs, ys = numpy.where(img_arr > 64)
    top_index = numpy.where(xs == xs.min())
    x_top = int(numpy.average(xs[top_index]))
    y_top = int(numpy.average(ys[top_index]))
    return x_top, y_top


# 判断是人头还是目标方块
def is_head_top(img_arr: numpy.ndarray, x: int, y: int):
    return img_arr[x+5, y] > 64


# 获取下一个块的中点坐标
def get_center(img_gray: Image.Image)->tuple:
    img_arr = numpy.array(img_gray)
    img_arr = horizontal_border(img_arr)
    xs, ys = numpy.where(img_arr > 64)
    top_indexes = numpy.where(xs == xs.min())
    x_top = int(numpy.average(xs[top_indexes]))
    y_top = int(numpy.average(ys[top_indexes]))
    x_bottom = 0
    y_bottom = y_top
    # vertical_center_line是x从x_top到图片底部，y=y_top，所以算出的x_bottom要加上(x_top+5)才是才是真正的x_bottom
    vertical_center_line = img_arr[x_top+5:img_arr.shape[0], y_bottom]
    light_points_indexes = numpy.where(vertical_center_line > 64)
    x_bottom = light_points_indexes[0][0] + x_top + 5

    x_target = int((x_top + x_bottom) / 2)
    y_target = int((y_top + y_bottom) / 2)

    return x_target, y_target



