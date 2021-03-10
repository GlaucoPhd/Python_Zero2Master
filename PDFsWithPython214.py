# PDF is a Binary file and to read it we use rb
# Count number of pages
import PyPDF2

# Tell how many pages its on the PDF
# with open('twopage.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)

# Tell all the objects it has the PDF
# with open('twopage.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.getPage(1))

# Rotate use a with inside of a with
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('Rotate.pdf', 'wb') as new_file:
        writer.write(new_file)

