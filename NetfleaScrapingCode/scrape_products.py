# requests is used to send requests to a url
# which returns a html response of the url
import requests

# BeautifulSoup is used to extract information from html
from bs4 import BeautifulSoup

# csv is used to work with csv files, we will use it to read and write to csv
import csv

# our modules
import send_request_to_website
import soup_jobs
import download_image

def ScrapingProduct(productLink, csvName, imagesPath):
    # opening the csv file that we created earlier
    f = csv.writer(open(csvName, "a"))

    soup = send_request_to_website.GetSoup(productLink)
    
    # find all product attributes
    prodAttr = soup_jobs.GetProductAttributes(soup)

    # find type, brand and colour within all product attributes
    prodType = soup_jobs.GetAttribute(prodAttr, "Type")
    prodBrand = soup_jobs.GetAttribute(prodAttr, "Brand")
    prodColour = soup_jobs.GetAttribute(prodAttr, "Color")
    
    # find image
    # we only want to add the image url if it exists, else return an empty string
    imgName = soup_jobs.GetImageName(soup)

    # if there is an image we want to download it
    if imgName:
        download_image.WgetImage(imgName, imagesPath)

    # writing the tags to our .csv document
    f.writerow([prodType, prodBrand, prodColour, imgName])

        