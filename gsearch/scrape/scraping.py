import requests
import urllib.request
from bs4 import BeautifulSoup
import re
import gsearch.scrape.userAgents as userAgents
import gsearch.results.result as result
def search(headers, query, num_results=10, language="en"):
  escaped_query = query.replace(' ', '+')
  url = f"https://www.google.com/search?q={escaped_query}&num={num_results}&hl={language}"
  request = urllib.request.Request(url)
  request.add_header(
      'User-Agent', headers)

  return urllib.request.urlopen(request).read(), headers, query


def get_results(raw_response, headers, query):
  html = raw_response.decode("utf-8")
  soup = BeautifulSoup(html, 'html.parser')
  # Find all the search result divs
  divs = soup.select("#search div.g")
  responses = []
  spans = soup.find_all(
      'div', class_='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf')
  i = 0
  for links in soup.find_all('div', class_='yuRUbf'):
    # print(links)
    description = ""
    span = spans[i]
    if not span.span is None:
      description = span.span.getText()
    
    temp = result.result(title=links.h3.getText(
    ), url=links.a['href'], description=description, place=i+1,
    # DEBUG PARAMETERS                     
    header = headers, query=query
    )
    responses.append(temp)
    i+=1
  return responses
