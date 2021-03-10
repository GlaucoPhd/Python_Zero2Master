import PyPDF2
import sys


a_inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
        merger.write('agoras.pdf')


pdf_combiner(a_inputs)
