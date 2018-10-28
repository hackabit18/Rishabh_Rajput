import pickle
import numpy as np
import os
import glob
import skimage.io as io
from skimage.transform import rescale, resize
import skimage.color as co

def name_of_monument(argument):
    switcher = {
        0: "Unlabelled",
        1: "Charminar",
        2: "Gateway of India",
        3: "Golden Temple",
        4: "Gol Gumbaz",
        5: "Hawa Mahal",
        6: "Humayon's Tomb",
        7: "India Gate",
        8: "Lotus Temple",
        9: "Qutub Minar",
        10: "Rashtrapati Bhavan",
        11: "Red Fort",
        12: "Sanchi Stupa",
        13: "Se Cathedral",
        14: "Taj Mahal"
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid output!")
    # Execute the function
    return func

def predict_monument():
    ip_dir = "initial"
    ip_file = glob.glob(os.path.join(ip_dir,"*"))
    img = io.imread(ip_file[0])
    img1 = co.rgb2hsv(resize(img, (32,32,3),anti_aliasing=False))
    ip_np_arr = np.reshape(img1,(1,32*32*3))
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    class_num = loaded_model.predict(ip_np_arr)
    class_text = name_of_monument(int(class_num))
    return class_text

print(predict_monument())
