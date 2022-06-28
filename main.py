"""
Meli Scrapper
Created: 28/06/2022
@author: aloide
"""

from bs4 import BeautifulSoup
import requests
import json

def obtener_precio(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    precio = soup.find_all("span", class_="andes-money-amount__fraction")
    titulo = soup.find_all("h1", class_="ui-pdp-title")
    return (titulo[0].text, float(precio[0].text))

archivo = open("data.json")
data = json.load(archivo)

for url in data["meli_url"]:
    print(obtener_precio(url))
