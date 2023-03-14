# page to use for all functions called throughout the app
import pandas as pd
from collections import Counter
import networkx as nx
import plotly.express as px

pd.options.plotting.backend = "plotly"


# make title specific size
def update_title(fig, size):
    fig.update_layout(title=dict(font=dict(size=size, color="rgb(31,25,25)")))
    return fig



def update_standard_bar_plot(fig):
    fig.update_layout(showlegend=False)
    fig.update_yaxes(gridcolor="rgb(31,25,25)" , tickfont_size=14, color="rgb(31,25,25)", tickfont_color="rgb(31,25,25)",  titlefont_color="rgb(31,25,25)")
    fig.update_xaxes(gridcolor="rgb(31,25,25)" , tickfont_size=14, color="rgb(31,25,25)", tickfont_color = "rgb(31,25,25)", titlefont_color="rgb(31,25,25)")
    fig.update_traces(marker_color="rgb(141,107,78)"  )
    fig.update_traces(
        textfont_size=14, textangle=0, textposition="outside", textfont_color="rgb(31,25,25)" 
    )
 
    return 

def create_attribute_plot(attribute, width, height):
    # load graphs
    G = nx.read_gpickle('data/G.gpickle')
    GCC = nx.read_gpickle('data/GCC.gpickle')
    # count the number of characters in each attribute
    attribute_dict = dict(G.nodes(data=attribute))
    attribute_distribution = Counter(attribute_dict.values())
    # attribute_distribution.pop('Unknown')

    # save to a df for easier plotting
    attribute_count_df = pd.DataFrame.from_records(list(dict(attribute_distribution).items()), columns=[attribute,'count']).sort_values(by='count', ascending=False)

    # plot
    fig = px.bar(attribute_count_df, x=attribute, y='count', title=f'Count of characters per {attribute}', 
                color=attribute, template='plotly_dark', text_auto=".s",
                width=width, height=height,
                labels=dict(count="Number of characters", attribute=attribute)) 
    
    
    return fig

def create_attribute_hbar_plot(attribute, width, height):
    # load graphs
    G = nx.read_gpickle('data/G.gpickle')
    GCC = nx.read_gpickle('data/GCC.gpickle')
    # count the number of characters in each attribute
    attribute_dict = dict(G.nodes(data=attribute))
    attribute_distribution = Counter(attribute_dict.values())
    # attribute_distribution.pop('Unknown')

    # save to a df for easier plotting
    attribute_count_df = pd.DataFrame.from_records(list(dict(attribute_distribution).items()), columns=[attribute,'count']).sort_values(by='count', ascending=False)

    # plot
    fig = px.bar(attribute_count_df, y=attribute, x='count', title=f'Count of characters per {attribute}', 
                color=attribute, template='plotly_dark', text_auto=".s",
                width=width, height=height,
                labels=dict(count="Number of characters", attribute=attribute)) 
    return fig