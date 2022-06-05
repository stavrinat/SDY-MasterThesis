#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

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


# that scenario was the beginning scenario that was
# reading from the actual url file

# step 1: load data from url
data_from_url = rid.load_data_from_url("http://codemix.gr/athsense/gettextualdata.php")
#print(data_from_url)

# step 2: Tokenization
data_to_tokenize = rid.all_answers_question4(data_from_url)
doc_tokenization = tiger_tokenizer.tokenization_process(data_to_tokenize)

# step 3: Lemmatization
doc_lemmatization = tiger_lemmatizer.lemmatization_process(doc_tokenization)
#print(tmt.print_tokens(doc_lemmatization))

# step : tagger
#doc_tagger = tag.tagging_process(doc_lemmatization)

# step 4: sentiment analysis
#emotions = sa.sentiment_analysis_process2(doc_lemmatization)
#print(emotions)

# step 5: Find frequency of words
#word_freq = visual.word_frequency(doc_lemmatization)
#print(type(word_freq))
# step 5: Sort words according to their frequency
#sort_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
#dict_word_freq = dict(sort_word_freq)
#word_freq,word = visual.most_frequent(dict_word_freq)

# step 6: visualize text mining data, using various techniques
#visual.visualization1(word_freq,word)
#visual.visualization2(word_freq,word)
visual.visualization_for_sentiment_analysis_1(emotions)



