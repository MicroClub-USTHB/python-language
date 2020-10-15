#First we need to import the libraries we will be using
import pyttsx3
import PyPDF2

#Open your pdf file in read binary format
_file = open('test.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(_file)
pages = pdfReader.numPages

speaker = pyttsx3.init()  #creating a new engine
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)   #Queues a command to speak content of file
    speaker.runAndWait()
