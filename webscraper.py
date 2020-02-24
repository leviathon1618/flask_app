import requests
from bs4 import BeautifulSoup

class Product():
    def __init__(self, item, price):
        self.item = item
        self.price = price

def cycle():
    response = requests.get("https://www.trademe.co.nz/Browse/SearchResults.aspx?searchString=ps4&type=Search&searchType=all&buy=buynow&page=2")
    soup = BeautifulSoup(response.text,"html.parser")
    itemlist = soup.findAll("div", {"class":"supergrid-listing"})
    cnt = len(itemlist)
    return itemlist

def Element(itemlist):
    productlist = []
    for item in itemlist:
        if item.find("div",{"class":"title"}) != None:  
            item_title = item.find("div",{"class":"title"}).text.strip()
            item_price = item.find("div",{"class":"listingBuyNowPrice"}).text.strip()
            productlist.append(Product(item_title, item_price))
    return productlist


def work():
    productlist = Element(cycle())
    return productlist 