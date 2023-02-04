# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:33:29 2022

@author: Simsi_Arbeit
"""

import os
from PIL import Image


##### VARBIABLE ASSIGNMENT #####
file = r"D:\ucloud\Multi\Projekt_2\finished_material_kapitel3\map\legend_map_2.png"
out = r"D:\ucloud\Multi\Projekt_2\finished_material_kapitel3\legend_blend_out"
out_name = "legend_blend_out"
reverse = True
frames = 25


r = range(frames)
if reverse:
    r = range(frames-1, -1, -1)
    
img = Image.open(file)#.convert('RGBA')
datas = img.getdata()



c = 0
for i in r:
    alpha = int(round(255/frames, 0) * i)
    print(alpha)
    new = []
    for i, data in enumerate(datas):
        if len(data) < 3:
            data = (data[0], data[1], data[2], alpha)
        
        if data[3] != 0:
            data = (data[0], data[1], data[2], alpha)
            new.append(data)
        else:
            new.append(data)
        
    img.putdata(new)
    
    img.save(os.path.join(out, out_name + "_" + str(c) + ".png"))
    c += 1

