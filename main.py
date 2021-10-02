from urllib import response
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from socket import timeout
from urllib.error import HTTPError, URLError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def grabURL():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    my_url = "https://www.apartments.com/queens-ny/?bb=wvn4ot71wH89k0vqS"
    driver.get(my_url)
    #uClient = uReq(my_url)
    
    prices = driver.find_elements_by_xpath('//div[@class="price-range"]')
    prices_list = []
    for price in range(len(prices)):
        prices_list.append(prices[price].text)
    print(prices_list)
    
    '''
    try:
        response = uReq(my_url, timeout=10).read().decode('utf-8')
    except HTTPError as error:
        raise Exception('Data not retrieved because URL: ', error, my_url)
    except URLError as error:
        raise Exception('URL Error')
    except timeout:
        raise Exception('socket timed out: '+ my_url)
    else:
        print('Access successful.')
    readPage = response
    #print(readPage)
    


    #html parsing
    page_soup = soup(readPage, "html.parser")

    print(page_soup.h1)
'''
grabURL()