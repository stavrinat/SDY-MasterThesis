#!/usr/bin/env python
# coding: utf-8

from collections import Counter
import tiger_manage_tokens as tmt

def word_frequency(doc):
    word_freq = Counter(tmt.extract_tokens(doc))
    return word_freq

def words_and_frequencies_separate(word_frequency):
    word_freq = tmt.dict_to_list_values(word_frequency)
    word = tmt.dict_to_list_keys(word_frequency)
    return word_freq,word

def sort_according_to__frequency(doc):
    # step 1: Find frequency of words
    word_freq = word_frequency(doc)

    # step 2: Sort words according to their frequency
    sort_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    dict_word_freq = dict(sort_word_freq)
    word_freq,sorted_words = words_and_frequencies_separate(dict_word_freq)
    
    return word_freq,sorted_words

def text_depending_on_frequency(word_freq,sorted_words,max_words):
    max_words_text = ""
    for i in range(max_words):
        #for j in range(word_freq[i]):
            max_words_text += " "+sorted_words[i]
    
    return max_words_text