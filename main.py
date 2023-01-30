from gsearch.scrape import scraping
from gsearch.scrape import userAgents
raw = scraping.search(headers=userAgents._getUserAgent(), query="Where do I get chocolate milk?")
output = scraping.get_results(raw[0], raw[1], raw[2])
for result in output:
    print(result.title)
    print(result.url)
    print(result.description)
    print("---")
    print(result.toJson())
    print(result.header)
    print(result.query)