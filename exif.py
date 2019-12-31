from PIL import Image, ExifTags
import os

arr = os.listdir('.')

for filepath in arr:
    print ">> file: " + filepath
    if ('jpg' in filepath or 
        'JPG' in filepath or 
        'jpeg' in filepath or 
        'JPEG' in filepath or 
        'png' in filepath or
        'PNG' in filepath):
        try:
            image = Image.open(filepath)
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            exif = dict(image._getexif().items())

            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)
            else:
                print "skip"
                continue

            print "rotate"
            image.save(filepath)
            image.close()

        except (AttributeError, KeyError, IndexError, IOError):
            # cases: image don't have getexif
            print "failed"
            pass
