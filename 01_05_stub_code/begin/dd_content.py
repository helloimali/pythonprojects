import csv
import random
import json 
from urllib import request

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
    

def get_weather_forecast(lat=44.34, lon=10.99):
    apiKey = "ffb26b4db39c43679fbfb3f7b5ab20b0"
    apiUrl = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apiKey}"
    data = json.load(request.urlopen(apiUrl))
    # data now holds weather data in json
    # print(data)
    retData = {
        'city': data['city']['name'],
        'country': data['city']['country'],
        'period': list(),
        }
    # print(retData["city"])

    # now we need the next 5 days
    for period in data["list"]:
        retData["period"].append(
            {
             'temp': period["main"]["temp"],
             'desc': period["weather"][0]["description"],
            }
        )
    # print(retData)
    return retData

def get_twitter_trends():
    pass

def get_wikipedia_article():
    apiUrl = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

    data = json.load(request.urlopen(apiUrl))

    summary = data["extract"]
    title = data["title"]
    url = data['content_urls']['desktop']['page']

    return (title, summary, url)
    

if __name__ == '__main__':
    # pass # test code

    # print("get random quote")
    # print(get_random_quote())
    # print(get_random_quote())
    # print(get_random_quote(quote=None))x
    
    # print(get_weather_forecast())

    print(get_wikipedia_article())