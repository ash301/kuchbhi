import urllib2

url = "https://en.wikipedia.org/wiki/List_of_postcode_districts_in_the_United_Kingdom"

#import BeautifulSoup
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0'} #needed to prevent 403 eror
req = urllib2.Request(url,headers = header) 


#fetch the html of the url

page = urllib2.urlopen(req)
#parse the html 

soup = BeautifulSoup(page)

area=""
district=""
town=""
country=""


table = soup.find("table",{"class":"wikitable sortable"})

f = open('output.csv','w')


#print table.prettify()

for row in table.findAll("tr"):
	cells = row.findAll("td")

	#for each "tr" assign ech "td" to a variable

	if len(cells) == 4:
		area = cells[0].find(text = True)
		district = cells[1].findAll(text=True)
		town = cells[2].find(text=True)
		country = cells[3].find(text=True)



	for x in range(len(district)):

		postcode_list = district[x].split(",")

		for i in range(len(postcode_list)):

			if(len(postcode_list[i])>2) and (len(postcode_list[i])<=5):

			#strip \n that is at the begening of some postcodes
				write_f = area + ","+postcode_list[i].lstrip('\n').strip() +","+town +" , "+ country + "\n"
				f.write(write_f)

f.close()

