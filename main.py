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

from nltk.corpus import stopwords
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


def arraycreator():
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
    #print(string)
    #I can remove all values here
    stopwords = nltk.corpus.stopwords.words('english')
    #Add some aditional stopwords
    newstopwords = ['the','and']
    stopwords.extend(newstopwords)
    print(stopwords)
    for i in newstopwords:
        stopwords.append(i)
    print(stopwords)
    words = word_tokenize(string)
    wordsFiltered = []
    for w in words:
        if w not in stopwords:
            wordsFiltered.append(w)
           # print(w)
    #print(wordsFiltered)
    print(type(words))
    print(type(string))
    return words

def wordstripper(wordarray):
    arr = [x.strip() for x in wordarray.strip().split(' ')]
    return arr

def mostcommon100(wordarray):
    print(collections.Counter(wordarray).most_common(100))

#arraycreator()
#wordarray=wordstripper(arraycreator())
#s=set(stopwords.words('english'))

#mostcommon100(wordstripper(arraycreator()))
mostcommon100(arraycreator())



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