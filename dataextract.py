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