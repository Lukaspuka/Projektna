import re
import requests as req

def prenesi_html(url):
    html = req.get(url)
    with open("html_datoteka", "w", encoding="utf-8") as dat:
        print(html.text, file=dat)

prenesi_html("https://www.flashscore.com/")