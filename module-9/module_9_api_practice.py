'''
Ben Bode
CSD 325 week 9
assignment 9.2
2/20/2026
This code is designed to explore the ins and outs of API use. 
It is based on code from the tutorial found here:
https://www.dataquest.io/blog/api-in-python/
'''

import requests
import json

#list of pramaters we can change if we want, limit how many entries we see
params = {
    'limit':10
}

#call API, check response code and get raw data
response = requests.get('https://swapi.dev/api/starships/',params=params)
print(response.status_code)
print(response.json())

#print formatted data
text = json.dumps(response.json(), sort_keys=True, indent=4)
print(text)