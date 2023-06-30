import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://uk.finance.yahoo.com/quote/ASPL.L'
res = requests.get(url, headers=header)
# print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')


# price =  soup. find('span',  {' '})