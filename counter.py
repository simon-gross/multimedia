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
länge = 1024
breite = 1024

x = (-1, 1)
y = (0, 10000)

out = r"D:\ucloud\Multi\Projekt_2\finished_material_kapitel2\counter"


n = frames*seconds
rishi = gpd.read_file("data/rishi.shp").set_crs(4326).sort_values("Timestamp")
rishi.Timestamp = rishi.Timestamp.apply(lambda x: dt.strptime(x, "%Y-%m-%dT%H:%M:%S.000Z"))

start = rishi.Timestamp.min()
end = rishi.Timestamp.max()


anzahl_pro_sub = len(rishi)//n

start = len(rishi)//n

for i in range(0, n):
    i += 1
    
    fig, ax = plt.subplots(1, figsize=(breite/dpi_num, länge/dpi_num), dpi=dpi_num, facecolor='gray')
    ax.set_title('Number of Tweets', size=70, color='white')
    ax.set_facecolor("gray")
    
    ax.tick_params(axis='both', which='major', labelsize=40, colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.xaxis.label.set_color('red')
    #ax.tick_params(axis='x', colors='red')

    plt.xlim(x)
    plt.ylim(y)
    
    ax.bar(0, i*start, width=1, color="yellow", edgecolor='black')
    plt.text(0, i*start+200, str(i*start), size=50, horizontalalignment='center', color='white')
    
    ax.set_xticks([])
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)

    

    fig.savefig(os.path.join(out, f"counter_{i-1}.png"), transparent=True)
    
    plt.close(fig)
    # if i == 1:
    #     break