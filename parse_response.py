'''
classes to parse json response for either 
    entire page of results (Parse_All)
    single recipe information (Parse_Single)
'''

class Parse_All:
    def __init__(self, json_all):
        self.json_all = json_all
        self.current = 0
        
    def get_next_recipe_id(self):
        next_recipe = self.json_all['recipes'][self.current]
        self.current += 1
        return next_recipe['recipe_id']
    

class Parse_Single:
    def __init__(self, json_single):
        self.json_single = json_single
        
    def get_title(self):
        return self.json_single['recipe']['title']
    
    def get_ingredients(self):
        return self.json_single['recipe']['ingredients']
    
    def get_source_url(self):
        return self.json_single['recipe']['source_url']
