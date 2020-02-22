# Beautiful Soup is used to extract information from html
from bs4 import BeautifulSoup

# Path is used to create files on the system
from pathlib import Path

# os used for wget
import os

# csv is used to work with csv files, we will use it now to create the csv
# and adding the header
import csv

def first_CSV(csvName):
    f = csv.writer(open(csvName, "w"))
    f.writerow(["Type", "Brand", "Colour", "ImgName"])
    print("Writing csv headers done")


# get_attribute takes in a soup html and the attribute we want
# to extract information from and returns the value for the attribute
def get_attribute(soup, attr):
    if soup:
        for p in soup:
            prodAttr = p.find("div", string=attr)
            if prodAttr:
                attrVal = p.find("span", {"class": "outeratc"})
                if attrVal:
                    return attrVal.text.strip()
                else:
                    return ""
            else:
                return ""
    else:
        return ""


    

def setting_image_path():
    imagesFolder = Path.cwd().joinpath('images')
    imagesFolder.mkdir(parents=True, exist_ok=True)
    return imagesFolder

def wget_image(url, imagesPath):
    try:
        wgetStr = "wget -P " + str(imagesPath) + " " + url
        os.system(wgetStr)
    except OSError as e:
        print("Failed to wget " + str(imagesPath), e.strerror)