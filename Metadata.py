from PIL import Image
from PIL.ExifTags import TAGS

imagename = "IMG_20171018_133144.jpg"

image = Image.open(imagename)

#extract data
info_dict = {
    "Filename" : image.filename,
    "Image Size" : image.size,
    "Image Height" : image.height,
    "Image Width" : image.width,
    "Image Format" : image.format,
    "Image Mode" : image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image" : getattr(image, "n_frames", 1)
}

for label, value in info_dict.items():
    print(f"{label:25}: {value}")

#extract EXIF data
exifdata = image.getexif()

#iterating all EXIF data
for tagid in exifdata:
    #get tag name 
    tag =  TAGS.get(tagid, tagid)
    data = exifdata.get(tagid)

    #decode
    if isinstance(data, bytes):
        data = data.decode

    print(f"{tag:25}: {data}")

