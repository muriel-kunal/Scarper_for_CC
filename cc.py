import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import sys
import os
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By #type : ignore
from selenium.webdriver.support.ui import WebDriverWait #type : ignore
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH']+=r"C:\Users\ADMIN\Desktop\Scarpper"
driver=webdriver.Chrome()


driver.get('https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests')

def get_names(soup) :
    heading=soup.find('tbody',{'id' : 'future-contests-data'})
    items=heading.find_all('tr')
    names=[]
    for item in items :
        names.append(item.a.text)
    return names

def get_links(soup) :
    heading=soup.find('tbody',{'id' : 'future-contests-data'})
    items=heading.find_all('tr')
    links=[]
    for item in items :
        link=item.find('a').get('href')
        link ='https://www.codechef.com/'+str(link)
        links.append(str(link))
    return links
        
def get_dates(soup ) :
    heading=soup.find('tbody',{'id' : 'future-contests-data'})
    items=heading.find_all('tr')
    dates=[]
    for item in items :
        date=item.find_all('td')
        tchtch=date[2].text
        dates.append(str(tchtch))
    return dates
    

soup =BeautifulSoup(driver.page_source,'html.parser')
dates=get_dates(soup)
for date in dates :
    print(date)
driver.quit()