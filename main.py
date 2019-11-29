from misc import *

PATH = os.getcwd()+"/"
URL = PATH+"16x/"
paths = os.listdir(URL)

images = []

for path in paths:
    if path.endswith(".png"):
        img = imread(URL+path)
        if img.shape[0]*img.shape[1]*img.shape[2] == 1024:
            images.append(img)

im = imread(PATH+"main.png", 0)
new = reduce_size(im, 10)
colors = []
for i, img in enumerate(images):
    colors.append((i, get_average_color(img)))

final = []
m, r = new.shape[:2]
for i in range(m):
    for j in range(r):
        index = 0
        min_dist = math.inf
        pixel = new[i, j]/255
        for k, color in colors:
            d = dist(color, pixel)
            if d < min_dist:
                min_dist = d
                index = k
        final.append(images[index])

final = np.array(final)
end = stitch(final, (m, r), (16, 16))

plt.imshow(end)
plt.show()





