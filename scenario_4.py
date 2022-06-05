#!/usr/bin/env python
# coding: utf-8

# In[1]:


# using encoding='utf8'
# reference : https://realpython.com/natural-language-processing-spacy-python/
# reference : https://plotly.com/python/basic-charts/

import json
import requests
import spacy
import re
import string
import read_input_data as rid
import tiger_tokenizer
import tiger_lemmatizer
import tiger_manage_tokens as tmt
import tiger_visualizations_geo as geo
import tiger_tagger as tag
import tiger_sentiment_analysis as sa
from collections import Counter
from spacy.tokens import Doc


# step 1: load data from url
data_file = open("dummyData.txt","r")
answers = rid.dict_of_all_answers_and_emotions(data_file)
#print(answers)
data_file.close()

for key in answers:

    # step 2: Tokenization
    data_to_tokenize = answers[key][0]
    doc_tokenization = tiger_tokenizer.tokenization_process(data_to_tokenize)

    # step 3: Lemmatization
    doc_lemmatization = tiger_lemmatizer.lemmatization_process(doc_tokenization)
    #print(tmt.print_tokens(doc_lemmatization))

    # step 4: sentiment analysis
    answers[key][0] = doc_lemmatization
    sa.sentiment_analysis_process3(answers[key])
    #print(answers[key])
    
geo.visualization_google_map(answers)
#geo.visualization_scatter_plot(answers)
#geo.visualization_map(answers)


# In[ ]:





# In[ ]:




