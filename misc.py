import os
import sys
import cv2
import numpy as np 
from matplotlib.image import imread
import math
import matplotlib.pyplot as plt

def dist(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.sum((vec2-vec1)**2)


def get_average_color(im):
    pixels = []
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            pixels.append(np.array(im[i, j][:3]))

    color_sum = np.array([0, 0, 0]).astype("float64")
    for pixel in pixels:
        color_sum += pixel

    return (color_sum/len(pixels))

def reduce_size(im, n):
    new = []
    shape = im.shape
    for i in range(0, shape[0], n):
        for j in range(0, shape[1], n):
            new.append(im[i, j][:3])

    try:
        new_shape = (shape[0]//n+1, shape[1]//n+1, 3)
        new = np.array(new).reshape(new_shape)
    except:
        new_shape = (shape[0]//n, shape[1]//n, 3)
        new = np.array(new).reshape(new_shape)
    return new