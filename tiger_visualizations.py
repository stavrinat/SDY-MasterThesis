#!/usr/bin/env python

# using encoding='utf8'
# reference : https://realpython.com/natural-language-processing-spacy-python/
# reference : https://plotly.com/python/basic-charts/

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
from termcolor import colored



def colors_and_sizes(elements):
    colors = []
    sizes = []
    for i in range(1,elements+1):
        colors.append(i*5)
    sizes = list(reversed(colors))
    return colors,sizes

# reference: https://plotly.com/python/colorscales/
# reference: https://plotly.com/python/bar-charts/
# bar chart
def visualization_frequency_1(word_freq,word):
    # simple graph           
    #fig = go.Figure(data=go.Bar(x=word[:10],y=word_freq[:10]))
    #fig.show()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=word[:10],y=word_freq[:10],text=word_freq,textposition='outside'))
    
    fig.update_traces(marker_color='aqua', marker_line_color='darkmagenta',
                  marker_line_width=2)
    
    fig.update_layout(
        title = dict(text = "Οι 10 συχνότεροι όροι στις απαντήσεις των χρηστών", font = dict(size=20,color='darkmagenta',family='Georgia')),
        xaxis = dict(title_text = "Συχνότερα εμφανιζόμενοι όροι/λέξεις", titlefont = dict(size=20,color='darkmagenta',family='Georgia')),
        yaxis = dict(title_text = "Συχνότητα εμφάνισης όρων/λέξεων",titlefont = dict(size=20,color='darkmagenta',family='Georgia')), 
        plot_bgcolor = "lemonchiffon",title_x=0.35)
    
    fig.show()
    

# bubble chart
def visualization_frequency_2(word_freq,word):
    colors,sizes = colors_and_sizes(15)
    fig = go.Figure(data=[go.Scatter(x=word[:15], y=word_freq[:15],mode='markers',
    marker=dict(
        color = word_freq,
        colorscale = 'Viridis',
        size = sizes,
        showscale = True,
        reversescale = True
        ))])
    
    fig.update_layout(
        title = dict(text = "Οι 15 συχνότεροι όροι στις απαντήσεις των χρηστών", font = dict(size=20,color='darkmagenta',family='Georgia')),
        xaxis = dict(title_text = "Συχνότερα εμφανιζόμενοι όροι/λέξεις", titlefont = dict(size=20,color='darkmagenta',family='Georgia')),
        yaxis = dict(title_text = "Συχνότητα εμφάνισης όρων/λέξεων",titlefont = dict(size=20,color='darkmagenta',family='Georgia')), 
        plot_bgcolor = "lemonchiffon",title_x=0.35)
    
    fig.show()


# reference: https://plotly.com/python/gauge-charts/
def gauge_chart_for_each_emotion(e_label, e_value,e_color):
    title_text = 'Percentage of '+ e_label + ' that is depicted in the user\'s answers \n \n'

    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = e_value,
    mode = "gauge+number+delta",
    title = {'text':e_label,'font': {'color': e_color,'size': 30}},
    gauge = {'axis': {'range': [0, 100],'tickwidth': 3, 'tickcolor': "black"},
             'bar': {'color': e_color},
             'steps' : [
                 {'range': [0, 50], 'color': "lightgray"},
                 {'range': [50, 100], 'color': "gray"}],
             'threshold' : {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': e_value}}))
    fig.update_layout(title = title_text,title_x = 0.50,titlefont = {'color': "darkblue", 'family': "Georgia", 'size':22},paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Georgia", 'size':18})

    fig.show()

def visualization_for_sentiment_analysis_per_emotion(emotions):
    colors = ['tomato', 'yellowgreen', 'cadetblue', 'mediumspringgreen','cornflowerblue','gold']
    labels = [k for k in emotions.keys()]
    values = [emotions[k] for k in emotions.keys()]
    
    # gauge charts for each emotion
    for i in  range(len(labels)):
        gauge_chart_for_each_emotion(labels[i],values[i],colors[i])

# reference https://github.com/mnpinto/jupyter_tutorials/blob/master/code_with_emojis.ipynb
def visualization_for_sentiment_analysis_polarity(polarity):
    colors = ['goldenrod', 'darkorchid', 'navy', 'firebrick']
    labels = ['Neutral','Both','Negative','Positive']
    values = [polarity[k] for k in polarity.keys()]
    
    # emojis for polarity displace
    pol_emojis = pd.DataFrame({'Answers vibe': ('😐 🤔 ☹️ 😊').split(' '),
                     'Percentage': values})
  
    for i in range(len(values)):
        labels[i] = str(round(values[i],2)) + "% " + labels[i]
        
    fig = px.bar(pol_emojis, x='Answers vibe', y='Percentage',color_discrete_sequence = colors,
            color =labels, width=750, height=850, text = values)
    fig.update_xaxes(title_text='Polarity', tickfont=dict(size=50))
    fig.update_traces(texttemplate='%{text:.4s}', textposition='outside')
    fig.update_layout(title_text='Polarity of user\'s answers', title_x=0.35, plot_bgcolor = "lemonchiffon")
    fig.update_traces( marker_line_color='black',
                  marker_line_width=1.5)
    fig.show()

    
def visualization_for_sentiment_analysis_emotions_a(emotions):
    colors = ['red', 'purple', 'orange', 'green','blue','yellow']
    labels = [k for k in emotions.keys()]
    values = [emotions[k] for k in emotions.keys()]
    
    # donut pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values,hole=.3, textinfo='label+percent',
                             insidetextorientation='horizontal'
                            )])
    fig.update_traces(textfont_size=14,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig.update_layout(title_text = "Percentage of each emotion, in total of all user's answers" )
    fig.show()
    
    

def visualization_for_sentiment_analysis_emotions_b(emotions):
    colors = ['red', 'purple', 'orange', 'green','blue','yellow']
    sort_emotions ={k:v for k,v in sorted(emotions.items(), key=lambda x: x[1], reverse=True)}
    labels = [k for k in sort_emotions.keys()]
    values = [emotions[k] for k in sort_emotions.keys()]
        
    # funel chart
    # although funnel chart do not usual being used 
    # for sentiment analysis
    # percents are presenting rounded to ceil
    fig = go.Figure(go.Funnel(
    y = labels,
    x = values,
    textposition = "inside",
    textinfo = "percent total",
    textfont = {"family": "Old Standard TT, serif", "size": 18},
    opacity = 1, marker = {"color": ["darkgreen","seagreen", "limegreen", "springgreen", "palegreen", "mintcream"],
    "line": {"width": [3, 2.5, 2, 1.5, 1, 1], "color": ["darkorange", "darkorange", "darkorange", "darkorange", "darkorange","darkorange"]}},
    connector = {"line": {"color": "darkorange", "dash": "solid", "width": 3}},)
    )

    fig.update_layout(
    title = {"text":"Percentage of each emotion,from most prevailed emotion to lowest prevailed emotion ,in total of all user's answers","font":{"family": "Old Standard TT, serif", "size": 18}})
    fig.show()

    
