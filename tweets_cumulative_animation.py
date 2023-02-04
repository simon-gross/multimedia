import os
import glob
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from PIL import Image
import json
from datetime import datetime as dt

##### VARIABLES #####
seconds = 40
frames = 8

dpi_num = 72
breite = 4096 * 1.325
länge = 2048 * 1.325

x = (-20037508.34, 20037508.34)
y = (-10018754.17, 10018754.17)

out = r"D:\ucloud\Multi\Projekt_2\finished_material_kapitel2\tweets_cumulative_animation"


n = frames*seconds
rishi = gpd.read_file("data/rishi.shp").set_crs(4326).sort_values("Timestamp")
rishi = rishi.to_crs(32662)
rishi.Timestamp = rishi.Timestamp.apply(lambda x: dt.strptime(x, "%Y-%m-%dT%H:%M:%S.000Z"))

start = rishi.Timestamp.min()
end = rishi.Timestamp.max()


anzahl_pro_sub = len(rishi)//n

start = len(rishi)//n

for i in range(0, n):
    i += 1
    if i == n:
        sub = rishi
    else:
        sub = rishi.head(i*start)
    
    fig, ax = plt.subplots(1, figsize=(breite/dpi_num, länge/dpi_num), dpi=dpi_num, frameon=False)
    plt.xlim(x)
    plt.ylim(y)
    
    plt.axis('off')
    
    # sub.plot(ax=ax, marker="o", color="yellow", markersize=5, alpha=1)
    # sub.plot(ax=ax, marker="o", color="yellow", markersize=10, alpha=0.8)
    # sub.plot(ax=ax, marker="o", color="yellow", markersize=20, alpha=0.5)
    sub.plot(ax=ax, marker="o", color="yellow", markersize=20, alpha=0.3)
    
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(os.path.join(out, f"points_{i-1}.png"), bbox_inches=extent)
    
    plt.close(fig)
    # if i == 1:
    #     break