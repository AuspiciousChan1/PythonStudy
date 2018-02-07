import numpy
from matplotlib import pyplot
from PIL import Image
from JumpPlugIn import ImageHanlder

img: Image.Image = Image.open("../Sources/Right.png")

# 灰度图
img_gray0 = ImageHanlder.grayscale(img)

# 去掉不重要的上下区域
img_gray = ImageHanlder.remain_center_height(img_gray0)

img_wid, img_len = img_gray.size

# 图像对应的ndarray（此函数会将本来的矩阵转置后存入ndarray矩阵）
img_arr = numpy.array(img_gray)
img_arr.reshape((img_wid, img_len))

xc, yc = ImageHanlder.get_center(img_gray)

img_arr = ImageHanlder.square_mark(numpy.array(img_gray0), xc + int(img_len/2), yc, 0)

# img_arr = img_arr[:, 0:int(img_wid/2)] if yc > img_wid/2 else img_arr = img_arr[:, int(img_wid/2): img_wid]

# 此函数会将ndarray里的矩阵转置后存进图片
ImageHanlder.show_ndarray_as_image(ImageHanlder.horizontal_border(img_arr))
