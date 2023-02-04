# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:09:51 2022

@author: Simsi_Arbeit
"""

import os

folder = r"D:\ucloud\Multi\Projekt_2\finished_material_kapitel2\zeitrahl_raw"
locator = "zeitstrahl"

fns = []
files = os.listdir(folder)

for i, file in enumerate(files):
    
    new = locator + "_" + str(i) + ".png"
    os.rename(os.path.join(folder, file), os.path.join(folder, new))