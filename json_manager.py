import json
import os


def read_json():
    if not os.path.isfile('contactos.json'):
        with open('contactos.json','w') as f:
            json.dump([], f)
    with open('contactos.json', 'r') as f:
        data = json.load(f)    
    return data



def write_json(data):    
    with open('contactos.json', 'w') as f:
        json.dump(data, f)