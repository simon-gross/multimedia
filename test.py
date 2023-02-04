# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:16:28 2022

@author: Simsi_Arbeit
"""
import os
import numpy as np
from PIL import Image
import copy


# Open the two images
image1 = Image.open(r"D:\ucloud\Multi\Projekt_2\finished_material\countries_animation\pop_up_0.png")
path = r"D:\ucloud\Multi\Projekt_2\finished_material\paintbrush"

images2 = [os.path.join(path, im) for im in os.listdir(path) if ".png" in im]
c = 0
for image2 in images2:
    img_f = copy.deepcopy(image1)
    img = Image.open(image2)
    print(c)
    # Get the width and height of the images
    width, height = img_f.size
    
    # Iterate over each pixel in the image
    for x in range(width):
        for y in range(height):
            # Get the pixel at the current location
            pixel = img_f.getpixel((x, y))
    
            # Check if the pixel has the desired color
            if pixel[:3] == (29, 161, 242):  # blue
                # Replace the pixel with the corresponding pixel from the second image
                img_f.putpixel((x, y), img.getpixel((x, y)))
    
    # Save the modified image
    img_f.save(rf"D:\ucloud\Multi\Projekt_2\finished_material\paintbrush_finished\paintbrush_{str(c)}.png")
    c += 1
    img_f.close()