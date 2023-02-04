"""
Created on Wed Jan 11 21:08:46 2023

@author: Simsi_Arbeit
"""



import os

folder = r"D:\ucloud\Multi\Projekt_2\test_export"

import re




for filename in os.listdir(folder):
    if filename.startswith("image_"):
        new_filename = re.sub(r"image_0*", "image_", filename)
        print(new_filename)
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))
