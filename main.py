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
new = reduce_size(im, 7)
colors = []
for i, img in enumerate(images):
    colors.append((i, get_average_color(img)))

final = []
m = new.shape[0]
r = new.shape[1]
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
end = np.zeros((m*16, r*16, 4))
w, h = 0, 0
for img in final:
    try:
        end[h:h+16, w:w+16] = img
    except:
        pass
    w += 16
    if w == r*16:
        h += 16
        w = 0

plt.imshow(end)
plt.show()





