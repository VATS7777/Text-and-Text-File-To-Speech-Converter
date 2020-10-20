# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
text_write = 'hello,how are you my name is Vatsal'
  
# Language we want to use 
language = 'en'
  

myobj = gTTS(text=text_write, lang=language, slow=False) 
  

myobj.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3")