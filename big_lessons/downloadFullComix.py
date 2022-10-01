#! python3
# Download full comic from XKCD.com

import bs4, webbrowser, requests, os


url = 'https://xkcd.com/'

os.makedirs('/home/mikhail/Desktop/Learning/python/big_lessons/xkcd', exist_ok=True)

while not url.endswith('#'):
    # Get last page of comic
    res = requests.get(url)
    res.raise_for_status()
    # Parsing site
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Search URL of image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("Image of comic dosn't find")
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download image
        print(f'Download image {comicUrl}...')
        res = requests.get(comicUrl)
        res.raise_for_status()
        # Save image file in xkcd folder
        imageFile = open(os.path.join('/home/mikhail/Desktop/Learning/python/big_lessons/xkcd', \
            os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    # Get URL of prev button
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done!')