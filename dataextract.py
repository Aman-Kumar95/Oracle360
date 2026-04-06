import requests
from bs4 import BeautifulSoup
import csv
from textblob import TextBlob
import matplotlib.pyplot as plt

query= "zomato complaint"

url= "https://old.reddit.com/search"
params= {"q":query}

headers= {
    "User-Agent" : "Mozilla/5.0"
}

response = requests.get(url,headers= headers,params=params)
soup= BeautifulSoup(response.text,"html.parser")

posts= soup.find_all("a",class_= "title")
data= []

for post in posts[:20]:
    title= post.text
    link = post.get("href")

    polarity= TextBlob(title).sentiment.polarity

    if polarity>0:
        sentiment= "Positive"
    elif polarity <0 :
        sentiment= "Negative"
    else:
        sentiment= "Neutral"

        data.append([title,link,sentiment])