import os
from PIL import Image
import numpy as np

pic2 = r"D:\ucloud\Multi\Projekt_2\finished_material_kapitel3\map\legend_map_2.png"
pic1 = r"D:\ucloud\Multi\Projekt_2\finished_material_kapitel3\map\legend_swings_2.png"
out = r"D:\ucloud\Multi\Projekt_2\finished_material_kapitel3\legend_sliding"
frames = 50

#pic1 = Image.new("RGBA", (4096, 4096))
pic1 = Image.open(pic1)
pic2 = Image.open(pic2)

na2 = np.array(pic2)
na1 = np.array(pic1)



if not na1.shape == na2.shape:
    raise ValueError('Images do not have the same size!')

counter = 0
for i in range(frames):
    size = na1.shape[1]
    border = (size // frames) * (i+1)
    if i == frames-1:
        border = size
        
    a = na1[:, :border, :]
    b = na2[:, border:, :]
    
    current_pic = np.hstack([a, b])
    
    img = Image.fromarray(current_pic)
    img.save(os.path.join(out, f"legend_sliding_{str(counter)}.png"))
    counter+=1
    
    # if i == round(frames*0.33):
    #     break