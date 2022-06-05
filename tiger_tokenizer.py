#!/usr/bin/env python
# coding: utf-8
# using encoding='utf8'
# reference : https://realpython.com/natural-language-processing-spacy-python/

import json
import requests
import spacy
import re
import string
import tiger_manage_tokens as tmt
import tiger_more_stopwords as stop
import tiger_remove_tokens as rmv
from collections import Counter
from spacy.tokens import Doc

nlpGR = spacy.load("el")
nlpEN = spacy.load("en")


#Tokenization is the next step after sentence detection.
#It allows you to identify the basic units in your text.
#These basic units are called tokens. Tokenization is useful
#because it breaks a text into meaningful units.
#These units are used for further analysis, like part of speech tagging.
def tokenization_process(data):
    doc_without_stopwords = rmv.remove_stop_words(data)
    return doc_without_stopwords