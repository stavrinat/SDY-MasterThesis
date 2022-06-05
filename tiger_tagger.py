#!/usr/bin/env python
# coding: utf-8


#https://spacy.io/api/tagger

import spacy
from spacy.lang.el import Greek

nlpGR = Greek()

def tagging_process(doc):
    for token in doc:
        print('Token:{}, POS tag: {}'.format(token,token.tag_))

