from misc import *

PATH = os.getcwd()+"/"

while True:
    picture_name = input("Enter picture filename: ")
    try:
        im = imread(PATH+picture_name, 0)
    except:
        continue
    break

tile_type = input("Enter Tile Type: ")
tile_size = input("Enter Tile Size: ")
size_reduction = int(input("Enter image size reduction scale: "))
new = reduce_size(im, size_reduction)

URL = PATH+f"{tile_size}x/"
paths = os.listdir(URL)
paths = [p for p in paths if p.endswith(".png")]

images = []
alpha = imread(URL+paths[0]).shape[2]

print("Loading Tiles")
for path in tqdm(paths):
    img = imread(URL+path)
    if img.shape[1] == int(tile_size) and img.shape[0] ==int(tile_size) and img.shape[2] == alpha:
        images.append(img)

colors = []
print()
print("getting colors from tiles")
for i, img in tqdm(enumerate(images)):
    colors.append((i, get_average_color(img)))

final = []
m, r = new.shape[:2]
print()
print("generating image")
for i in tqdm(range(m)):
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

try:
    final = np.array(final)
    end = stitch(final, (m, r), (int(tile_size), int(tile_size)))

    filename = input("Enter output filename: ")
    imsave(filename, end)
    
    plt.imshow(end)
    plt.show()
except:
    final = None
    print("Memory Error")






