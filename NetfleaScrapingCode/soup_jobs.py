# BeautifulSoup is used to extract information from html
from bs4 import BeautifulSoup


def GetProductLinks(soup):
    return soup.findAll("h2", {"class":"product-name"})

def GetProductHref(soup):
    return soup.find("a", href=True)

def GetProductAttributes(soup):
    return soup.findAll(class_="attribute-wrapper")

def GetAttribute(soup, attr):
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

def GetImageName(soup):
    prodImages = soup.find(class_="product-image")
    if prodImages:
        prodImage = prodImages.find("a", {"class": "cloud-zoom"})
        if prodImage:
            return str(prodImage["href"])
        else:
            return ""
    else:
        return ""

def GetNumberPages(soup):
    return soup.findAll(class_="amount")