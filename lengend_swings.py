import os
import glob
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from PIL import Image
import json
from datetime import datetime as dt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe

out = r"D:\ucloud\Multi\Projekt_2\finished_material_kapitel3\map"
# x = (-20037508.34, 20037508.34)
# y = (-10018754.17, 10018754.17)

dpi_num = 72
länge = 4096 
breite = 4096
blue = "#011993"

fig, ax = plt.subplots(1, figsize=(breite/dpi_num, länge/dpi_num), dpi=dpi_num, frameon=False)
# plt.xlim(x)
# plt.ylim(y)
plt.axis('off')

d = {1: ('Republican', "#E9141D"),
     2: ('Democrat', "#0015BC"),
     3: ('Battleground States', "purple"),
     4: ('No open Senat Seat', "gray")}

labs = ["Republican", "Democrat", "Battleground\nStates", "No open\nSenat Seat"]
cols = ["#E9141D", "#0015BC", "purple", "gray"]

patches = [mpatches.Patch(color=col, label=lab, path_effects=[pe.withStroke(linewidth=15, foreground="white")]) for col, lab in zip(cols, labs)]

#, bbox_to_anchor =(0.17,0.61)
l = plt.legend(handles=patches, prop= {'size': 300}, \
           title='Party\nAffiliation', title_fontsize=300, framealpha=0, loc="upper left")
    
plt.setp(l.get_title(), multialignment='center', path_effects=[pe.withStroke(linewidth=15, foreground="white")])
l.get_title().set_color(blue)
for text in l.get_texts():
    text.set_color(blue)
    text.set_path_effects(path_effects=[pe.withStroke(linewidth=15, foreground="white")])

#extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig(os.path.join(out, "legend_swings_2.png"))
