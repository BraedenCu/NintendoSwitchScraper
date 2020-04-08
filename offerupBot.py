
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

html = urlopen("https://offerup.com/search/?q=nintendo%20switch")
s = html.read()
soup = BeautifulSoup(s, 'lxml')


class newProduct():
    def declarationOfVariabels():
        global a
        a = soup.find('span', attrs={'class':'_s3g03e4'})

    def fullDeatails():
        name_box = soup.find('a', attrs={'class': '_109rpto _1anrh0x'})

    def findPrice():
        global price_box
        price_box = soup.find('span', attrs={'class':'_s3g03e4'})
    
    def comparePrices():
        if a != price_box:
            print("newItemFoundPog")
            b = price_box
            print(price_box)
        if a == price_box:
            print("no new item found")
            print(price_box)
         
if __name__ == "__main__":
    newProduct.declarationOfVariabels()
    newProduct.findPrice()
    newProduct.comparePrices()
