#This will not run on online IDE
import json
import pprint
from xml.dom.minidom import Attr
import requests
from bs4 import BeautifulSoup
URL = "https://clutch.co/directory/mobile-application-developers?page=0"
dict={}
def scraper(URL):
    
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, "html.parser")

    # print(soup.prettify(encoding='utf8'))

    tables=soup.find_all('h3', attrs={'class':"company_info" })


    for table in tables:  
        name = table.find('a').text.strip() # result not results
        url = table.find('a')['href'].strip()
        dict.update({name:url})
  
    # page number
for i in range(10):
   scraper("https://clutch.co/directory/mobile-application-developers?page={0}".format(i))


with open('data.json', 'w') as fp:
    json.dump(dict, fp , indent=2)



# for keys in dict :
#     f.write(keys)