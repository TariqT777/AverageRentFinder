from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from socket import timeout
from urllib.error import HTTPError, URLError


my_url = "https://www.apartments.com/"

#uClient = uReq(my_url)
try:
    response = uReq(my_url, timeout=10).read().decode('utf-8')
except HTTPError as error:
    raise Exception('Data not retrieved because URL: ', error, my_url)
except URLError as error:
    raise Exception('URL Error')
except timeout:
    raise Exception('socket timed out - URL:', my_url)
else:
    print('Access successful.')
readPage = uReq.read()
#print(readPage)
uReq.close()


#html parsing
page_soup = soup(readPage, "html.parser")

print(page_soup.h1)