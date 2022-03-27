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
    #String is created, then ensured its lower case
    string = output_string.getvalue()
    string = string.lower()
    #I can remove all values here
    #This builds out the default stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    #Add some aditional stopwords
    newstopwords = ['the','and',',','.','(',')','''''',':','’','The',';']
    stopwords.extend(newstopwords)
    for i in newstopwords:
        stopwords.append(i)
    #this tokenizes the words + creates my filter
    words = word_tokenize(string)
    wordsFiltered = []
    for w in words:
        if w not in stopwords:
            wordsFiltered.append(w)
    #Returns my Words filtered
    return wordsFiltered


#wordstripper isn't needed if the wordsfiltered is used, as it outputs as a nice list i think
def wordstripper(wordarray):
    arr = [x.strip() for x in wordarray.strip().split(' ')]
    return arr

#This just shows me most common 250 words of an array
def mostcommon100(wordarray):
    print(collections.Counter(wordarray).most_common(250))

def entirefilter(wordarray):
    print(collections.Counter(wordarray))

#arraycreator()
#wordarray=wordstripper(arraycreator())
#s=set(stopwords.words('english'))

#mostcommon100(wordstripper(arraycreator()))
#mostcommon100(arraycreator())
entirefilter(arraycreator())


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