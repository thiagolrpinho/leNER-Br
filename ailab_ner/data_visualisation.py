import os
import re
import pandas as pd
from typing import List, Tuple
from wordcloud import WordCloud
from nltk.tokenize import WordPunctTokenizer
import seaborn as sns
import matplotlib.pyplot as plt

DATASETS_RELATIVE_PATH = "./assets/datasets/"

def generate_wordcloud(df_column, figsize=(20, 8)):
    ''' Receives a single a dataframe column and
        prints on screen a wordcould of the 100
        most common words
        :args: df_column -> Dataframe, figsize -> (int, int)
    '''
    text = df_column.str.cat(sep=" ")
    wordcloud = WordCloud(
        max_words=100,
        width=900,
        height=500,
        max_font_size=350,
        collocations=False,
        normalize_plurals=False).generate(text)
    plt.figure(figsize=figsize)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def generate_freq_dist_plot(df_column, max_words=25):
    ''' Receives a single a dataframe column and
        plots on screen a bar graph with the most
        frequent tokens and also return those tokens
        as a list.
        :args: df_column -> DataFrame, max_words -> int
        :returns: words_that_appear_the_most -> List[int]
    '''
    text = df_column.str.cat(sep=" ")
    words = WordPunctTokenizer().tokenize(text)
    words_that_apper_the_most = pd.Series(
        words).value_counts().nlargest(max_words)

    ax = sns.barplot(
        x=words_that_apper_the_most.index,
        y=words_that_apper_the_most.values)
    ax.figure.set_size_inches(20, 7)

    return words_that_apper_the_most
