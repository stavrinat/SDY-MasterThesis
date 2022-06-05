
#!/usr/bin/env python
# coding: utf-8
# using encoding='utf8'
# reference : https://realpython.com/natural-language-processing-spacy-python/


import json
import requests
import spacy
import re
import string
from collections import Counter
from spacy.tokens import Doc
from difflib import SequenceMatcher

nlpGR = spacy.load("el")
nlpEN = spacy.load("en")


def extract_tokens(doc):
    tokens = [token.text for token in doc]
    return tokens

def print_tokens(doc):
    for token in doc:
        print(token, token.idx , token.pos_)
        
def print_tokens_lemmas(doc):
    for token in doc:
        print(token,token.lemma_)

def list_to_string(lst):
    str_all = ""
    for s in lst:
        str_all += s+" "
    return str_all

def dict_to_list_values(dictionary):
    return list(dictionary.values())

def dict_to_list_keys(dictionary):
    return list(dictionary.keys())

def doc_to_string(doc):
    tokens = [token.text for token in doc]
    s = list_to_string(tokens)
    return s    

#https://stackoverflow.com/questions/17388213/find-the-similarity-metric-between-two-strings
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def same_starting_letter(token, dictionary):
    pref = token.text[0]
    res = {key:val for key, val in dictionary.items()  
                   if key.startswith(pref)} 
    return res
    
    
def find_if_similar_key_exists(token,dictionary):
    more_similar = "none" 
    similarity_degree = 0 # maximum similarity degree 
    
    # 1. find the already existing keys that start with the same letter as the token
    # so to reduce time of the find_similar procedure
    starting_letter = same_starting_letter(token, dictionary)
    for key in starting_letter.keys():
        # 2. find similarity degree between token and k
        check = similar(token.text,key)
        # 3. if that degree is greater than the for-the-time-being 
        # maximum similarity degree then store that as
        # maximum degree and the corresponding index
        if(check >= 0.80 and check > similarity_degree):
            similarity_degree = check
            more_similar = key
    return more_similar
    
# check if two strings are over 0.85 similar (because they might not appear exactly the 
# same in greek_sentiment_lexicon for example όμορφος & ομορφιά
# find_similar() examines all possible terms in the lexicon
# to find if there is an identical term or a term with the same stem
# return the most index of the most similar term if such a term exists
def find_similar(token, dictionary):
    more_similar = 0 # index of most similar term
    similarity_degree = 0 # maximum similarity degree 
    
    # 1. find the terms/rows that start with the same letter as the token
    # so to reduce time of the find_similar procedure
    starting_letter = same_starting_letter(token, dictionary)
    for k in starting_letter.keys():
        # 2. find similarity degree between token and k
        check = similar(token.text,k)
        # 3. if that degree is greater than the for-the-time-being 
        # maximum similarity degree then store that as
        # maximum degree and the corresponding index
        if(check >= 0.80 and check > similarity_degree):
            similarity_degree = check
            more_similar = dictionary[k]
    return more_similar

def get_key(val,my_dict): 
    for key, value in my_dict.items(): 
         if val == value: 
            return key 
  
    return "key doesn't exist"
