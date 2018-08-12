'''
Handles what the user sees
    inputing ingredients
    default sort:
        by trending
        by most ingredient match
    enable next recipe if don't like
    view output
        opens webpage
        displays missing ingredients
        displays amount you need for the ingredients you have
'''

from retrieve_request import Get_Response
from parse_response import Parse_All, Parse_Single

import webbrowser

def get_ingredients():
    '''
    returns comma separated string of ingredients ready for request 
    '''
    ingredients = ""
    print("Enter ingredients one per line (enter when finished):")
    while True:
        ingredient = input()
        if ingredient:
            ingredients += ingredient.strip().lower() + ','
        else:
            break
    return ingredients[:-1]

def get_next_recipe(all_recipes, rr):
    #id for top of search
    top_rId = all_recipes.get_next_recipe_id() 
    #json response for top search
    json_top_recipe = rr.get_recipe_by_id(top_rId) 
    return json_top_recipe
    
def display(recipe):
    ingredients = recipe.get_ingredients()
    url = recipe.get_source_url()
    for ingredient in ingredients:
        print(ingredient)
    webbrowser.open(url)

def get_all_ingredients(rIds):
    '''
    returns dictionary = {recipe_id: [ingredients]} for single page
    '''
    all_ingredients = {}
    

def app():
    # string of all ingredients 
    ingredients = get_ingredients()
    
    #object to interact with API
    rr = Get_Response(ingredients)
    
    #json response for all recipes given the ingredients 
    json_all = rr.get_all_recipes()
    
    #object to parse all search results
    all_recipes = Parse_All(json_all)
    
    #retrieve all ingredients
#     all_rId = all_recipes.get_all_rId()
    
    while True:
        json_next_recipe = get_next_recipe(all_recipes, rr)
        print(json_next_recipe)
        #object to parse single recipe
        single_recipe = Parse_Single(json_next_recipe)
        question = "Would you like to make: " + single_recipe.get_title() + "?"
        print(question)
        select = input()
        if len(select) != 0:
            break
     
    display(single_recipe)

if __name__ == "__main__":
    app()
    
    
    
    
