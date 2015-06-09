#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wasserzeichen.py
#  
#  Copyright 2015 kernbeisser bonn kernbeisser@tom-bonn.de
#  License: GPL v2 -- see LICENSE file 
#

__author__ = 'kernbeisser'


from PIL import Image, ImageDraw, ImageFont
import sys


def create_watermark(image_in, text, image_out="result.jpg"):
    
    FONT = 'UbuntuMono-B.ttf'
    # Open the original image
    img = Image.open(image_in)

    # Create a new image for the watermark with an alpha layer (RGBA)
    watermark = Image.new("RGBA", img.size)

    # Get an ImageDraw object so we can draw on the image
    waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")

    # Place the text at (x, y), text color will be (r, g, b).
    tfont = ImageFont.truetype(FONT, 72)
    waterdraw.text((10, img.size[1] - 100), text, font=tfont, fill=(0, 255, 0))

    # Paste the watermark (with alpha layer) onto the original image and save it
    img.paste(watermark, None, watermark)
    img.save(image_out, "JPEG")


def main():
    if len(sys.argv) < 2:
        print("we need an image to work with -- don't we?")
        return
    if len(sys.argv) < 3:
        print("also some text would be nice...")
        return

    # all set? Let's go!
    create_watermark(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
