# requests is used to send requests to a url
# which returns a html response of the url
import requests

# BeautifulSoup is used to extract information from html
from bs4 import BeautifulSoup

def GetSoup(link):
    # setting headers in case the website is checking the header
    headers = requests.utils.default_headers()
    headers.update({ "User-Agent": "Mozilla/5.0 \
        (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/70.0"})

    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup