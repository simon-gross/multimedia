import os
import glob
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from PIL import Image
import json
from datetime import datetime as dt



##### VARIABLES #####

x = (-20037508.34, 20037508.34)
y = (-10018754.17, 10018754.17)

dpi_num = 72
breite = 4096 * 1.325
länge = 2048 * 1.325

out = r"C:\Users\Simsi_Arbeit\Desktop\Uni\ucloud\Multi\Projekt\finished_material_kapitel3\map"
usa = r"C:\Users\Simsi_Arbeit\Desktop\Uni\ucloud\Multi\Projekt\data\ne_110m_admin_0_countries_lakes\cb_2018_us_state_500k.shp"
usa = gpd.read_file(usa).set_crs(4269)
usa = usa.to_crs(32662)
swings = ["Arizona", "Georgia", "Michigan", "Nevada", "Pennsylvania", "Wisconsin"]
d = {1: ('Republican', "#E9141D"),
     2: ('Democrat', "#0015BC"),
     3: ('Battleground States', "purple"),
     4: ('No open Senat Seat', "gray")}
usa['swing'] = states = [4,1,1,4,4,1,3,4,1,1,4,2,4,4,1,4,2,1,3,3,1,2,1,4,4,2,1,1,3,2,2,4,1,1,2,3,4,4,4,4,2,4,2,4,4,4,4,1,3,3,2,1,1,1,4,2]
usa.party = usa.swing.apply(lambda x: d[x][0])
usa.col = usa.swing.apply(lambda x: d[x][1])

fig, ax = plt.subplots(1, figsize=(breite/dpi_num, länge/dpi_num), dpi=dpi_num, frameon=False)
plt.xlim(x)
plt.ylim(y)
plt.axis('off')


usa.plot(column='swing', ax=ax, color=usa.col, edgecolor="#6E6E6E", linewidth=1)


extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig(os.path.join(out, "swing_states.png"), bbox_inches=extent)