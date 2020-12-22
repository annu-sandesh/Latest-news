import speech
import requests
import json
import time

url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=7ccc4eb95bbb40eb8ef3eea3a1c5c8c7"

speech.say("lets begin..")

r = requests.get(url).text
news = json.loads(r)
arts = news["articles"]

for article in arts:
    speech.say(article['title'])
    speech.say("next one is")
    print(article['title'],"\n")
    time.sleep(8)
