import requests
url = "https://realty-mole-property-api.p.rapidapi.com/saleListings"

querystring = {"city":"Austin","state":"TX"}

headers = {
    'x-rapidapi-host': "realty-mole-property-api.p.rapidapi.com",
    'x-rapidapi-key': "34625615e4msh88c6bc89082c953p12795cjsnc6833b4a870c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)