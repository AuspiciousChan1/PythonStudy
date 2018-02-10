from collections import Iterable

import numpy
from PIL import Image


def output_ndarray_to_file(arr: numpy.ndarray):
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


# Image转换类型为ndarray
def to_ndarry(img_gray: Image.Image) -> numpy.ndarray:
    return numpy.array(img_gray)


# ndarray转换类型为Image
def from_ndarray(img_arr: numpy.ndarray) -> Image.Image:
    return Image.fromarray(img_arr)


# 返回灰度图
def grayscale(img: Image.Image) -> Image.Image:
    return img.convert("L")


def is_gray_img(img: Image.Image) -> bool:
    if img is None:
        print("Not gray image: None")
        return False
    arr = numpy.array(img)
    if len(arr.shape) is not 2:
        print("Not gray image: dimension is not 2")
        return False
    too_big = numpy.where(arr > 255)[0]
    too_small = numpy.where(arr < 0)[0]
    if len(too_big) + len(too_small) > 0:
        print("Not gray image: out of range")
        return False
    return True


# 保留y方向上中间的图片
def remain_center_height(img: Image.Image) -> Image.Image:
    w, l = img.size
    return img.crop((0, l / 4, w, l * 3 / 4))


def horizontal_border(img_gray: Image.Image) -> Image.Image:
    if is_gray_img(img_gray):
        img_arr = to_ndarry(img_gray)
        w, l = img_arr.shape
        for i in range(w - 1):
            img_arr[i, :] -= img_arr[i + 1, :]
        img_arr[w - 1, :] = numpy.zeros((1, l), dtype=int)
        img_arr = numpy.abs(img_arr)
        return from_ndarray(img_arr)
    else:
        return img_gray


def show_ndarray_as_image(img_arr: numpy.ndarray):
    img = Image.fromarray(img_arr)
    img.show()


# 在灰度图上绘制正方形的标记
def mark_square(img_gray: Image.Image, x: int, y: int, light=255) -> Image.Image:
    if is_gray_img(img_gray):
        img_arr = numpy.array(img_gray)
        w, l = img_arr.shape
        x_min = x - 5 if x >= 5 else 0
        x_max = x + 5 if x < w - 5 else w - 1
        y_min = y - 5 if y >= 5 else 0
        y_max = y + 5 if y < l - 5 else l - 1
        img_arr[x_min:x_max+1, y_min: y_max+1] = light
        # for i in range(x_min, x_max + 1):
        #     for j in range(y_min, y_max + 1):
        #         img_arr[i, j] = light
        return Image.fromarray(img_arr)
    else:
        return img_gray


# 获取起点位置
def get_begin(img_gray: Image.Image, is_left: bool) -> tuple:
    screen_divide = 7/15

    img_gray = horizontal_border(img_gray)
    img_arr = numpy.array(img_gray)
    l, w = img_arr.shape
    # print("width: %d" % w)
    img_arr = img_arr[:, 0: int(w * screen_divide)] if is_left else img_arr[:, int(w * (1 - screen_divide)): w]
    xs, ys = numpy.where(img_arr >= 255)
    top_index = numpy.where(xs == numpy.min(xs))
    x_top = int(numpy.average(xs[top_index])) + int(200/960*img_arr.shape[0])
    y_top = int(numpy.average(ys[top_index]))

    y_top = y_top if is_left else y_top + int(w * (1 - screen_divide))

    return x_top, y_top


# 获取下一个块的顶点坐标
def get_top(img_gray: Image.Image) -> tuple:
    img_gray = horizontal_border(img_gray)
    img_arr = numpy.array(img_gray)
    xs, ys = numpy.where(img_arr > 64)
    top_index = numpy.where(xs == xs.min())
    x_top = int(numpy.average(xs[top_index]))
    y_top = int(numpy.average(ys[top_index]))
    return x_top, y_top


# 获取下一个块的中点坐标
def get_center(img_gray: Image.Image) -> tuple:
    img_gray = horizontal_border(img_gray)
    img_arr = numpy.array(img_gray)
    xs, ys = numpy.where(img_arr > 8)
    top_indexes = numpy.where(xs == xs.min())
    x_top = int(numpy.average(xs[top_indexes]))
    y_top = int(numpy.average(ys[top_indexes]))
    x_bottom = 0
    y_bottom = y_top
    # vertical_center_line是x从x_top到图片底部，y=y_top，所以算出的x_bottom要加上(x_top+5)才是才是真正的x_bottom
    vertical_center_line = img_arr[x_top + 50:img_arr.shape[0], y_bottom]
    light_points_indexes = numpy.where(vertical_center_line > 8)
    x_bottom = light_points_indexes[0][0] + x_top + 50

    x_target = int((x_top + x_bottom) / 2)
    y_target = int((y_top + y_bottom) / 2)

    return x_target, y_target


def is_high_light_region(img_gray: Image.Image, x: int, y: int)->bool:
    if is_gray_img(img_gray):
        img_arr = numpy.array(img_gray)
        l, w = img_arr.shape
        half_reg = 10
        x_min = x - half_reg if x >= half_reg else 0
        x_max = x + half_reg if x < l - half_reg else l - 1
        y_min = y - half_reg if y >= half_reg else 0
        y_max = y + half_reg if y < w - half_reg else w - 1
        avg = numpy.average(img_arr[x_min:x_max + 1, y_min: y_max + 1])
        return avg > 128

    else:
        print("Error: Not gray image")
        return False


def is_top_head(img_gray: Image.Image, x_top: int, y_top: int)->bool:
    if is_gray_img(img_gray):
        img_arr = numpy.array(img_gray)
        l, w = img_arr.shape
        if x_top > l - 200:
            print("x_top is too big")
            return False
        avg = numpy.average(img_arr[x_top:x_top + 6, y_top])
        # print("avg: %f" % avg)
        return avg <= 60
    else:
        print("Error: Not gray image")
        return False
