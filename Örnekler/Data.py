
import requests
from bs4 import beatifulSoup

Url = "https://myip.ms/browse/sites/1/own/376714"
R = requests.get(Url)
print(R.text)