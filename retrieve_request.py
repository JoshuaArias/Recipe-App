'''
Handles response with recipe API
'''

import requests
import json
import urllib.parse
from urllib.request import Request, urlopen

API_KEY = "****"
SEARCH_URL = "http://food2fork.com/api/search?"
RECIPE_URL = "http://food2fork.com/api/get?"

class Get_Response:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        
    def request_response(self, url):
        '''
        Takes url and returns the response from the webpage
        Required to bypass a website blocking an attempt to connect
        '''
        class AppURLopener(urllib.request.FancyURLopener):
            version = "Mozilla/5.0"
        opener = AppURLopener()
        response = opener.open(url)
        return response
    
    def parse_response(self, response):
        '''
        Takes response from url and returns a loaded json response
        '''
        json_text = response.read().decode(encoding = 'utf-8')
        json_response = json.loads(json_text)
        return json_response
    
    def get_all_recipes(self, page = 1):
        '''
        Given a list of ingredients, return top recipes that include them
        '''
        parameters = [("key", API_KEY), 
                      ("q", self.ingredients),
                      ("sort", "T"),
                      ("page", page) ]
        url = SEARCH_URL + urllib.parse.urlencode(parameters)
        print(url)
        response = self.request_response(url)
        json = self.parse_response(response)
        return json

    def get_recipe_by_id(self, recipe_id):
        '''
        Return information for a recipe by ID
        '''
        parameters = [("key", API_KEY),
                      ('rId', recipe_id)]
        url = RECIPE_URL + urllib.parse.urlencode(parameters)
        print(url)
        response = self.request_response(url)
        json = self.parse_response(response)
        return json

