# requests is used to send requests to a url
# which returns a html response of the url
import requests

# BeautifulSoup is used to extract information from html
from bs4 import BeautifulSoup

# math module used for ceiling function
import math

# our modules
import send_request_to_website
import soup_jobs

def GetPageNumber(link):
    soup = send_request_to_website.GetSoup(link)
	
    findNumberInSoup = soup_jobs.GetNumberPages(soup)
	
    # findNumberInSoup will return all text where the class
    # amount is found, therefore we can choose the first one
    numberAmount = findNumberInSoup[0].text.strip().split(" ")

    # since we split the text, we know that the number is the sixth
    # item in the split text, we also know that there are 100 product
    # listings on each page, so we can find the pages number by taking
    # the ceiling of that number
    return math.ceil(int(numberAmount[5]) / 100)