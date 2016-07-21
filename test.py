import urllib2 
from bs4 import BeautifulSoup
#specify the url you want to query

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#query the website and return the html to the page
page = urllib2.urlopen(url)

#parse the html in the page variable and store in the BeautifulSoup format

soup = BeautifulSoup(page)

#iterate over each tag and then return link using href with get 

all_my_links = soup.find_all("a")
all_my_tables = soup.find_all('table')

#to find right table

right_table = soup.find('table',class_='wikitable sortable plainrowheaders jquery-tablesorter')
#print right_table

heading_data = soup.find_all('th')

for i in heading_data:
	print i.get_text() 

table_data  = soup.find_all('td')

for j in table_data:
	print j.get_text()



# """
# for i in all_my_links:
# 	print i.get("href")

# """


