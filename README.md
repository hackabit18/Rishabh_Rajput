# Rishabh_Rajput
## ToGIV(Tool to Give every Image a Voice)
# Introduction
We ideate an image to text and image to audio platform that makes possible the decoding of images for social and entrepreneurial benefits. We seek to develop an end to end application with an accompanying API which takes any image as input and using a CNN-RNN architecture returns accurate captions and descriptions for the image.
Our main lines of ideas to develop a proof of concept demonstrating a use case include-
a) Developing a categorizing tool which takes an image input and returns a description of the monument if the image classifies as a well known monument of India and gives a generic caption for the image otherwise. 
 A further extension of this is a assistance tool for blind people which enables them to gain a description place through automatic audio description of a captured image using Computer and NLP. We will use image caption generator model to generate a caption for a given image and further generate audio output from text.
b) A product that automatically generates captions for social media websites like Instagram, Tumblr, Pintrest etc instead of manually captioning images, ensuring the image's content remains intact while saving time as well. The quality of text output will be dramatically improved to optimise for easy information sharing and vitality by fine tuning the model using scraped image-caption pairs from social media platforms.
In the future, it can aid news/media companies to deal with high volume image scanning or high document inflow by developing a tool for image captioning.
Install dependencies

`pip3 install flask flask-uploads flask-dropzone`
`pip3

and run

`export FLASK_APP=app.py`

`flask run`
