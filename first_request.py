import requests 


r = requests.get('http://wikipedia.org')
print r.content 
print r.status_code 