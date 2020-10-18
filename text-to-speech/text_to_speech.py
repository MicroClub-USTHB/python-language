#First we need to import the libraries we will be using
import pyttsx3
import PyPDF2

#Open your pdf file in read binary format
_file = open('test.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(_file)
pages = pdfReader.numPages

speaker = pyttsx3.init()  #creating a new engine
print("Engine up and running")

#Setting voice property
eng_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
speaker.setProperty('voice', eng_voice)

#Change some other properties
speaker.setProperty('rate', 150)  #Set reading rate or speed
speaker.setProperty('volume', 0.6) # Set volume: float between 0 and 1

for num in range(0, pages):   #The first argument represents the page number at which it will start reading
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)   #Queues a command to speak content of file
    speaker.runAndWait()
