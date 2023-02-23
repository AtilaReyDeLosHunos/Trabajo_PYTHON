import requests
link="http://info.cern.ch/"
r=requests.get(link)
print(r.status_code)
html=r.text