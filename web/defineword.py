from bs4 import BeautifulSoup
import requests

word = raw_input("Enter word to find its meaning: ")
url = "https://www.google.com/search?q=" + word +  "+define"

headers = {'User-Agent': 'Mozilla/2.0 (compatible; MSIE 3.03; Windows 3.1)'}
requestedhtml = requests.get(url, headers = headers)
soup = BeautifulSoup(requestedhtml.content, 'html.parser')

for div in soup.find_all(True):
    print div.text


#from the wikipedia article "car" 
#class="div-col columns column-width"



#find_all(attrs={"data-dobid": "dfn", "style": "display:inline"})

#query format google
#https://www.google.com/search?q= word +define
#location of div with defintion
#<div style="display:inline" data-dobid="dfn"> </div>
