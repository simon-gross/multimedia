# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:13:58 2022

@author: Simsi_Arbeit
"""

import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

borders = gpd.read_file("data/ne_110m_admin_0_countries_lakes/ne_110m_admin_0_countries_lakes.shp").to_crs(32662)

dpi_num = 72
breite = 4096 * 1.325
länge = 2048 * 1.325
size = 2
x = (-20037508.34, 20037508.34)
y = (-10018754.17, 10018754.17)
out = r"C:\Users\Simsi_Arbeit\Desktop\Uni\ucloud\Multi\Projekt\finished_material\forbidden_blending_animation2"


verboten = ["China", "Iran", "Myanmar", "North Korea", "Russia", "Uzbekistan", "Turkmenistan"]

borders['verboten'] = borders.NAME.isin(verboten)
verboten = borders[borders.NAME.isin(verboten)]

fig, ax = plt.subplots(1, figsize=(breite/dpi_num, länge/dpi_num), dpi=dpi_num, frameon=False)
plt.xlim(x)
plt.ylim(y)

plt.axis('off')
for item in [fig, ax]:
    item.patch.set_visible(False)

verboten.plot(ax=ax, color="#636363", edgecolor="#6E6E6E", linewidth=1)
borders[borders['verboten'] != True].plot(ax=ax, color="#1DA1F2", edgecolor="#6E6E6E", linewidth=1)

extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig(os.path.join(out, "verboten.png"), bbox_inches=extent)