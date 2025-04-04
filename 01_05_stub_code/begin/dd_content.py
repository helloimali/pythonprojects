import csv
import random

def get_random_quote(quote='quotes.csv'):
    try:
        with open(quote) as csvfile:
            quotes = [{
                'author': line[0],
                'quote': line[1]} for line in csv.reader(csvfile, delimiter='|')]
            
    except Exception as e:
        quotes = [{
                'author': 'Andy',
                'quote': 'Vibes are vibing'}
                ]

    return random.choice(quotes)
    

def get_weather_forecast():
    pass

def get_twitter_trends():
    pass

def get_wikipedia_article():
    pass

if __name__ == '__main__':
    # pass # test code
    print("get random quote")
    print(get_random_quote())
    print(get_random_quote())
    print(get_random_quote(quote=None))