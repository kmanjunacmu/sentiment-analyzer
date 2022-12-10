import news
import sentiment_analysis
import news_archive
import pandas as pd


if __name__ == '__main__':
    """
    Displays the main menu to the user.
    """
    csv_df = pd.read_csv("old-newspaper.csv")

    while True:
        print("\n**********MENU**********")
        print("1. Search for news articles by keyword")
        print("2. Display top headlines")
        print("3. Display local news")
        print("4. Perform Sentiment analysis")
        print("5. Display news from archive based on language")
        print("6. Exit\n")

        choice = int(input("Enter your choice (1/2/3/4/5/6) : "))

        if choice == 1:
            news.search_news_articles_from_keyword()

        elif choice == 2:
            news.display_top_headlines()

        elif choice == 3:
            news.display_local_news()

        elif choice == 4:
            sentiment_analysis.sentiment_analysis()

        elif choice == 5:
            news_archive.search_archives_from_keyword(csv_df)

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Incorrect choice entered.")
