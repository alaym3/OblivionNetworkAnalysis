import streamlit as st
import os
import re
import json
import scipy
import numpy as np
import pandas as pd
from tabulate import tabulate
import plotly.express as px
from collections import Counter


pd.options.plotting.backend = "plotly"


import matplotlib.pyplot as plt
import seaborn as sns
# sns.set_style("whitegrid")

import networkx as nx
import urllib.request
from tqdm.auto import tqdm

import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer
tokenizer = WordPunctTokenizer()
lemmatizer = WordNetLemmatizer()
stopwords = nltk.corpus.stopwords.words('english')
from nltk import sentiment
from nltk.sentiment import vader
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import PlaintextCorpusReader
from nltk.probability import FreqDist 
from nltk import word_tokenize
from wordcloud import WordCloud
from PIL import Image
from functions import *

#### 1st step always: make layout wider #####
st.set_page_config(layout="wide", page_title="Oblivion character analysis")

# set title and description
st.title('Analysis of all characters in Elder Scrolls IV: Oblivion')
st.markdown('### This website shows a breakdown of all of the attributes of characters in Oblivion. Next we analyze each character compared to their relations to other characters and explore the network of characters.')


# race
fig = create_attribute_plot('race', 900, 500)
update_standard_bar_plot(fig)
update_title(fig,25)
st.plotly_chart(fig,use_container_width=True)


# organize into columns
col1, col2 = st.columns(2)

with col1:
    # gender
    fig = create_attribute_plot('gender', 900, 500)
    update_standard_bar_plot(fig)
    update_title(fig,25)
    st.plotly_chart(fig,use_container_width=True)
    
with col2:
    # essential
    fig = create_attribute_plot('essential', 900, 500)
    update_standard_bar_plot(fig)
    update_title(fig,25)
    st.plotly_chart(fig,use_container_width=True)

# faction
fig = create_attribute_hbar_plot('faction', 500, 1500)
update_standard_bar_plot(fig)
update_title(fig,25)
fig.update_yaxes(showgrid=False)
fig.update_xaxes(showgrid=True)
st.plotly_chart(fig,use_container_width=True)
    