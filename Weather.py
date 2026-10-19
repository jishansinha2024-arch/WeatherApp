import requests
import json
city = input("Enter the city name: ")
url = f"https://api.weatherapi.com/v1/current.json?key=5280303dac7546038f6140544261910&q={city}"
r = requests.get(url)
print(r.text)
wdict = json.loads(r.text)
print(f"City: {wdict['location']['name']}")
print(f"Temperature: {wdict['current']['temp_c']}°C")
print(f"Condition: {wdict['current']['condition']['text']}")