import re
import requests as req
import csv

def prenesi_html(url):
    html = req.get(url)
    # with open("html_datoteka", "w", encoding="utf-8") as dat:
    #     print(html.text, file=dat)
    return html.text

# prenesi_html("https://myanimelist.net/topanime.php")

def bloki_podatkov(html):
    vzorec = r'<div class="di-ib clearfix"><h3 class="fl-l fs14 fw-b anime_ranking_h3">.*?Add to My List</a></td>'
    return re.findall(vzorec, html, flags=re.DOTALL)

print(len(bloki_podatkov(prenesi_html("https://myanimelist.net/topanime.php"))))

def izlusci_iz_bloka(blok):
    vzorec = re.compile(r'class="hoverinfo_trigger">(?P<ime>.*?)</a>.*?'
                        r'', re.DOTALL)
    najdba = vzorec.search(blok)
    slovar = {}
    slovar["ime"] = najdba["ime"]
    return slovar
