import os
import glob
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


borders = gpd.read_file("data/ne_110m_admin_0_countries_lakes/ne_110m_admin_0_countries_lakes.shp").to_crs(32662)
dpi_num = 72
breite = 4096 * 1.325
länge = 2048 * 1.325
size = 3
out = r"C:\Users\Simsi_Arbeit\Desktop\Uni\ucloud\Multi\Projekt\data\countries_ani"
out = "D:/"

west_usa = -13803616.856444445
borders['nearest_x'] = borders.geometry.apply(lambda x: x.bounds[0])

def temp(x):
    if x.nearest_x < west_usa:
        return x.nearest_x + 40075016.68
    else:
        return x.nearest_x
    
borders['nearest_x'] = borders.apply(temp, axis=1)


borders = borders.sort_values('nearest_x')

reihenfolge = borders.index.tolist()

x = (-20037508.34, 20037508.34)
y = (-10018754.17, 10018754.17)


c = 0
frame = borders.boundary
sam = gpd.GeoDataFrame(borders.loc[4]).T
while True:
    c += 1
        
    
    fig, ax = plt.subplots(1, figsize=(breite/dpi_num, länge/dpi_num), dpi=dpi_num, frameon=False)
    plt.xlim(x)
    plt.ylim(y)
    
    plt.axis('off')
    # for item in [fig, ax]:
    #     item.patch.set_visible(False)
    
    frame.plot(ax=ax, color="#6E6E6E", linewidth=1)
    if len(reihenfolge) < size:
        new_sam = reihenfolge
        idx = reihenfolge
        sam = sam.append(borders.loc[idx])
        reihenfolge = []
        
    else:
        new_sam = reihenfolge[:size]
        idx = new_sam
        sam = sam.append(borders.loc[idx])
        del reihenfolge[:size]
        
    sam.plot(ax=ax, color="#1DA1F2", edgecolor="#6E6E6E", linewidth=1)
    print(idx)
    
    
    s = str(c)
    # if len(s) == 1:
    #     s = '00' + s
    # if len(s) == 2:
    #     s = '0' + s
        
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(os.path.join(out, f"test.png"), bbox_inches=extent)
    
    if len(reihenfolge) == 0:
        break
    
    if c == 1:
        break
    
    plt.close(fig)
    
    
fig, ax = plt.subplots(1, figsize=(breite/dpi_num, länge/dpi_num), dpi=dpi_num, frameon=False)
plt.xlim(x)
plt.ylim(y)

plt.axis('off')
# for item in [fig, ax]:
#     item.patch.set_visible(False)

sam = gpd.GeoDataFrame(borders.loc[4]).T

frame.plot(ax=ax, color="#6E6E6E", linewidth=1)
sam.plot(ax=ax, color="#1DA1F2", edgecolor="#6E6E6E", linewidth=1)

s = "0"
    
extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig(os.path.join(out, f"pop_up_{s}.png"), bbox_inches=extent)

plt.close(fig)
    
# fp_in = os.path.join(out, "*test.png")
# fp_out = os.path.join(out, "ani2.gif")

# imgs = (Image.open(f) for f in sorted(glob.glob(fp_in)))
# img = next(imgs)  # extract first image from iterator
# img.save(fp=fp_out, format='GIF', append_images=imgs,
#          save_all=True, duration=40, loop=0)

# Zuerst alle einfärben, dann blending, die in grau wo twitter verboten ist!!