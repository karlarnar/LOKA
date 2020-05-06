def ScrapingDone():
    print("Scraping Netflea is done...")

def InitDone():
    print("Initialization of the project is done...")

def WomenDone():
    print("Scraping the women category is done...")

def MenDone():
    print("Scraping the men category is done...")

def KidsDone():
    print("Scraping the kids category is done...")

def PrintPageNumberDone(pageNumber, totalPages):
    print("Scraping for page #" + str(pageNumber) + " of " + str(totalPages) + " pages done...")

def PrintProductNumberDone(prodNumber, pageNumber, totalPages):
    print("Scraping product #" + str(prodNumber) + " of 100 in page #" + str(pageNumber) + " of "\
          + str(totalPages) + " pages done...")