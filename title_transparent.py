# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:08:42 2022

@author: Simsi_Arbeit
"""

# 2 Sekunden von 0 auf 100
from PIL import Image
import os


path = r"C:\Users\Simsi_Arbeit\Downloads\K_1_S_1_Title_Frames\K_1_S_1_Title_Frames\K_1_S_1_Title_Frame"

imgs = [os.path.join(path, im) for im in os.listdir(path)]
c = 0
for i, bild in enumerate(imgs):
    # if (i - 1) % 2 == 0:
    #     continue
    img = Image.open(bild)
    
    rgba = img.convert("RGBA")
    datas = rgba.getdata()
    
    newData = []
    
    for item in datas:
    
       if item[0] == 0 and item[1] == 0 and item[2] == 0:
    
           newData.append((255, 255, 255, 0))
       else:
    
          newData.append(item)

    rgba.putdata(newData)
    rgba.save(r"C:\Users\Simsi_Arbeit\Desktop\Uni\ucloud\Multi\Projekt\finished_material\title_typewriter\intro_text_animation_{}.png".format(c), "PNG")
    print("saved")
    c += 1