from bs4 import BeautifulSoup
from requests import get

url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/'

page = get(url)
soup = BeautifulSoup(page.content, 'lxml')

x = soup.find("div",{"class":"css-4mw0p4"}).find("ul",{"class":"pagination-list  css-1vdlgt7"}).find_all("a")
print(x)
