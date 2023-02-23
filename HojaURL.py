import requests
link="http://info,cern.ch/"
r=requests.get(link)
html=r.text