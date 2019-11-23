from bs4 import BeautifulSoup
import requests

# Specify with which URL/web page we are going to be scraping
url = requests.get('https://www.facebook.com/?ref=tn_tnmn').text

soup = BeautifulSoup(url, "lxml")
#To look at the HTML underlying to the web 
print(soup.prettify())
#To get the title of the page
soup.title()
# use the 'find_all' function to bring back all instances of the 'table' tag in the HTML and store in 'all_tables' variable
all_tables=soup.find_all("table")
all_tables

# use the 'find_all' function to bring back all instances of the 'table' tag in the HTML and store in 'all_tables' variable
My_table = soup.find('table',)

links = My_table.findAll('a')

Countries = []
for link in links:
    Countries.append(link.get('title'))
    
print(Countries)

import pandas as pd
df = pd.DataFrame()
df['Country'] = Countries
