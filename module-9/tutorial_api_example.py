import requests
import json

#get a response from the API and show the status code
response = requests.get('http://api.open-notify.org/astros.json')
print(response.status_code)
#print(response.json())

#small function to format the API response
def jprint(object):
    text = json.dumps(object, sort_keys=True, indent=4)
    print(text)

#print the response
jprint(response.json())                 