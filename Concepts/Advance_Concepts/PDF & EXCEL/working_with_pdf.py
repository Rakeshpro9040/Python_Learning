import os
import PyPDF2

os.system('cls')
print(os.getcwd())

# Step-1 Open a File
f = open('.//Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)

# Some Operations
print(pdf_reader.numPages) # Count page number

# Get Text from Page-1
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
# print(page_one_text)
f.close()

# Wtite to a PDF
f = open('.//Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
page_one = pdf_reader.getPage(0)
print(type(page_one))
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_one)
pdf_output = open('.//Some_BrandNew_Doc.pdf','wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()
