import requests
from bs4 import BeautifulSoup
import json

mystocks = ['VAST.L', ' ICON.L', 'PREM.L', 'BZT.L', 'ASPL.L']
stockdata = []

def getData(symbol):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = f'https://uk.finance.yahoo.com/quote/{symbol}'
    res = requests.get(url, headers=header)
    # print(res.status_code)
    soup = BeautifulSoup(res.text, 'html.parser')
    stock= {
        'symbol': symbol,
        'price':soup.find('div',  {'class':'D(ib) Mend(20px)'}).find_all('span')[0].text,
        'change':soup.find('span',  {'class':'D(ib) Mend(20px)'}).find_all('span')[1].text
    }
    return stock

#print(getData('ASPL.L'))
for item in mystocks:
    stockdata.append(getData(item))
    print("Getting:", item)

with open('stockdata.json', 'w') as f:
    json.dump(stockdata, f)
