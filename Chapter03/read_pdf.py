import PyPDF2
from PyPDF2 import PdfFileReader

#Get the reader object to read PDF files
pdf = open("diveintopython.pdf", 'rb')
readerObj = PdfFileReader(pdf)
print "PDF Reader Object is:\n", readerObj

#Get Details of diveintopython book
print "Details of diveintopython book"
print "Number of pages", readerObj.getNumPages()
print "Title:", readerObj.getDocumentInfo().title
print "Author:", readerObj.getDocumentInfo().author

#Read outline of a PDF file with Reader object
print "Book Outline"
for heading in readerObj.getOutlines():
    if type(heading) is not list:
        print dict(heading).get('/Title')

#Read given page of the PDF file
print "Reading Page 1"
page = readerObj.getPage(1)
print page.extractText()

pdf.close()
