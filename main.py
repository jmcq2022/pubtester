import pdfminer
##remember to install pdfminer.
import collections

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
#print(output_string.getvalue())
string = output_string.getvalue()


#figuring out how to count each word
arr = [ x.strip() for x in string.strip().split(' ') ]

#print (arr)
#print (arr.count('the'))
x = len(arr)
#print(x)
i=0
n = len(arr)
# function to count

print(collections.Counter(arr).most_common(100))




#while i < len(arr):

##formula is below,
#pt = companies trustworthyness . persons trustworthniess . countries trusthworthiness(lenght of report/average report length for similar firms . (buzzwords/paragraph + amount of esg information / total length of report + pictures/total words))

#things to need to be done
#Length of report
#Buzzword counter
#total paragraphs
#total amount of ESG buzzwords
#Total amount of words
#total number of pics
#total number of words