# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:25:52 2022

@author: Simsi_Arbeit
"""

import os
import geopandas as gpd
import matplotlib.pyplot as plt
from PIL import Image


borders = gpd.read_file("data/ne_110m_admin_0_countries_lakes/ne_110m_admin_0_countries_lakes.shp").to_crs(32662)
out = r"C:\Users\Simsi_Arbeit\Desktop\Uni\ucloud\Multi\Projekt\data\countries_ani"

dpi_num = 72
breite = 4096 * 1.325
länge = 2048 * 1.325
x = (-20037508.34, 20037508.34)
y = (-10018754.17, 10018754.17)

frame = borders.boundary


fig, ax = plt.subplots(1, figsize=(breite/dpi_num, länge/dpi_num), dpi=dpi_num, frameon=False)
plt.xlim(x)
plt.ylim(y)

ax.set_facecolor("#1D2224")

borders.plot(ax=ax, color="#818E9D")
frame.plot(ax=ax, color="#6E6E6E", linewidth=1)

extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig(os.path.join(out, "background.png"), bbox_inches=extent)


# plt.axis('off')