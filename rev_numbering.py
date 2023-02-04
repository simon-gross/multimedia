# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:55:36 2022

@author: Simsi_Arbeit
"""

import os

folder = r"D:/ucloud/Multi/Projekt_2/finished_material_kapitel4/live_blink"
#out = r"C:/Users\Simsi_Arbeit\Desktop\Uni\ucloud\Multi\Projekt\finished_material\forbidden_fade_in"


numbers = []
d = {}

for file in os.listdir(folder):
    temp = file.split("_")[-1]
    temp = temp.split(".")[0]
    numbers.append(int(temp))
    
    d[file] = int(temp)
    
numbers = sorted(numbers)
numbers.reverse()

for key, value in d.items():
    v = numbers[value-25]
    
    d[key] = [value, v]
    
for key, val in d.items():
    
    out_name = "_"+ key.split("_"+str(val[0]))[0] + "_" + str(val[1]) + ".png"
    
    os.renames(os.path.join(folder, key), os.path.join(folder, out_name))
    
    #d.values() = reversed(d.values())
    
for key, val in d.items():
    out_name = "_"+ key.split("_"+str(val[0]))[0] + "_" + str(val[1]) + ".png"
    os.renames(os.path.join(folder, out_name), os.path.join(folder, out_name[1:]))