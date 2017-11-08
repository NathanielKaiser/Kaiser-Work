from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/2.0 (compatible; MSIE 3.03; Windows 3.1)'}
requestedhtml = requests.get("http://time.is", headers = headers)
soup = BeautifulSoup(requestedhtml.content, 'html.parser')

timediv = soup.find(id="twd")

print "time according to time.is |", timediv.text, "|"
