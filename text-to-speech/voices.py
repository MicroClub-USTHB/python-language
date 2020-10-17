#This code lets you select the voice of your choice which you can then include in the main code
#The available voices depend on each PC
#You can add more voices by downloading the package in your settings

import pyttsx3

speaker = pyttsx3.init()

voices = speaker.getProperty('voices') 
  
for voice in voices: 
    #Get the info about the voices in your PC  
    print("Voice:") 
    print("ID: %s" %voice.id) 
    print("Name: %s" %voice.name) 
    print("Age: %s" %voice.age) 
    print("Gender: %s" %voice.gender) 
    print("Languages Known: %s" %voice.languages) 

#For example, I get:
'''Voice:
ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0
Name: Microsoft Hortense Desktop - French
Age: None
Gender: None
Languages Known: []
Voice:
ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
Name: Microsoft Zira Desktop - English (United States)
Age: None
Gender: None
Languages Known: []
Voice:
ID: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
Name: Microsoft David Desktop - English (United States)
Age: None
Gender: None
Languages Known: []'''

#I choose one ID corresponding to the voice I want to use, 
# and I'm gonna add it to my main text-to-speech program