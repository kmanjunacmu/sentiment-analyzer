"""
Scrapes news from NEWS API and Local news from www.wxpi.com.
"""
import json
import requests
from bs4 import BeautifulSoup

_api_key = "fc6b9dd03dc841d888b31e6ec049c45f"
_base_url = "https://newsapi.org"
_everything_endpoint = "/v2/everything"
_top_headline_endpoint = "/v2/top-headlines"
_local_news = "https://www.wpxi.com/"


def print_news_articles(json_string):
    """
    Prints the news articles in the JSON String.
    :param json_string : A JSON string containing news articles as returned by the API.
    """
    for i in range(len(json_string['articles'])):
        print(f"{i + 1} : {json_string['articles'][i]['description']}")


def get_sort_choice():
    """
    Gets the user's choice on sorting the news articles.
    :return: request parameter corresponding to user's choice
    """
    while True:
        print("\nEnter 1 to sort the articles by Relevance\n" +
              "Enter 2 to sort the articles by Popularity\n" +
              "Enter 3 to sort the articles by published date.")

        sort_by_choice = int(input("Enter your choice (1/2/3): "))

        if sort_by_choice == 1:
            return "relevancy"
        elif sort_by_choice == 2:
            return "popularity"
        elif sort_by_choice == 3:
            return "publishedAt"
        else:
            print("Incorrect choice for sorting entered!")


def search_news_articles_from_keyword():
    """
    Searches for news articles based on the keyword entered by the user and prints them.
    """
    query = _base_url + _everything_endpoint

    topic = input("Enter the topic of interest : ")

    sort_by = get_sort_choice()

    print(f"\n----------------NEWS ABOUT {topic.upper()}--------------------\n")

    response = requests.get(url=query, params={'apiKey': _api_key, 'sortBy': sort_by, 'q': topic})
    print_news_articles(json.loads(response.content))


def display_top_headlines():
    """
    Displays top headlines in the category entered by the user.
    Available categories: business, entertainment, general, health, science, sports, technology
    """
    query = _base_url + _top_headline_endpoint
    country = "us"
    cat_list = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

    while True:
        print("CATEGORIES : Business | Entertainment | General | Health | Science | Sports | Technology")
        category_input = input("Which category would like to explore? ")
        category = category_input.lower()

        if category.strip() in cat_list:
            break

        print("\nPlease enter a category from the above list\n")

    response = requests.get(url=query, params={'apiKey': _api_key, 'country': country, 'category': category})

    print(f"\n----------------TOP HEADLINES OF {category_input.upper()} CATEGORY--------------------\n")

    print_news_articles(json.loads(response.content))


def display_local_news():
    """
    Displays top 10 headlines from the local Pittsburgh news.
    Scrapes the headlines from "www.wpxi.com"
    """
    print(f"\n----------------LOCAL NEWS--------------------\n")

    query = _local_news
    response = requests.get(query)
    soup = BeautifulSoup(response.content, 'html.parser')
    i = 1
    for article in soup.find_all("div", {"class": "promo-headline headline-wrap"}):
        print(f'{i} : {article.get_text()}')
        if i == 10:
            break
        i += 1
