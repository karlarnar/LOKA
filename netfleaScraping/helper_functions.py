# Beautiful Soup is used to extract information from html
from bs4 import BeautifulSoup

# Path is used to create files on the system
from pathlib import Path

# csv is used to work with csv files, we will use it now to create the csv
# and adding the header
import csv

def firstCSV(csvName):
    f = csv.writer(open(csvName, "w"))
    f.writerow(["Type", "Brand", "Colour", "ImgName", "ImgSrc"])
    print("Writing csv headers done")


# get_attribute takes in a soup html and the attribute we want
# to extract information from and returns the value for the attribute
def get_attribute(soup, attr):
    
    for p in soup:
        prodAttr = p.find("div", string=attr)
        if prodAttr:
            attrVal = p.find("span", {"class": "outeratc"})
            if attrVal:
                return attrVal.text.strip()
            else:
                return ""

def createTXT(fileName):
    txtName = fileName + ".txt"
    txtPath = Path(txtName)
    txtPath.touch(exist_ok=True)

def writingListToTXT(fileName, lst):
    txtName = fileName + ".txt"
    with open(txtName, "a") as f:
        for l in lst: 
            f.write("%s\n" % l)
    print("Writing list to " + txtName + " done")

def txtToList(fileName):
    retList = []
    txtName = fileName + ".txt"
    with open(txtName, "r") as f:
        for line in f:
            currLine = line[:-1] # removing linebreak
            retList.append(currLine)
    return retList