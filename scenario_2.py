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
import tiger_visualizations as visual
import tiger_tagger as tag
import tiger_sentiment_analysis as sa
from collections import Counter
from spacy.tokens import Doc


# step 1: load data from file
data_file = open("dummyData.txt","r")

# step 2: Tokenization
data_to_tokenize = rid.all_answers(data_file)
data_file.close()
doc_tokenization = tiger_tokenizer.tokenization_process(data_to_tokenize)

# step 3: Lemmatization
doc_lemmatization = tiger_lemmatizer.lemmatization_process(doc_tokenization)
#print(tmt.print_tokens(doc_lemmatization))

# step 4: sentiment analysis
emotions,polarity = sa.sentiment_analysis_process2(doc_lemmatization)
#print(emotions)


# step 5: visualize text mining data, using various techniques
visual.visualization_for_sentiment_analysis_emotions_a(emotions)
visual.visualization_for_sentiment_analysis_emotions_b(emotions)


# In[ ]:





# In[ ]:




