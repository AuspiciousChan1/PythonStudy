from collections import Iterable
import numpy


# 向量和
def add(v0: Iterable, v1: Iterable):
    if v0 is None or v1 is None:
        print('Unexpected None')
        return None
    a0 = numpy.array(v0)
    a1 = numpy.array(v1)
    if len(a0) == len(a1):
        return a0 + a1
    else:
        print('vectors in different size')
        return None


# 点乘
def dot(v0: Iterable, v1: Iterable):
    if v0 is None or v1 is None:
        print('Unexpected None')
        return None
    a0 = numpy.array(v0)
    a1 = numpy.array(v1)
    if len(a0) == len(a1):
        a = a0 * a1
        return a.sum()
    else:
        print('vectors in different size.')
        return None


# 欧几里得度量（长度，距离等）
def euclidean_metric(v: Iterable):
    if v is None:
        print('Unexpected None')
        return None
    a = numpy.array(v)
    r = 0
    for i in a:
        r += i * i
    return numpy.sqrt(r)


# 向量夹角的余弦值
def cosine(v0: Iterable, v1: Iterable):
    if v0 is None or v1 is None:
        print('Unexpected None')
        return None
    a0 = numpy.array(v0)
    a1 = numpy.array(v1)
    if len(a0) == len(a1):
        dot_time = dot(a0, a1)
        len0 = euclidean_metric(v0)
        len1 = euclidean_metric(v1)
        return dot_time/len0/len1
    else:
        print('vectors in different size.')
        return None


# 向量归一化
def normalize(v: Iterable):
    if v is None:
        print('Unexpected None')
        return None
    a = numpy.array(v)
    l = euclidean_metric(a)
    a /= l
    return a


# 维度
def dimension(v: Iterable):
    if v is None:
        print('Unexpected None')
        return None
    tup = tuple(v)
    return len(tup)