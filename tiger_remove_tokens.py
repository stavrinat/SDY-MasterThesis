#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8
# using encoding='utf8'
# reference : https://realpython.com/natural-language-processing-spacy-python/

import json
import requests
import spacy
import re
import string
import unicodedata
import tiger_manage_tokens as tmt
import tiger_more_stopwords as stop
from collections import Counter
from spacy.tokens import Doc

nlpGR = spacy.load("el")
nlpEN = spacy.load("en")

#https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-normalize-in-a-python-unicode-string
# function strip_accents was taken from the above link
def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def remove_stopwords_stripping_accents(doc):
    # 1. go to our stop words, remove all accents and create a list with these non-accented words
    stopwords_without_accents = [strip_accents(s) for s in stop.STOP_WORDS]
    # 2. create a new list after the elimination of non-accented words
    items_without_stopwords = [token.text for token in doc if token.text not in stopwords_without_accents]
    doc_without_stopwords = nlpGR(tmt.list_to_string(items_without_stopwords))
    return doc_without_stopwords

def remove_white_numbers_symbols(doc):
    #print("number of tokens before removing whitespaces, numbers and symbols : ",len(tmt.extract_tokens(doc)))
    items_only_words = [token.text for token in doc if token.text.isalpha() == True and token.text not in string.whitespace and token.text.isdigit() == False and token.text not in string.punctuation]
    doc_only_words = nlpGR(tmt.list_to_string(items_only_words))
    return doc_only_words

#Stop words are the most common words in a language
#the below function removes stop words from
# the tokens list
#remove stop words and punctuation symbols
def remove_stop_words(data):
    # 1. calculating all stop words: spacy's stop words + our stop words
    stopwords = stop.STOP_WORDS
    # 2. removing Greek stop words, white characters, numbers and symbols
    file_doc = remove_white_numbers_symbols(nlpGR(data))
    #print("number of tokens after removing whitespaces, numbers and symbols and before removing stopwords: ",len(tmt.extract_tokens(file_doc)))
    items_without_stopwords = [token.text for token in file_doc if not token.is_stop and token.text not in stopwords and not token.is_punct]   
    #print("number of tokens after removing the Greek stopwords : ",len(items_without_stopwords))

    # 3. removing English/GreekGlish stop words
    data = tmt.list_to_string(items_without_stopwords)
    file_doc = nlpEN(data)
    items_without_stopwords = [token.text for token in file_doc if not token.is_stop and not token.is_punct]   
    #print("number of tokens after removing the English stopwords : ",len(items_without_stopwords))

    
    # 4. creating final doc without stopwords
    doc_without_stopwords = nlpGR(tmt.list_to_string(items_without_stopwords))
    #print("number of tokens after removing stopwords and every non relevant string : ",len(items_without_stopwords))
    #print("tokens after removing the stopwords : ")
    #tmt.print_tokens(doc_without_stopwords)
    return doc_without_stopwords

