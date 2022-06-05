#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests
import spacy
import re
import string
import read_input_data as rid
import tiger_tokenizer
import tiger_lemmatizer
import tiger_manage_tokens as tmt
import tiger_visualizations as visual
import tiger_tagger as tag
import tiger_sentiment_analysis as sa
import tiger_vector_generation_for_clustering as vg
from collections import Counter
from spacy.tokens import Doc

# step 1: load data from file
data_file = open("dummyData.txt","r")

# step 2: create dictionary out of all the characteristic features (tokens or words) 
# of the documents collection

# step 2.1 : tokenization
data_to_tokenize = rid.all_answers(data_file)
data_file.close()
doc_tokenization = tiger_tokenizer.tokenization_process(data_to_tokenize)

# step 2.2 : Lemmatization
doc_lemmatization = tiger_lemmatizer.lemmatization_process(doc_tokenization)

# step 2.3 : create dictionary/hashtable that contains the dictionary words
dictionary = vg.create_dictionary_frequencies(doc_lemmatization)
#print(dictionary)
which_docs = vg.create_which_document(doc_lemmatization)
#print(which_docs)

# step 3 : create a spreadsheet of numeric data corresponding
# to the document collection
data_file = open("dummyData.txt","r")
vg.create_spreadsheet(data_file,which_docs)
data_file.close()


# In[ ]:




