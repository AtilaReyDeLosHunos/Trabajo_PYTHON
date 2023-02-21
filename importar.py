import requests
currency="eur"
basecurrency="aud"
url = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + currency + "&f=" + basecurrency + "&v=1&s=cbr"
resp=requests.get(url)
print(resp.text)
print(resp.json())
