# request module


import requests

r = requests.get("https://www.apartmenttherapy.com/")
print(r.text)

print(r.status_code)