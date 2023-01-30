import requests
from bs4 import BeautifulSoup
import re
from userAgents import userAgents 
def run():
  
  search= "geeksforgeeks"
  results = 20
  html = requests.get("https://www.google.com/search?q="+search+f"&num={results}")
  soup = BeautifulSoup(html.text, 'lxml')
  print("running")
  for result in soup.select('.tF2Cxc'):
    title = result.select_one('.DKV0Md').text
    link = result.select_one('.yuRUbf a')['href']
  
    print(title, link, sep='\n')