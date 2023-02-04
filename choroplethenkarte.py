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

csv = r"C:\Users\Simsi_Arbeit\Desktop\Uni\ucloud\Multi\Projekt\data\ne_110m_admin_0_countries_lakes\nst-est2019-01.csv"
out = r"C:\Users\Simsi_Arbeit\Desktop\Uni\ucloud\Multi\Projekt\finished_material_kapitel3\map"
usa = r"C:\Users\Simsi_Arbeit\Desktop\Uni\ucloud\Multi\Projekt\data\ne_110m_admin_0_countries_lakes\cb_2018_us_state_500k.shp"

csv = pd.read_csv(csv, sep=";", header=None)
temp = csv.columns.tolist()
temp[0] = 'State'
csv.columns = temp
csv['State'] = csv['State'].apply(lambda x: x[1:])


midterms = gpd.read_file("data/midterms.shp").set_crs(4326)
#midterms = midterms.to_crs(32662)
midterms.Timestamp = midterms.Timestamp.apply(lambda x: dt.strptime(x, "%Y-%m-%dT%H:%M:%S.000Z"))


#### USA ####
usa = gpd.read_file(usa).set_crs(4269).to_crs(4326).rename(columns={'NAME': 'State'})

midterms = gpd.clip(midterms, usa)

usa = usa.merge(csv, on='State')
usa = usa.rename(columns={12: "population"})
usa.population = usa.population.apply(lambda x: x.replace(".", "")).astype(int)

usa = usa[['State', 'population', 'geometry']]

def _count(poly):
    count = len(gpd.clip(midterms, poly))
    return count

usa['counts'] = usa.geometry.apply(_count)
usa['counts_rel'] = usa.counts * 1000000 / usa.population
usa = usa.to_crs(32662)

fig, ax = plt.subplots(1, figsize=(breite/dpi_num, länge/dpi_num), dpi=dpi_num, frameon=False)
plt.xlim(x)
plt.ylim(y)
plt.axis('off')

usa.plot(column='counts_rel', scheme="quantiles", k=5, ax=ax, cmap="OrRd",\
         edgecolor="#6E6E6E", linewidth=1)
extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
fig.savefig(os.path.join(out, "choroplethen.png"), bbox_inches=extent)