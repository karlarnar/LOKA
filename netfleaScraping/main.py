# importing other modules
import helper_functions as helper_functions
import scrape_pages as scrape_pages
import scrape_products as scrape_products

########################################################################################

# edit these before running program
# change to True to run scraper for given category
women = True
men = False
kids = False
csvName = "Netflea_Dataset.csv" # name of csv file

# each url for 4each page is the same except for the page number
womenFirstPartLink = "https://www.netflea.com/womens-clothing.html?limit=100&p="
womenNumberOfPages = 1 #595 # ceiling(59429/100)

menFirstPartLink = "https://www.netflea.com/mens-clothing.html?limit=100&p="
menNumberOfPages = 1 #91 # ceiling(9010/100)

#https://www.netflea.com/childrens-clothing.html?limit=100&p=2
kidsFirstPartLink = "https://www.netflea.com/childrens-clothing.html?limit=100&p="
kidsNumberOfPages = 1 #393 # ceiling(39295/100)

########################################################################################

helper_functions.firstCSV(csvName)

if women:
    print("Women scraping beginning...")
    
    scrape_pages.getPageLinks(womenFirstPartLink, womenNumberOfPages, csvName)
    
    print("Women scraping ending...")
    
if men:
    print("Men scraping beginning...")

    scrape_pages.getPageLinks(menFirstPartLink, menSecondPartLink, menNumberOfPages, csvName)
    
    print("Men scraping ending...")

if kids:
    print("Kids scraping beginning...")

    scrape_pages.getPageLinks(kidsFirstPartLink, kidsNumberOfPages, csvName)
    
    print("Kids scraping ending...")

print("All done")