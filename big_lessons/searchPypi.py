#! python3
# Search and open several tabs

import sys, requests, webbrowser, bs4

print('Search...')
# Get page with requested information
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status() # Get status of request 200 - OK, 4**/5** NOT OK
# Get several links from result ^
soup = bs4.BeautifulSoup(res.text,'html.parser')
linkElems = soup.select('.package-snippet')

# Open several links
numOpen = min(3,len(linkElems))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Open', urlToOpen)
    webbrowser.open(urlToOpen)

#[print (a.getText()) for a in linkElems]

