# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:34:30 2022

@author: Simsi_Arbeit
"""

from shapely.geometry import Polygon
import geopandas as gpd


def create_bbox(coords):
    coords = coords['geo']['bbox']
    x_min, y_min, x_max, y_max = coords
        
    polygon_tuples = [
        (x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)
    ]
    
    polygon = Polygon(polygon_tuples)
    
    centroid = polygon.centroid
    
    return centroid


def make_gdf(df):
    gdf = gpd.GeoDataFrame(df, geometry='geom')
    gdf = gdf.set_crs('EPSG:4326')
    gdf.Timestamp = gdf.Timestamp.astype(str)
    gdf = gdf.drop(columns=['Referenced Tweets'])
    return gdf
    print(gdf.crs)