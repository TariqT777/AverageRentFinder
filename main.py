from urllib import response
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from socket import timeout
from urllib.error import HTTPError, URLError
from numpy import character
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def grabURL():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    my_url = "https://www.apartments.com/queens-ny/?bb=wvn4ot71wH89k0vqS"
    #df = pd.DataFrame(columns=['prices'])
    
    
    '''
    #We can use this commented out code in order to help us find the next page
    for pg in range(1,5):
        page_num = str(pg) + '-' + str(pg+1) +'/'
    url = 'https://www.apartments.com/queens-ny' + page_num
    driver.get(url)
    '''
    
    
    driver.get(my_url)
    #uClient = uReq(my_url)
    
    prices = driver.find_elements_by_xpath('//div[@class="price-range"]')
    prices_list = []
    for price in range(len(prices)):
        prices_list.append(prices[price].text)
    print(prices_list)
    print("\n""\n")
    for price_range in range(len(prices_list)):
        prices_list[price_range] = prices_list[price_range].replace(" - ",",")


    #prices_string = " "
   # prices_list = prices_string.join(prices_list)

    #prices_list = prices_list.split(",")
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