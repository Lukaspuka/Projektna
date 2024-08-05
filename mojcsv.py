import csv
from luscenje import *

def naredi_csv(ime_csv_datoteke, stevilo_strani):
    with open(ime_csv_datoteke, "w", encoding="utf-8", newline='') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["ime", "zvrst in število epizod", "čas nastajanja", "število uporabnikov", "ocena"])
        bloki = zbiraj_podatke(stevilo_strani)
        for blok in bloki:
            slovar = izlusci_iz_bloka(blok)
            pisatelj.writerow([slovar["ime"], slovar["zvrst_in_število_epizod"], slovar["čas_nastajanja"], slovar["število_uporabnikov"], slovar["ocena"]])

naredi_csv("ime_csv_datoteke.csv", stevilo_strani=20)