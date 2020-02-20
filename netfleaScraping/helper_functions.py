# Beautiful Soup is used to extract information from html
from bs4 import BeautifulSoup

# Path is used to create files on the system
from pathlib import Path

# csv is used to work with csv files, we will use it now to create the csv
# and adding the header
import csv

def firstCSV(csvName):
    f = csv.writer(open(csvName, "w"))
    f.writerow(["Type", "Brand", "Colour", "Img name", "Img src"])
    print("Writing csv headers done")


# get_attribute takes in a soup html and the attribute we want
# to extract information from and returns the value for the attribute
def get_attribute(soup, attr):
    """
    # finding attribute within dt tag
    prodAttr = soup.find("dt", string=attr)
    retAttr = ""

    # if there is no attribute, then we will return an empty string
    if prodAttr:

        # if we find the attribute, we want to find the dd tag for that
        # attribute, which is the value for that attribute
        siblings = prodAttr.find_next_siblings("dd")

        # find_next_siblings returns a list of all siblings that come
        # after the dt tag, we only want the first one
        sibling = siblings[0]

        # we want to cut out the <dt> and </dt>
        retAttr = str(sibling)[4:-5]
    return retAttr
    """

def createTXT(fileName):
    txtName = fileName + ".txt"
    txtPath = Path(txtName)
    txtPath.touch(exist_ok=True)

def writingListToTXT(fileName, lst):
    txtName = fileName + ".txt"
    with open(txtName, "a") as f:
        for l in lst: 
            f.write("https://www.netflea.com%s\n" % l)
    print("Writing list to " + txtName + " done")

def txtToList(fileName):
    retList = []
    txtName = fileName + ".txt"
    with open(txtName, "r") as f:
        for line in f:
            currLine = line[:-1] # removing linebreak
            retList.append(currLine)
    return retList