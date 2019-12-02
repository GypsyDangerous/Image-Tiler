# Image Tiler
recreate images by tiling smaller images

# Files and Folders
## Folders
 - Images - place the image you want to tile here. there are some example images already in it.
 - Output - the tiled image will be placed in this folder when it is done. there are some example finished images in it.
 - Tiles - This folder contains folders for each tile type. Each tile type has folders for different sizes.
 
## Files
 - Main.py - This is the file you will run to tile an image, it has all the code for the tiler
 - misc.py - This file contains all the imports, and helper functions used in the tiler.
 
# Installation and usage
 1. clone the repo with `git clone https://github.com/GypsyDangerous/Image-Tiler.git`
 2. cd into the repo
 3. install all requirements from requirements.txt
 4. run main.py with your preffered python executor
 5. enter the name of you image
 6. enter what type of tile you want, you can see the available tile types in the Tiles folder
 7. enter the tile size you want. some tile types only support specific size while others support any size. Large tile could result in a memory error
 8. enter how much you want to scale down the resolution of the input image. put 1 if you want to keep the original resolution
 9. find you tiled image in the output folder.
 
