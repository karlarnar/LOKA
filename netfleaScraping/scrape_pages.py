# requests is used to send requests to a url
# which returns a html response of the url
import requests

# BeautifulSoup is used to extract information from html
from bs4 import BeautifulSoup

def getPageLinks(firstPartLink, numberPages, pagesClass):
    # setting headers in case the website is checking the header
    headers = requests.utils.default_headers()
    headers.update({ "User-Agent": "Mozilla/5.0 \
        (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/70.0"})

    retList = []

    for page in range(1, numberPages + 1):

        # we will need to build a link that represents the url
        link = firstPartLink + str(page)

        # we will need to send a request to that page and
        # get back a html response, we will use BeautifulSoup
        # to search the html for any href link within the class
        # we defined in pagesClass, which will be a link to the
        # product page of an item.
        response = requests.get(link)
        html = response.content
        soup = BeautifulSoup(html, "html.parser")

        for link in soup("a", "product-image", href=True):
            retList.append(link["href"])

        print("All links added for page " + str(page))
    print("All links added to list, returning list")
    return retList