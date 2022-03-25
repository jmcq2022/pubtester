import pdfminer
##remember to install pdfminer.

from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()
with open('02488082.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
      interpreter.process_page(page)
print(output_string.getvalue())


##formula is below,
#pt = companies trustworthyness . persons trustworthniess . countries trusthworthiness(lenght of report/average report length for similar firms . (buzzwords/paragraph + amount of esg information / total length of report + pictures/total words))