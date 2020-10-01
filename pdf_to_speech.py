#importing necessary libraries
import pyttsx3
import PyPDF2

#importing the pdf
book = open('filename.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

#speech command
speaker = pyttsx3.init()
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()