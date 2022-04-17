import pdfminer
##remember to install pdfminer.
import collections
import pandas as p
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import matplotlib
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


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
    print(wordsFiltered)
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
    return()

#arraycreator()
#wordarray=wordstripper(arraycreator())


#mostcommon100(wordstripper(arraycreator()))
#mostcommon100(arraycreator())
#entirefilter(arraycreator())

def wordwriter(bsid, wordarray):
    df = p.read_csv('wordcount.csv')
    #print(df)
    #print(df)
    if bsid in df.bsid.values:
        print('bsid already created')
    else:
        df2 = p.DataFrame.from_dict(collections.Counter(wordarray),orient='index').reset_index()
        df2 = df2.rename(columns={'index':'word',0:'count'})
        print(df2)
        #add bsid onto it
        #print(df)
        df2['bsid'] = bsid
        #df2 = p.concat([df2,df], axis=1)
        df2=df.append(df2,ignore_index=True)
        df2.to_csv('wordcount.csv')
        print('Added length  to dataframe')

wordwriter(103,arraycreator())
#index,word,count,bsid

#print(collections.Counter(arraycreator()))

