import numpy
from matplotlib import pyplot
from PIL import Image
from JumpPlugIn import ImageHanlder

img: Image.Image = Image.open("../Sources/Left.png")

# 灰度图
img_gray0 = ImageHanlder.grayscale(img)

# 去掉不重要的上下区域
img_gray = ImageHanlder.remain_center_height(img_gray0)

xc, yc = ImageHanlder.get_center(img_gray)

img_gray = ImageHanlder.horizontal_border(img_gray)

# img_gray = ImageHanlder.mark_square(img_gray, xc, yc, 0)

img_gray.show()

ImageHanlder.output_ndarray_to_file(numpy.array(img_gray))
