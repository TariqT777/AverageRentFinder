from urllib import response
from urllib.request import urlopen as uReq
#from bs4 import BeautifulSoup as soup
from socket import timeout
from urllib.error import HTTPError, URLError
#from numpy import character
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from flask import Flask, render_template,request,flash,redirect
from appForms import cityStateForm

#from werkzeug.fixers import CGIRootFix

    
def grabURL(my_url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #URL to webscrape from
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
    
    prices = driver.find_elements_by_xpath('//div[@class="price-range"]') #Finds the section with the data that we're looking for.
    prices_list = []
    for price in range(len(prices)): #Finds all the prices on the page and stores it in a list.
        prices_list.append(prices[price].text) 
    print(prices_list)
    print("\n""\n")
    for price_range in range(len(prices_list)): #Since the prices are displayed as a string on Apartments.com, the following lines get rid of any unnecessary charachters (like the commas).
        prices_list[price_range] = prices_list[price_range].replace(" - ",":")
        prices_list[price_range] = prices_list[price_range].replace("$","")
        prices_list[price_range] = prices_list[price_range].replace(",","")
    if "Call for Rent" in prices_list:
        i = 0
        while i < len(prices_list):
            if prices_list[i] == "Call for Rent":
                prices_list.remove("Call for Rent")   #Eliminates any places that don't provide their rent on website. 
            else:
                i += 1
    prices_list = [[i] for i in prices_list] #Creating a nested list to make it easier to change the parsed strings into int types.

    for price_range in range(len(prices_list)): #Split the max and min prices of each apartments into separate entity based off of the ':' delimiter we created earlier.
        prices_list[price_range] = prices_list[price_range][0].split(":") 

    print(prices_list)

    for price_range in range(len(prices_list)): #Finally turn each number into an int type.
        for index in range(len(prices_list[price_range])):
            prices_list[price_range][index] = int(prices_list[price_range][index]) 

    priceSumList = []
    for price_range in range(len(prices_list)): #Get the average of each apartment's price and then put them into a new list for separate use.
        priceSumList.append(sum(prices_list[price_range])/len(prices_list[price_range]))
    
    print("avg of each apartment is:", priceSumList)

    totalRentAvg =  sum(priceSumList)/len(priceSumList)
    totalRentAvg = "%.2f" % totalRentAvg
    print("The average rent for an apartment is :","$"+totalRentAvg)

    return "$" + totalRentAvg + "/Month"

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any secret string'

@app.route('/', methods=['GET', 'POST']) #Grabs the input from the form and displays output if valid.
def cityState():
    form = cityStateForm()
    if form.validate_on_submit():
        addCity = form.city.data 
        addState = form.state.data
        my_url = "https://www.apartments.com/" + addCity + "-" + addState + "/"
        flash(grabURL(my_url))
        #'Location requested for {}, in {}'.format(
         #   form.city.data, form.state.data))
        return redirect('/')
    return render_template('/index.html', title="Average Rent", form=form)

#my_url = "https://www.apartments.com/" + addCity + "-" + addState + "/"
#print(my_url)

if __name__ == '__main__':
    app.run(debug = True)
    
    
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




'''

Not using this rn, but may need it later.
@app.route('/')
def index():
    return render_template('index.html',totalRentAvg = grabURL())
'''


'''
@app.route('/', methods=['POST']) #This grabs the input from the form on the index.html page.
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    print("test", processed_text)
    #return "test",processed_text
'''
