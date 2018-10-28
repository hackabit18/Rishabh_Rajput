# Rishabh_Rajput
## ToGIV(Tool to Give every Image a Voice)
# The idea
We ideate an image to text and image to audio platform that makes possible the decoding of images for social and entrepreneurial benefits. We seek to develop an end to end application with an accompanying API which takes any image as input and using Random Forest Classifier, classifies it as a monument and then uses a CNN-RNN architecture returns accurate captions and descriptions for the image, if it is not a monument detected by the classifier.

# Tools and technologies

**Our main lines of ideas to develop a proof of concept demonstrating a use case include**:-
* a) Developing a categorizing tool which takes an image input and returns a description of the monument if the image classifies as a well known monument of India and gives a generic caption for the image otherwise. 
 A further extension of this is a assistance tool for blind people which enables them to gain a description place through automatic audio description of a captured image using Computer Vision and NLP. We will use image caption generator model to generate a caption for a given image and further generate audio output from text.
 
* b) A product that automatically generates captions for social media websites like Instagram, Tumblr, Pintrest etc instead of manually captioning images, ensuring the image's content remains intact while saving time as well. The quality of text output will be dramatically improved to optimise for easy information sharing and vitality by fine tuning the model using scraped image-caption pairs from social media platforms.

In the future, it can aid news/media companies to deal with high volume image scanning or high document inflow by developing a tool for image captioning.

### Tools and Technologies used:

* for Web Implementation : **HTML**, **CSS** **Flask(Web Framework written in Python)**, **gtts python library(For text to speech)**

* for Caption Generation : **Keras**, **TensorFlow**, **ScikitLearn**, **Anaconda(tool)**


# Run the program

### Install dependencies

`pip3 install flask`

`pip3 install pickle`

`pip3 install numpy`

`pip3 install os`

`pip3 install glob`

`pip3 install skimage`

`pip3 install werkzeug`

and run

`python3 file.py`

Currently, one part of the project classifies only 14 monuments in India, displays its name and generates a simple caption for any unidentified/unlabelled image.
Other part gives a suitable caption suggestion on giving an image's URL as input.

### Future Scope

1. In the future, if trained extensively, the proposed model can process images in bulk and help generate caption and basic descriptions for large media and social media companies as they have a daily input of thousands of images.
2. The model can be made an android app which will generate caption on the go helpful for blind people, and geolocation can be used to help them go safely to their destination.
