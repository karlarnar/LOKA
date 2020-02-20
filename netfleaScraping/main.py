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
scrapePages = False # if we want to scrape pages
scrapeProducts = True # if we want to scrape products
csvName = "Netflea_Dataset.csv" # name of csv file

# change the name to reflect on class names
pagesClass = "item"
attributesClass = "attribute-wrapper"
imagesClass = "product-image"

# each url for 4each page is the same except for the page number
womenFirstPartLink = "https://www.netflea.com/womens-clothing.html?limit=100&p="
womenNumberOfPages = 1 #595 # ceiling(59429/100)
womenPagesName = "women_pages" # name of txt file to save

menFirstPartLink = "https://www.netflea.com/mens-clothing.html?limit=100&p="
menNumberOfPages = 1 #91 # ceiling(9010/100)
menPagesName = "men_pages"

#https://www.netflea.com/childrens-clothing.html?limit=100&p=2
kidsFirstPartLink = "https://www.netflea.com/childrens-clothing.html?limit=100&p="
kidsNumberOfPages = 1 #393 # ceiling(39295/100)
kidsPagesName = "kids_pages"

########################################################################################

helper_functions.firstCSV(csvName)

if women:
    print("Women scraping beginning...")
    
    # if we need to scrape pages, else skip
    if scrapePages:

        # creating txt file incase we need to go through scrapeProducts again
        helper_functions.createTXT(womenPagesName)
        
        # getting a list of all urls for products
        womenList = scrape_pages.getPageLinks(womenFirstPartLink, womenNumberOfPages, pagesClass)
        
        # writing to txt file we created earlier
        helper_functions.writingListToTXT(womenPagesName, womenList)
        print("Scraping pages of women done")
    
    # if we need to scrape products, else skip
    if scrapeProducts:

        # looping through products and writing attributes to csv file
        scrape_products.scrapeToCSV(womenPagesName, attributesClass, imagesClass, csvName)
        print("Scraping products of women done")
    print("Women scraping ending...")
    
if men:
    print("Men scraping beginning...")

    helper_functions.createTXT(menPagesName)

    if scrapePages:
        menList = scrape_pages.getPageLinks(menFirstPartLink, menSecondPartLink, menNumberOfPages, pagesClass)
        helper_functions.writingListToTXT(menPagesName, menList)
        print("Scraping pages of men done")
    
    if scrapeProducts:
        scrape_products.scrapeToCSV(menPagesName, attributesClass, imagesClass, csvName)
        print("Scraping products of men done")
    print("Men scraping ending...")

if kids:
    print("Kids scraping beginning...")

    helper_functions.createTXT(kidsPagesName)

    if scrapePages:
        kidsList = scrape_pages.getPageLinks(kidsFirstPartLink, kidsNumberOfPages, pagesClass)
        helper_functions.writingListToTXT(kidsPagesName, kidsList)
        print("Scraping pages of kids done")
    
    if scrapeProducts:
        scrape_products.scrapeToCSV(kidsPagesName, attributesClass, imagesClass, csvName)
        print("Scraping products of kids done")
    print("Kids scraping ending...")

print("All done")