# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 13:17:06 2022

@author: Simsi_Arbeit
"""
import os
import numpy as np
from PIL import Image


def update_pics(path):
    imgs = [os.path.join(path, im) for im in os.listdir(path) if ".png" in im]


    c = 0
    for i, bild in enumerate(imgs):
        print(i)
        img = Image.open(bild)
        na = np.array(img)
        
        # row, col
        print(na.shape[1])
        if na.shape[1] == 4097:
            na = na[:, :4096, :]
            
            img = Image.fromarray(na)
            img.save(bild)

if __name__ == "__main__":
    path = r"D:\ucloud\Multi\Projekt_2\finished_material_kapitel2\tweets_cumulative_animation"
    update_pics(path)