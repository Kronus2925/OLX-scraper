from bs4 import BeautifulSoup
from requests import get
import pandas as pd

def main():

    url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/'

    loc =[]
    tit =[]
    prc =[]
    lnk =[]

    get_html(url)
    soup = get_html(url)
    load_data(soup, loc, tit, prc, lnk)
    excel_export(loc, tit, prc, lnk)

def get_html(url):

    page = get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    return soup

def load_data(soup, loc, tit, prc, lnk):

    offers = soup.find_all('div',{"class" : "offer-wrapper"})

    for offer in offers:

            footer = offer.find('td',{'class' : 'bottom-cell'})
            location = footer.find('small', {'class' : 'breadcrumb x-normal'}).get_text().strip()
            loc.append(location)
            title = offer.find('strong').get_text().strip()
            tit.append(title)
            price = offer.find('p', {'class' : 'price'}).get_text().strip()
            prc.append(price)
            links= offer.find('a').get('href')
            lnk.append(links)

def excel_export(loc, tit, prc, lnk):

    d = {
        "Lokalizacja" : loc,
        "Tytuł" : tit,
        "Cena" : prc,
        "Link" : lnk,
    }
    df = pd.DataFrame(d)
    df.to_excel('mieszkania.xlsx')

main()