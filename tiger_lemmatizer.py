
# using encoding='utf8'
# reference : https://realpython.com/natural-language-processing-spacy-python/
# reference : https://plotly.com/python/basic-charts/

import json
import requests
import spacy
import re
import string
import tiger_manage_tokens as tmt
import tiger_remove_tokens as rmv
from collections import Counter
from spacy.tokens import Doc

nlpGR = spacy.load("el")
nlpEN = spacy.load("en")

#'''
# reference: https://realpython.com/natural-language-processing-spacy-python/#lemmatization
#Lemmatization is the process of
#reducing inflected forms of a word while still
#ensuring that the reduced form belongs to the language.
#This reduced form or root word is called a lemma.
#For example, organizes, organized and organizing are
#all forms of organize. Here, organize is the lemma.
#'''
def lemmatization_process(doc):
    # 1. create a list with all lemmas that exists in our tokenization doc
    #all_lemmas = [token.lemma_ for token in doc]
    all_lemmas = []
    for token in doc:
        if len(all_lemmas)== 0:
            all_lemmas.append(token.lemma_)
        else:
            added = False
            for l in all_lemmas:
                if tmt.similar(rmv.strip_accents(l).lower(), rmv.strip_accents(token.lemma_).lower())>=0.85:
                    all_lemmas.append(l)
                    added = True
                    break
            if added == False:
                all_lemmas.append(token.lemma_)

    # 2. create a Doc object from the above list
    doc_with_lemmas = nlpGR(tmt.list_to_string(all_lemmas))    
    
    # 3. using the standard procedure to remove stopwords, spaces, numbers, white characters, etc
    doc_with_lemmas = rmv.remove_stop_words(tmt.doc_to_string(doc_with_lemmas))   
    
    # 4. second round of removing stopwords, because many users write words without the proper
    # accent , but the stopwords remain stopwords even without accent so they must be removed
    doc_with_lemmas = rmv.remove_stopwords_stripping_accents(doc_with_lemmas)
    #print("tokens after lemmatization:")
    #tmt.print_tokens_lemmas(doc_with_lemmas)
    #doc_with_lemmas = Doc(nlpGR.vocab, words = all_lemmas)
    return doc_with_lemmas