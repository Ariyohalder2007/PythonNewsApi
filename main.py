import requests
import json
from plyer import notification
url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=2606a35885384640a5d2592e449ad907')
response = requests.get(url)
data = response.json()
def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:/Users/Tushar Chowdhury/Desktop/News Api Python/news.ico",
        timeout=15
    )
# print(data["articles"])
# print(response.json())
articles=data["articles"]
for i in articles[:10]:
    # print(i["title"])
    # print(i["content"])
    title=i["title"]
    content=i["content"]
    notifyMe(title[:64], content)