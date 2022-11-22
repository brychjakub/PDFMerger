import os
from PyPDF2 import PdfMerger


pdfs = [a for a in os.listdir() if a.endswith(".pdf")]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("mergedPdf.pdf")
merger.close()