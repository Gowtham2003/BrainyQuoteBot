# Coded By Gowtham on 03/06/2020
# Coded Using Visual Studio Code

import requests
from bs4 import BeautifulSoup as bs
import random

def getQuotes(query):
    BASE_URL = "https://www.brainyquote.com/"

    url = f"https://www.brainyquote.com/topics/{query}-quotes"

    quotesDictionary = {
        "success": True,
        "data": []
    }

    try:
        soup = bs(requests.get(url).content, "lxml")
    except AssertionError as er:
        print(er)
        quotesDictionary["success"] = False

    divs = soup.findAll("div", {"class": "qll-bg"})

    for div in divs:
        try:
            quote = div.find("a", {"title": "view quote"}).text
        except:
            quote = ""
        try:
            quotelink = BASE_URL + \
                div.find("a", {"title": "view quote"}).get("href")
        except:
            quotelink = ""
        try:
            author = "By " + div.find("a", {"title": "view author"}).text
        except:
            author = ""
        try:
            authorlink = BASE_URL + \
                div.find("a", {"title": "view author"}).get("href")
        except:
            authorlink = ""

        try:
            tagsElement = div.findAll(
                "a", {"class": "qkw-btn btn btn-xs oncl_list_kc"})
        except:
            tagsElement = []
        tags = []
        for tag in tagsElement:
            tags += tag

        QuoteContent = {
            "quote": quote,
            "quotelink": quotelink,
            "author": author,
            "authorlink": authorlink,
            "tags": tags
        }

        quotesDictionary["data"].append(QuoteContent)
    dt = quotesDictionary["data"]
    ran = random.randint(0,len(dt)-1)
    data = dt[ran]
    return data

    print(quotesDictionary)
