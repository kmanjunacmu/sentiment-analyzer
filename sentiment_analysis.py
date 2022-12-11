"""
Performs Sentiment Analysis using the VADER library:

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

Nltk downloader required to download the SentimentIntensityAnalyzer.
"""
# import nltk.downloader
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

_api_key = "fc6b9dd03dc841d888b31e6ec049c45f"
_base_url = "https://newsapi.org"
_everything_endpoint = "/v2/everything"


def sentiment_analysis():
    """
    Performs sentiment analysis on the news articles about the user's topic of interest.
    """
    # nltk.downloader.download('vader_lexicon')
    query = _base_url + _everything_endpoint
    sort_by = "top"

    topic = input("Enter the topic of interest : ")

    print(f"\n----------------SENTIMENT ANALYSIS OF NEWS ABOUT {topic.upper()}--------------------\n")

    response = requests.get(url=query, params={'apiKey': _api_key, 'sortBy': sort_by, 'q': topic})
    response_string = json.loads(response.content)
    analysis = []

    for i in range(len(response_string['articles'])):
        headline = response_string['articles'][i]['description']
        print(f"{[i+1]} : {headline}")

        # Get the polarity score of each headline using the VADER model
        polarity_score = sia().polarity_scores(text=headline)
        polarity_score['headline'] = headline
        analysis.append(polarity_score)

    analysis_df = pd.DataFrame.from_records(analysis)

    # A compound score greater than 0.2 indicates a positive sentiment
    # A compound score lesser than 0.2 indicates a negative sentiment

    analysis_df['category'] = 0
    analysis_df.loc[analysis_df['compound'] > 0.2, 'category'] = 1
    analysis_df.loc[analysis_df['compound'] < -0.2, 'category'] = -1

    fig, ax = plt.subplots(figsize=(5, 5))

    counts = analysis_df.category.value_counts(normalize=True) * 100

    sns.barplot(x=counts.index, y=counts, ax=ax)

    ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
    ax.set_ylabel("Percentage")

    plt.show()
