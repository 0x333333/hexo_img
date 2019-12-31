from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os


def watermark_text(input_image_path, text):
    print ">> image: " + input_image_path
    photo = Image.open(input_image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    # find the position
    width = photo.size[0]
    height = photo.size[1]
    pos = (width - 150, height - 30)

    white = (255, 255, 255)
    font = ImageFont.truetype("FreeMonoBold.ttf", 20)
    drawing.text(pos, text, fill=white, font=font)
    photo.save(input_image_path)

    print "done"


if __name__ == '__main__':
    arr = os.listdir('.')
    for filepath in arr:
        if ('jpg' in filepath or
            'JPG' in filepath or
            'jpeg' in filepath or
            'JPEG' in filepath or
            'png' in filepath or
            'PNG' in filepath):
            watermark_text(filepath, text='zpjiang.me')
