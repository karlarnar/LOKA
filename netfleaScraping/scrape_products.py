# requests is used to send requests to a url
# which returns a html response of the url
import requests

# BeautifulSoup is used to extract information from html
from bs4 import BeautifulSoup

# csv is used to work with csv files, we will use it to read and write to csv
import csv

# our own module
import helper_functions as helper_functions

def scrapeToCSV(link, csvName, imagesPath):
    # opening the csv file
    f = csv.writer(open(csvName, "a"))
    print("Opened csv file")
        
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    
    # find product attributes
    prodAttr = soup.findAll(class_="attribute-wrapper")

    # find type, colour, brand, exact colour, title
    prodType = helper_functions.get_attribute(prodAttr, "Type")
    prodBrand = helper_functions.get_attribute(prodAttr, "Brand")
    prodColour = helper_functions.get_attribute(prodAttr, "Color")
    print("Finding attributes done")
    
    # find image
    prodImages = soup.find(class_="product-image")
    if prodImages:
        prodImage = prodImages.find("a", {"class": "cloud-zoom"})

        if prodImage:
            imgName = str(prodImage["href"])
            helper_functions.wget_image(imgName, imagesPath)
        else:
            imgName = ""
        print("Finding image done")
    else:
        imgName = ""

    # we only want to add the image url if it exists, else return an empty string
    
    
    # writing a new row to csv with new information
    f.writerow([prodType, prodBrand, prodColour, imgName])
    print("Writing row to csv done")

        