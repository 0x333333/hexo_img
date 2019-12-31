from PIL import Image
import os

arr = os.listdir('.')
BASE_WIDTH = 1024

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
            width = float(image.size[0])
            height = float(image.size[1])
            if width > BASE_WIDTH:
                ratio = BASE_WIDTH / width
                print "ratio: " + str(ratio)
                width = BASE_WIDTH
                height = int(height * ratio)
            else:
                print "skip"

            image = image.resize((width, height), Image.ANTIALIAS)
            image.save(filepath)
            image.close()

        except (AttributeError, KeyError, IndexError, IOError):
            # cases: image don't have getexif
            print "failed"
            pass
