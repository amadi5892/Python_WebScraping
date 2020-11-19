# ---- Task 1 ----
import requests
import bs4

# ---- Task 2 ----
res = requests.get('http://quotes.toscrape.com/')
# print(res.text)

# ---- Task 3 ----
# Get the names of all the authors on the first page. 
soup = bs4.BeautifulSoup(res.text,'html5lib')
names = soup.select('small')
authors = []
# print(names[0].getText())
for n in range(0,10):
    authors.append(names[n].getText())

# print(set(authors))

# ---- Task 4 ----
# Create a list of all the quotes on the first page.
sayings = soup.select('.text')
# print(sayings[0].getText())
quotes = []
for n in range(0,10):
    quotes.append(sayings[n].getText())

# print(quotes)

# ---- Task 5 ----
# Create a list of the Top Ten Tags
top_ten = soup.select('.tag-item')
# print(top_ten[0].getText())

# for n in range(0,10):
#     print(top_ten[n].getText())

# ---- Task 5 ----
base_url = 'http://quotes.toscrape.com/page/{}/'
creators = set()
for n in range(1,10):

    scrape_url = base_url.format(n)
    ans = requests.get(scrape_url)

    soup2 = bs4.BeautifulSoup(ans.text,'html5lib')
    
    for name in soup.select('.author'):
        creators.add(name.text)

print(creators)
