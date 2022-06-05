#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import requests
import spacy
import re
import string
import random
from collections import Counter
from spacy.tokens import Doc


def load_data_from_url(data_url):
    response = requests.get(data_url)
    #data = response.json()
    data = json.loads(response.text)
    return data

def all_answers(data_file):
    answers = ""
    with data_file:
        content = data_file.readlines()
    for ans in content:
        a = ans.replace("\"","")
        a = a.replace("\n","")
        a = a.split(":")
        answers = answers + a[1].replace(",","")+" "
    return answers

def dict_of_all_answers_and_emotions(data_file):
    # generate random latitude and longtitude
    start_long= 23.68478
    stop_long = 23.78956
    start_lat = 37.93908
    stop_lat = 38.01979 
    
    answers = {}
    with data_file:
        content = data_file.readlines()
    for ans in content:
        a = ans.replace("\"","")
        a = a.split(":")
        
        # each users answer is put into a dictionary
        # where each entry consists of:
        # key: serial number of the answer (eg 1, 2, 3, .... etc)
        # value: a list that is a vector and contains:
        # the answer of the user and 6 integers, one for each possible emotion:
        # anger, disgust, fear, happiness, sadness, surprise
        latitude = random.uniform(start_lat, stop_lat)
        longitude = random.uniform(start_long, stop_long)
        answers[int(a[0])] = [a[1].replace(",","").rstrip(),0,0,0,0,0,0,latitude,longitude]
    return answers

def dict_of_all_answers_only(data_file):
    answers = {}
    with data_file:
        content = data_file.readlines()
    for ans in content:
        a = ans.replace("\"","")
        a = a.split(":")
        answers[int(a[0])] = a[1].replace(",","").rstrip()
    return answers

def all_answers_question4(data):
    question4 = ""
    for user in data: 
        question4 = question4+data[user]['question4']+" "
    return question4

