from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Business
import os

myHeaders = {'Authorization' : os.environ['yelpKey']}
url = "https://api.yelp.com/v3/businesses/"

# /yelp/businesses/{location}
#return businesses within specified vicinity
#TODO change lines 31-33 for mysql databse in prod
def businesses(request, location):

    parameters = {
        'location':location,
        'radius':40000
        }

    try:    
        response = requests.get(url=url + "search", headers=myHeaders, params=parameters)
        data = response.json()

        for business in data['businesses']:
            try:
                Business.objects.get(business_id=business['id'])
                print(business['id'] + " Already in Database!")
            except Exception as e:
                new_business = Business(business_id=business['id'])  # create a new Business Object
                new_business.save()
                print(business['id'] + " Added to Database!")

        #text used to display entire json object
        text = json.dumps(data['businesses'], sort_keys=True, indent=5)
        return HttpResponse(text)

        return(data['businesses'])
        
    except requests.exceptions.HTTPError as error:
        print(error)

# /yelp/business/{id}
#return json object for requested business
#example business id WavvLdfdP6g8aZTtbBQHTw
def business(request, id):
    try:    
        response = requests.get(url=url + id, headers=myHeaders)
        data = response.json()
        
        #text used to display entire json object
        text = json.dumps(data, sort_keys=True, indent=5)
        return HttpResponse(text)
        
        #return data
        
    except requests.exceptions.HTTPError as error:
        print(error)

# /yelp/reviews/{id}
#return json object for requested business
#example business id WavvLdfdP6g8aZTtbBQHTw
def reviews(request, id):
    print(url + id + "/reviews/")
    try:    
        response = requests.get(url=url + id + "/reviews", headers=myHeaders)
        data = response.json()
        
        #text used to display entire json object
        text = json.dumps(data, sort_keys=True, indent=5)
        return HttpResponse(text)
        
        #return data
        
    except requests.exceptions.HTTPError as error:
        print(error)