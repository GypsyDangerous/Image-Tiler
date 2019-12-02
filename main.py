from misc import *

PATH = os.getcwd()+"/"

while True:
    picture_name = input("Enter picture filename: ")
    try:
        im = imread(PATH+picture_name, 0)
    except:
        print(f"{PATH+picture_name} is an Invalid image path")
        continue
    break

tile_type = input("Enter Tile Type: ")
disclaimer = ", Minecraft tiles only support '8' and '16' tile sizes" if tile_type == "minecraft" else ""
tile_size = input(f"Enter Tile Size{disclaimer}: ")
size_reduction = int(input("Enter image size reduction scale: "))
new = reduce_size(im, size_reduction)


URL = PATH+f"{tile_type}/{tile_size}x/"
if not os.path.isdir(URL):
    if tile_type == "minecraft":
        raise Exception("Invalid tile size for minecraft tiles")
    URL = PATH+f"{tile_type}/"
paths = os.listdir(URL)
paths = [p for p in paths if p.endswith(".png")]

images = []
alpha = imread(URL+paths[0]).shape[2]

for path in tqdm(paths, desc = "Loading Tiles"):
    img = imread(URL+path)
    if img.shape[2] == alpha:
        img = cv2.resize(img, dsize=(int(tile_size), int(tile_size)), interpolation=cv2.INTER_CUBIC)
        images.append(img)


colors = []
for i, img in (enumerate(images)):
    colors.append((i, get_average_color(img)))

final = []
m, r = new.shape[:2]
for i in tqdm(range(m), desc="generating Image"):
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
    imsave("output/"+filename, end)

    plt.imshow(end)
    plt.show()
except Exception as e:
    final = None
    print(e)






