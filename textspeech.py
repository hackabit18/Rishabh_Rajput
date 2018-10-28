from gtts import gTTS 
import os 
  
mytext = 'text to speak'
language = 'en'  
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("file.mp3") 

os.system("mpg321 file.mp3") 




