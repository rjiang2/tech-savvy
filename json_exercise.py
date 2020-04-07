import urllib.request
import json
import pprint

APIKEY = 'ca7188570d8b3ef215a52e5b30ae4b83'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'
# url = f'http://api.openweathermap.org/data/2.5/weather?q=Wellesley,us&APPID=ca7188570d8b3ef215a52e5b30ae4b83'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint.pprint(response_data)

# Can you get the current temperature in Wellesley?
print(response_data['main']['temp'])