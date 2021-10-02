from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.apartments.com/queens-ny/"

uClient = uReq(my_url)
readPage = uClient.read()
#print(readPage)
uClient.close()


#html parsing
page_soup = soup(readPage, "html.parser")