import pickle
import numpy as np
import os
import glob
import skimage.io as io
from skimage.transform import rescale, resize
import skimage.color as co


def zero():
    ret_text = "Unlabelled"
    return ret_text

def one():
    ret_text = "Charminar"
    return ret_text
 
def two():
    ret_text = "Gateway of India"
    return ret_text
 
def three():
    ret_text = "Golden Temple"
    return ret_text
 
def four():
    ret_text = "Gol Gumbaz"
    return ret_text
 
def five():
    ret_text = "Hawa Mahal"
    return ret_text
 
def six():
    ret_text = "Humayon's Tomb"
    return ret_text
 
def seven():
    ret_text = "India Gate"
    return ret_text
 
def eight():
    ret_text = "Lotus Temple"
    return ret_text
 
def nine():
    ret_text = "Qutub Minar"
    return ret_text

def ten():
    ret_text = "Rashtrapati Bhavan"
    return ret_text
 
def eleven():
    ret_text = "Red Fort"
    return ret_text
 
def twelve():
    ret_text = "Sanchi Stupa"
    return ret_text

def thirteen():
    ret_text = "Se Cathedral"
    return ret_text

def fourteen():
    ret_text = "Taj Mahal"
    return ret_text
 
def name_of_monument(argument):
    switcher = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve,
        13: thirteen,
        14: fourteen
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid output!")
    # Execute the function
    return func

def predict_monument():
    ip_dir = "initial"
    ip_file = glob.glob(os.path.join(ip_dir,"cat*"))
    img = io.imread(ip_file[0])
    img1 = co.rgb2hsv(resize(img, (128,128,3),anti_aliasing=False))
    ip_np_arr = np.reshape(img1,(128*128*3))
    pkl_filename = "random_forest_classifier.pkl"
    with open(pkl_filename, 'rb') as file:  
        pickle_model = pickle.load(file)
    class_num = pickle_model.predict(ip_np_arr)
    class_text = name_of_monument(int(class_num))
    return class_text

predict_monument()