import json

class JsonHandler():
    def __init__(self,json_path):
        self.json_path = json_path
        

    def read_json(self):
        with open(self.json_path, 'r') as file:
            data = json.load(file)
        return data
    
    
