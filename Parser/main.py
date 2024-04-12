import requests
from bs4 import BeautifulSoup
import lxml
import sys
import re

url = "https://fnbr.co/shop"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)
src = req.text

soup = BeautifulSoup(src, "lxml")

div_owner = soup.find("div", "shop-container")

all_title = soup.find_all("h2", "shop-section-title")

title_list = []

for item in all_title:
    title_list.append(item.text)
picture_list = []
all_item_div = soup.find_all("div", "items-row shop-items slosh-mode")
all_item = soup.find_all("div", "item-responsive")
for item in all_item:
    picture = item.find("img", "desktop-img outfit")
    if picture == None:
        picture = item.find("img", "desktop-img emote")
        if picture == None:
            picture = item.find("img", "desktop-img bundle")
            if picture == None:
                picture = item.find("img", "desktop-img backpack")
                if picture == None:
                    picture = item.find("img", "desktop-img wrap")
                    if picture == None:
                        picture = item.find("img", "desktop-img glider")
                        if picture == None:
                            picture = item.find("img", "desktop-img pickaxe")
                            if picture == None:
                                picture = item.find("img", "desktop-img bass")
                                if picture == None:
                                    picture = item.find("img", "desktop-img microphone")
                                    if picture == None:
                                        picture = item.find("img", "desktop-img keytar")
                                        if picture == None:
                                            picture = item.find("img", "desktop-img guitar")
                                            if picture == None:
                                                picture = item.find("img", "desktop-img drums")
                                                if picture == None:
                                                    picture = item.find("img", "desktop-img jam-tracks")

    pattern_three = re.compile(re.escape('src="') + '(.*?)' + re.escape('"/>'))
    match_three = re.search(pattern_three, str(picture))
    if match_three:
        picture = match_three.group(1)

    picture_list.append(picture)
# print(picture_list)

item_shop = {}
name_div = soup.find_all("div", "content-box")
name_list = []
for item in name_div:
    name = item.find("h4", "item-name marquee")

    name = item.find("h4", "item-name")

    pattern = re.compile(re.escape("<span>") + '(.*?)' + re.escape("</span>"))
    match = re.search(pattern, str(name))
    if match:
        name = match.group(1)

    if name == None:
        name = item.find("h4", "item-name")

        pattern = re.compile(re.escape("<span>") + '(.*?)' + re.escape("</span>"))
        match = re.search(pattern, str(name))
        if match:
            name = match.group(1)

    name_list.append(name)
# print(name_list)

price_list = []
for item in name_div:
    price = item.find("p", "item-price")

    pattern_two = re.compile(re.escape('\n') + '(.*?)' + re.escape('\n</p>'))
    match_two = re.search(pattern_two, str(price))
    if match_two:
        price = match_two.group(1)

    price_list.append(price)
# print(price_list)

for name_name, price_price in zip(name_list, price_list):
    item_shop[name_name] = price_price
# print(item_shop)

