import requests
import bs4

# ---- GRABBING A TITLE ----
# result = requests.get('http://www.example.com')
# # print(result.text)

# # I specifically have to use html5lib as my parser (for Pure Python)
# soup = bs4.BeautifulSoup(result.text,"html5lib")
# print(soup)

# print(soup.select('title')[0].getText())

# site_paragraphs = soup.select('p')
# print(site_paragraphs[0].getText())


# ---- GRABBING A CLASS ----
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text,"html5lib")
# print(soup)

# soup 
first_item = soup.select('.toctext')[0]
print(first_item.text)

for item in soup.select('.toctext'):
    print(item.text)

