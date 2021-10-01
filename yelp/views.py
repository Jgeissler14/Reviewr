from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

myHeaders = {'Authorization' : 'Bearer pO6GuQayXawfmMhK_h_FUJgj67BXZUFYe0kcBhLmLxYUNu6tJxF_AXJyTSejnKpxfcjrcpwTuw22iAMw7u8ng5xc6gGyaf6hBkZd-IE7h3epMY7cdogc8r_j2l9XYXYx'}
url = "https://api.yelp.com/v3/businesses/"
exampleId = "WavvLdfdP6g8aZTtbBQHTw"

# /yelp/yelp
#return json object for example business
def yelp(request):
    try:    
        response = requests.get(url=url + exampleId, headers=myHeaders)
        data = response.json()
        #text used to display entire json object
        text = json.dumps(data, sort_keys=True, indent=5)
        return HttpResponse(text)
        
    except requests.exceptions.HTTPError as error:
        print(error)

# /yelp/businesses/{location}
#return businesses within specified vicinity
def businesses(request):
    #hardcoded glassboro zip for testing
    location = "08028"
    parameters = {
        'location':location,
        'radius':40000
        }
    try:    
        response = requests.get(url=url + "search", headers=myHeaders, params=parameters)
        data = response.json()

        #text used to display entire json object
        text = json.dumps(data, sort_keys=True, indent=5)
        return HttpResponse(text)

        #return HttpResponse(data)
        
    except requests.exceptions.HTTPError as error:
        print(error)
