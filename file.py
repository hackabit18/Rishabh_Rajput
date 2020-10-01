from flask import Flask, render_template, request
import pickle
import numpy as np #for matrix
import os
import glob
import skimage.io as io
from skimage.transform import rescale, resize
import skimage.color as co
from werkzeug import secure_filename





app = Flask(__name__)

#ml implementation

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
    ip_dir = "static/images"
    ip_file = glob.glob(os.path.join(ip_dir,"*"))
    img = io.imread(ip_file[-1])
    img1 = co.rgb2hsv(resize(img, (32,32,3),anti_aliasing=False))
    ip_np_arr = np.reshape(img1,(1,32*32*3))
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    class_num = loaded_model.predict(ip_np_arr)
    class_text = name_of_monument(int(class_num))
    return class_text

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
  
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join("static/images",secure_filename(f.filename)))
      final_text = predict_monument()
      if final_text == "Unlabelled":
        return "The image is not a monument! :("
      else:
        return "The monument is "+final_text+"."
    
if __name__ == '__main__':
   app.run(debug = True)
