import requests
import json

# response = requests.get("http://api.open-notify.org/iss-now.json")
# astros = requests.get("http://api.open-notify.org/astros.json")

# print response.content
# data = response.json()
# print(data['iss_position']['longitude'])

# data = astros.json()
# print data["number"]

response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyAWjT2xJUE1ylIMoPZF4LlZil1zP2ayeuA")

data = response.json()
print data['results'][0]["address_components"][2]["long_name"]