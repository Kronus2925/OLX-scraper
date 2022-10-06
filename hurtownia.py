import requests
from bs4 import BeautifulSoup
import pandas as pd




def main():
   
   category = []
   cat_name = []

   url = 'https://www.hurtowniazabawek.pl/' 


   soup = html_access(url)
   get_category_name(soup,cat_name)
   get_categories(soup, category)
  
   for cat in cat_name:
    name = cat
    mainlist = []
    for i in category:

        soup1 = html_access(i)
        mainlist.extend(product_details(soup1))
    get_excel(mainlist,name)


def html_access(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content,'lxml')
    return soup


def get_categories(soup, category):

    for i in soup.find_all('a',{"class" : "categorySubMenu__categoryItem col"}):
        kategorie = i['href']
        category.append(kategorie)


def get_category_name(soup, cat_name):

    for i in soup.find_all('a' ,{"class" : "categorySubMenu__categoryItem col"}):

        kat = i.find('span', {"class": "categorySubMenu__categoryName"}).get_text().lower()
        cat_name.append(kat)
    

def product_details(soup):

    roducts = []
    for i in soup.find_all('div',{"class": "moreBox productIcon__descBox"}):
        
        products = {
            "name" : i.find('a',{"class":"productIcon__descNameLink"}).get_text(),
            "price" : i.find('div',{"class":"productIcon__descPrice"}).get_text()
        }
        roducts.append(products)
    return roducts


def get_excel(roducts,i):
    df = pd.DataFrame(roducts)
    df.to_excel(f'{i}.xlsx',index=True)

main()
