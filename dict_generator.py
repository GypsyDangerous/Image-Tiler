import pickle
from matplotlib.image import imread
import os
import numpy as np 
import math


URL = r"C:\Users\david\Downloads\Old_Default_1.13.2\assets\minecraft\textures\block/"
paths = os.listdir(URL)

images = []

for path in paths:
    if path.endswith(".png"):
        img = imread(URL+path)
        if img.shape[0]*img.shape[1]*img.shape[2] == 1024:
            images.append(img)


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


color_dict = {
    "red": ([255, 0, 0], [])
    # "green": ([0, 255, 0], []),
    # "blue": ([0, 255, 0], []),
    # "yellow": ([255, 255, 0], []),
    # "orange": ([255, 127, 0], []),
    # "white": ([255, 255, 255], []) 
}

colors = []
for i, img in enumerate(images):
    colors.append((i, get_average_color(img)))

for i, color in colors:
    min_d = math.inf
    index = ""
    for name in color_dict.keys():
        base_color = color_dict[name][0]
        d = dist(color*255, base_color)
        if d < min_d:
            min_d = d
            index = name
    color_dict[index][1].append((i, color))

print(color_dict.keys())


with open("color_dict", "wb") as f:
    pickle.dump(color_dict, f)