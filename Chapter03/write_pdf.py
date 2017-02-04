import PyPDF2

#Open a PDF file and add a blank page to it
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
infile = PdfFileReader(open('Exercise.pdf', 'rb'))
outfile = PdfFileWriter()
outfile.addBlankPage(612, 792)
p = infile.getPage(0)
outfile.addPage(p)
with open('myPdf.pdf', 'wb') as f:
        outfile.write(f)
f.close()


#Add a new page to a PDF file and add a table with certain text
import fpdf
from fpdf import FPDF
pdf = FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome to Automate It!", ln=1, align="C")
pdf.cell(200,10,'Created by Chetan',0,1,'C')
pdf.output("automateit.pdf")

#Merge mutiple PDF files to one PDF file
from PyPDF2 import PdfFileReader, PdfFileMerger
import os
merger = PdfFileMerger()
files = [x for x in os.listdir('.') if x.endswith('.pdf')]
for fname in sorted(files):
    merger.append(PdfFileReader(open(os.path.join('.', fname), 'rb')))
merger.write("output.pdf")


#Create a PDF file and manage header and footer across pages
from fpdf import FPDF
class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Automate It!', 1, 0, 'C')
        self.ln(20)

pdf = PDF(format='A5')
pdf.add_page()
pdf.set_font("Times", size=12)
for i in range(1, 50):
    pdf.cell(0, 10, "This my new line. line number is: %s" % i, ln=1, align='C')
pdf.output("header_footer.pdf")
