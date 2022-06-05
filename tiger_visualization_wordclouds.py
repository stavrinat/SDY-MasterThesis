# using encoding='utf8'
# reference : https://realpython.com/natural-language-processing-spacy-python/
# reference : https://amueller.github.io/word_cloud/auto_examples/index.html#example-gallery

import json
import requests
import spacy
import re
import plotly.graph_objects as go
import plotly.express as px
import string
import tiger_manage_tokens as tmt
import pandas as pd
import numpy as np
from collections import Counter
from spacy.tokens import Doc
from spacy import displacy
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import random
from PIL import Image

    
# reference: https://www.datacamp.com/community/tutorials/wordcloud-python
def visualization_wordcloud_simple(text,title):
    # Create and generate a word cloud image:
    wordcloud = WordCloud(max_font_size=70,background_color="white").generate(text)

    # Display the generated image:
    #plt.title(title) # when I put title for some reason a x-y axis empty graph appears
    plt.figure(figsize=[7,7])
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


# reference: https://www.datacamp.com/community/tutorials/wordcloud-python
def visualization_wordcloud_mask(text,title):
    
    cat_mask = np.array(Image.open( "cat.png"))
    
    # Create and generate a word cloud image:
    wordcloud =WordCloud(max_font_size=70,background_color="white",contour_width=1, contour_color='darkmagenta',mask=cat_mask).generate(text)
    
    # Display the generated image:
    plt.figure(figsize=[10,10])
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

# reference: https://amueller.github.io/word_cloud/auto_examples/single_word.html#
def visualization_wordcloud_singleWord(text,title):
    x, y = np.ogrid[:700, :700]

    mask = (x - 350) ** 2 + (y - 350) ** 2 > 330 ** 2
    mask = 255 * mask.astype(int)


    wc = WordCloud(background_color="white", repeat=True, mask=mask)
    wc.generate(text)

    plt.figure(figsize=[7,7])
    plt.axis("off")
    plt.title(title)
    plt.imshow(wc, interpolation="bilinear")
    plt.show()
    
    
# reference: https://www.datacamp.com/community/tutorials/wordcloud-python
def visualization_wordcloud_word_limit(text,limit):
    # Create and generate a word cloud image:
    wordcloud = WordCloud(max_font_size=100, max_words=limit, background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    