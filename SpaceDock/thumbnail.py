from PIL import Image

import os.path

def create(imagePath, thumbnailPath, thumbnailSize):
    if not os.path.isfile(imagePath):
        return
    im = Image.open(imagePath)
    im.thumbnail(thumbnailSize, Image.ANTIALIAS)
    im.save(thumbnailPath,'jpeg',quality=50,optimize=True)