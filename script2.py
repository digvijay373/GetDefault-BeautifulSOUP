
import json
from xml.dom.minidom import Attr
import requests
from csv import writer
from bs4 import BeautifulSoup
dict=[]


    
URL="https://clutch.co/profile/algoworks"
def scraper( name ,URL):
     r = requests.get(URL)
     soup = BeautifulSoup(r.content, "html.parser")

    #  print(soup.prettify(encoding='utf8'))
     
     tables=soup.find_all('div', attrs={'class':"module-list"})
     link=soup.find('a' , attrs={'class':'website-link__item'})
     phone=soup.find('a' , attrs={'class':'contact phone_icon'})
     try:
      contact=(phone.text).strip()
     except :
       contact=None

     print(contact)
     website=link['href']
     for table in tables:  
        spans = table.find_all('span') # result not results
        data=[]
        for span in spans:
            data.append(span.text)
        
        projectsize=data[0]
        hourlyrates=data[1]
        employeesize=data[2]
        founded=data[3]
        dict.append((name , contact , website , projectsize , hourlyrates , employeesize , founded))
        
        
f=open('data.json')
data=json.load(f)
print(data)

for keys in data:
  URL=('https://clutch.co'+data[keys])
  print(URL)
  scraper(keys ,URL=URL)

with open('data.csv', 'w', newline='') as f_object:  
    # Pass the CSV  file object to the writer() function
    obj = writer(f_object)
    # Result - a writer object
    # Pass the data in the list as an argument into the writerow() function
    obj.writerow(['name' , 'contact' , 'website' ,'projectsize' , 'hourlyrates','employee size' , 'founded' ]) 
    obj.writerows(dict)
print(dict)
