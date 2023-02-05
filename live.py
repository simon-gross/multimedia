import os
import numpy as np
import pandas as pd
import geopandas as gpd
import streaming
import html
import matplotlib.pyplot as plt
import remove_pixel
from PIL import Image
import tweepy as tw
# import matplotlib.patheffects as pe
from datetime import datetime
from matplotlib.patches import Rectangle

dpi_num = 72
breite = 4096 * 1.325
länge = 2048 * 1.325

x = (-20037508.34, 20037508.34)
y = (-10018754.17, 10018754.17)

out = r".\live"

API_KEY = 'F08q1o4skqkiR0nuR2YnILSob'
API_KEY_SECRET = 'HHjitrVhnmQ3BViLsIVZpGKQfzJo45jAbBnVEaGq2Ra14Rmo8E'

access_token = "1237766974589014022-z5qD33nrfRmDV5FPdrquHtE1uouMqB"
access_token_secret = "Rcv41dBaU1ipImj0nXjHjwvJNatnGdaD5Jhq9KOawcRUK"


def set_gdf(tweets):
    new_tweets = []
    
    for tweet in tweets:
        _tweet = {}
        _tweet['text'] = tweet['text']
        if tweet['geo'] is not None:
            _tweet['coords'] = tweet['geo']['coordinates']
        else:
            four_coords = tweet['place']['bounding_box']['coordinates'][0]
            y = [c[0] for c in four_coords]
            x = [c[1] for c in four_coords]
            #return x, y
            center = sum(x)/len(x), sum(y)/len(y)

            _tweet['coords'] = center
        _tweet['timestamp'] = tweet['created_at']
        new_tweets.append(_tweet)
    
    df = pd.DataFrame(data=[html.unescape(tweet['text']) for tweet in tweets], columns=['Text'])
    df['lat'] = np.array([tweet['coords'][0] for tweet in new_tweets])
    df['lon'] = np.array([tweet['coords'][1] for tweet in new_tweets])
    df['timestamp'] = np.array([tweet['timestamp'] for tweet in new_tweets])
    
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat, crs=4326))
    gdf = gdf.to_crs(32662)
    
    return gdf

def plot_live_tweets(gdf, material_name):
    fig, ax = plt.subplots(1, figsize=(breite/dpi_num, länge/dpi_num), dpi=dpi_num, frameon=False)
    plt.xlim(x)
    plt.ylim(y)
    
    plt.axis('off')
    
    gdf.plot(ax=ax, marker="o", color="red", markersize=100, edgecolors='black')
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(os.path.join(out, f"{material_name}.png"), bbox_inches=extent)
    
    breite2 = 2048 * 1.2905
    länge2 = 1024 * 1.325

    fig, ax = plt.subplots(1, figsize=(breite2/dpi_num, länge2/dpi_num), dpi=dpi_num, frameon=False)
    plt.xlim(x)
    plt.ylim(y)
    
    plt.axis('off')
    
    texts = [gdf.Text[0].strip(), gdf.Text[1].strip(), gdf.Text[2].strip()]
    
    for i, text in enumerate(texts):
        if len(text) >= 50:
            texts[i] = text[:50] + "..."
    
    # Tweet Time
    now = datetime.now()
    time = now.strftime("%d/%m/%Y, %H:%M:%S")
    plt.text(0.8*x[0], 0.3*y[1], "Last tweets since: ".upper() + time, fontsize=70)
    
    rect = Rectangle((0.85*x[0], 0.35*y[0]), 1.68*x[1], 0.85*y[1], facecolor='gray',\
                     edgecolor='black', linewidth=8)

    # Add the rectangle to the axis
    ax.add_patch(rect)
    
    border = "\n--------------------------------------------------------------------------"
    # Tweet Text
    plt.text(0.8*x[0], 0.05*y[1], texts[0]+border, color="black", fontsize=50)
    
    # Tweet Text 2
    plt.text(0.8*x[0], 0.15*y[0], texts[1]+border, color="black", fontsize=50)
    
    # Tweet Text 3
    plt.text(0.8*x[0], 0.25*y[0], texts[2], color="black", fontsize=50)
    
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(os.path.join(out, f"{material_name}_material2.png"), bbox_inches=extent)
    
    
    remove_pixel.update_pics(out)
    
def transform_to_dds(path, material_folder, material_name, c):
    img = Image.open(os.path.join(path, f"{material_name}.png"))
    img.compression = 'dtx1a'
    img.save(fp=os.path.join(material_folder, f"{material_name}.dds"))
    
def get_api():
    auth = streaming.TweepyTwitterAuthenticator().authenticate_twitter_app()
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth)
    return api
    
def send_outro_tweet():
    api = get_api()
    
    username = "simsi79141326"
    status = "Mulitmedia is Fun!"
    api.update_status(status=status, place_id="07d9e3a1cac85002")
    
def plot_outro_tweet(material_folder, material_name):
    api = get_api()
    outro = [api.user_timeline()[0]._json]
    # return outro
    
    gdf = set_gdf(outro)
    fig, ax = plt.subplots(1, figsize=(breite/dpi_num, länge/dpi_num), dpi=dpi_num, frameon=False)
    plt.xlim(x)
    plt.ylim(y)
    
    plt.axis('off')
    
    plt.text(gdf.geometry.x+100000, gdf.geometry.y-800000, "Our Position", fontsize=100, color='white')
    
    gdf.plot(ax=ax, marker="x", color="green", markersize=600, edgecolors='black')
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(os.path.join(out, f"{material_name}.png"), bbox_inches=extent)
    fig.close()
    
    remove_pixel.update_pics(out+"/outro")
    
    
    
    
    transform_to_dds(out, material_folder, material_name.split("/")[-1])
    
    transform_to_dds(out, material_folder, material_name.split("/")[-1]+"_material2")

if __name__ == '__main__':

    material_folder = r"C:\Users\Simsi_Arbeit\Documents\OmniSuite_media\materials\textures\11\test_update\test"
    material_name = "current_tweets"
    all_tweets = []
    
    c = 10
    twitter_streamer = streaming.TweepyTwitterStreamer(time_limit=3)
    while True:
        print("Getting Tweets")
        hash_tag_list = [""]
        
        
        tweets = twitter_streamer.stream_tweets(hash_tag_list, filter=False)
        
        gdf = set_gdf(tweets)
        #gdf = gpd.read_file("D:/temp.shp")
        plot_live_tweets(gdf, material_name)
        
        transform_to_dds(out, material_folder, material_name+"_material2", c)
        transform_to_dds(out, material_folder, material_name, c)
        
        # c += 1
        # if c == 14:
        #     break