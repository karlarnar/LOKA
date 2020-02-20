# requests is used to send requests to a url
# which returns a html response of the url
import requests

# BeautifulSoup is used to extract information from html
from bs4 import BeautifulSoup

# csv is used to work with csv files, we will use it to read and write to csv
import csv

# our own module
import helper_functions as helper_functions

def scrapeToCSV(txtName, attributeClass, imageClass, csvName):

    # opening the csv file
    f = csv.writer(open(csvName, "a"))
    print("Opened csv file")

    # getting the txt file we created in scrape_pages to list so we can loop through it
    lst = helper_functions.txtToList(txtName)
    for product in lst:
        print(product)
        page = requests.get(product)
        soup = BeautifulSoup(page.text, "html.parser")

        # find product attributes
        prodAttr = soup.find(class_=attributeClass)

        # find type, colour, brand, exact colour, title
        prodType = helper_functions.get_attribute(prodAttr, "Type:")
        prodColour = helper_functions.get_attribute(prodAttr, "Colour:")
        prodBrand = helper_functions.get_attribute(prodAttr, "Brand:")
        prodExactColour = helper_functions.get_attribute(prodAttr, "Exact colour:")
        prodTitle = helper_functions.get_attribute(prodAttr, "Title:")
        print("Finding attributes done")

        # find image
        prodImages = soup.find(class_=imageClass)
        prodImage = prodImages.findAll("img")
        prodImageName = ""
        
        # we only want to add the image url if it exists, else return an empty string
        if prodImage:
            for image in prodImage:
                imgStr = str(image["src"])

                # we want the main image, not the thumbnail image
                if "/Main/" in imgStr:

                    # adding https: to the string, to get the full url
                    prodImage = "https:" + imgStr

                    # getting the name which will be the same as image name
                    prodImageName = "HD_" + prodImage.split("HD_")[1]
        else:
            prodImage = ""
        print("Finding image done")

        # writing a new row to csv with new information
        f.writerow([prodType, prodColour, prodBrand, prodExactColour, prodTitle, prodImageName, prodImage])
        print("Writing row to csv done")