import re
import requests as req
import csv

def prenesi_html(stran):
    url = f"https://myanimelist.net/topanime.php?limit={stran * 50}"
    odgovor = req.get(url)
    odgovor.raise_for_status()
    with open("html_datoteka", "w", encoding="utf-8") as dat:
        dat.write(odgovor.text)
    return odgovor.text


def bloki_podatkov(html):
    vzorec = r'<div class="di-ib clearfix"><h3 class="fl-l fs14 fw-b anime_ranking_h3">.*?Add to My List</a></td>'
    return re.findall(vzorec, html, flags=re.DOTALL)


def izlusci_iz_bloka(blok):
    vzorec = re.compile(
        r'class="hoverinfo_trigger">(?P<ime>.*?)</a>.*?'
        r'<div class="information di-ib mt4">.*?'
        r'(?P<zvrst_in_število_epizod>.*?)<br>.*?'
        r'(?P<čas_nastajanja>.*?)<br>.*?'
        r'(?P<število_uporabnikov>\d{1,3}(?:,\d{3})*) members.*?'
        r'<span class="text on score-label score-\d+">(?P<ocena>\d+\.\d+)</span>',
        re.DOTALL
    )
    najdba = vzorec.search(blok)
    if najdba:
        slovar = {
            "ime": najdba.group("ime").strip(),
            "zvrst_in_število_epizod": najdba.group("zvrst_in_število_epizod").strip(),
            "čas_nastajanja": najdba.group("čas_nastajanja").strip(),
            "število_uporabnikov": najdba.group("število_uporabnikov").strip(),
            "ocena": najdba.group("ocena").strip()
        }
    else:
        slovar = {
            "ime": "N/A",
            "zvrst_in_število_epizod": "N/A",
            "čas_nastajanja": "N/A",
            "število_uporabnikov": "N/A",
            "ocena": "N/A"
        }
    return slovar

def zbiraj_podatke(stevilo_strani):
    vsi_bloki = []
    for i in range(stevilo_strani):
        html = prenesi_html(i)
        bloki = bloki_podatkov(html)
        vsi_bloki.extend(bloki)
    return vsi_bloki

zbiraj_podatke(20)