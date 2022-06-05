#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python

# using encoding='utf8'
# reference : https://realpython.com/natural-language-processing-spacy-python/
# reference : https://plotly.com/python/basic-charts/

import json
import requests
import spacy
import re
import gmplot 
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

#https://www.geeksforgeeks.org/python-plotting-google-map-using-gmplot-package/
def visualization_google_map(data):
    latitude = []
    longitude = []
    colors = []
    
    for key in data:
        latitude.append(data[key][7])
        longitude.append(data[key][8])
        if data[key][1] == data[key][2] == data[key][3] == data[key][4] == data[key][5] == data[key][6] == 0:
            colors.append('pink')
        elif data[key][1] == 1:
            colors.append('red')
        elif data[key][2] == 1:
            colors.append('purple')
        elif data[key][3] == 1:
            colors.append('orange')
        elif data[key][4] == 1:
            colors.append('green')
        elif data[key][5] == 1:
            colors.append('blue')
        elif data[key][6] == 1:
            colors.append('yellow')
        
            
    gmap = gmplot.GoogleMapPlotter(38.01979, 23.78956, 12) 

    # scatter method of map object 
    # scatter points on the google map 
    gmap.scatter( latitude, longitude, colors, size = 25, marker = True ) 
    
    # tried to put api key from google but it didn't work
    # error "cannot load mpla mpla" kept appearing
    #gmap.apikey='AIzaSyAFHSoN7AVLj6PTdAZzXLiE_WeOAAetaC4'

    gmap.draw( "C:\\Users\\user\\Desktop\\mapTiger.html" ) 

# scatter plot chart
# using each user's answer and location
def visualization_scatter_plot(data):
    
    latitude = []
    longitude = []
    colors = []
    
    for key in data:
        latitude.append(data[key][7])
        longitude.append(data[key][8])
        if data[key][1] == data[key][2] == data[key][3] == data[key][4] == data[key][5] == data[key][6] == 0:
            colors.append('pink')
        elif data[key][1] == 1:
            colors.append('black')
        elif data[key][2] == 1:
            colors.append('purple')
        elif data[key][3] == 1:
            colors.append('orange')
        elif data[key][4] == 1:
            colors.append('green')
        elif data[key][5] == 1:
            colors.append('blue')
        elif data[key][6] == 1:
            colors.append('yellow')
        
      
    
    fig = go.Figure(data=go.Scatter(
    x = longitude,
    y = latitude,
        mode='markers',
    marker=dict(color=colors)
    ))
   
    fig.update_traces(mode='markers', marker_line_width=1, marker_size=20)
    fig.update_layout(title_text="Τοποθεσία χρηστών και απεικόνιση επικρατέστερου συναισθήματος καθενός/καθεμιάς", title_x=0.50, titlefont = {'color': "darkblue", 'family': "Georgia", 'size':22},plot_bgcolor = "cyan",
        xaxis = dict(title_text = "Longitude of users", titlefont = dict(size=20,color='darkmagenta',family='Georgia')),
        yaxis = dict(title_text = "Latitude of users",titlefont = dict(size=20,color='darkmagenta',family='Georgia')),
                     legend=dict(
        title_font_family="Times New Roman",
        font=dict(
            family="Courier",
            size=12,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=2
    ))

    fig.show()

def visualization_map(data):
    latitude = []
    longitude = []
    colors = []

    for key in data:
        latitude.append(data[key][7])
        longitude.append(data[key][8])
        if data[key][1] == data[key][2] == data[key][3] == data[key][4] == data[key][5] == data[key][6] == 0:
            colors.append('pink')
        elif data[key][1] == 1:
            colors.append('red')
        elif data[key][2] == 1:
            colors.append('purple')
        elif data[key][3] == 1:
            colors.append('orange')
        elif data[key][4] == 1:
            colors.append('green')
        elif data[key][5] == 1:
            colors.append('blue')
        elif data[key][6] == 1:
            colors.append('yellow')
        
    print(colors)
    fig = px.scatter_mapbox(lat=latitude, lon=longitude,
        color_discrete_sequence=colors, zoom=11, height=1000)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":1,"t":2,"l":2,"b":1})
    fig.show()
        

