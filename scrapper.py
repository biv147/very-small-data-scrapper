import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.ca/Logitech-Gaming-Headset-Black-Size/dp/B07PDFBJZD/ref=sr_1_2?crid=247TIDGSR5JFW&dchild=1&keywords=logitech+g+pro+x&s=electronics&sprefix=g+x+pro+%2Celectronics%2C181&sr=1-2"

headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

stringPrice = soup.find(id="priceblock_ourprice").get_text()
price = float(stringPrice[5:11])

if(price < 160):
    print("Price has been lowered below 160")
    print(price)
elif(price < 150):
    print("Price has been lowered below 150")
    print(price)
elif(price < 140):
    print("Price has been lowered below 140, deal is very nice!!")
    print(price)
elif(price < 130):
    print("Price has been lowered below 130, deal is AWESOME!!")
    print(price)
elif(price < 120):
    print("BUY IT NOWWW!!")
    print(price)
else:
    print("Price is still the same")
    print(price)

