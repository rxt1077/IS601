import requests
from bs4 import BeautifulSoup

# requests
query = "lifepo4"
response = requests.get(f"https://cnj.craigslist.org/search/sss?sort=date&query={query}")

# beautiful soup
soup = BeautifulSoup(response.text, 'html.parser')
for result in soup.select('a.result-title'):
    data_id = result['data-id']
    title = result.string
    datetime = result.find_previous('time')['datetime']
    print(f"{data_id},{datetime},{title}")
