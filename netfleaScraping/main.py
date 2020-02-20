# importing other modules
import helper_functions as helper_functions
import scrape_pages as scrape_pages
import scrape_products as scrape_products

########################################################################################

# edit these before running program
# change to True to run scraper for given category
women = True
men = True
boys = True
girls = True
scrapePages = True # if we want to scrape pages
scrapeProducts = True # if we want to scrape products
csvName = "Oxfam_Dataset.csv" # name of csv file

# change the name to reflect on class names
pagesClass = "product-result-item"
attributesClass = "product-attributes clearfix"
imagesClass = "sm sm-product-details-gallery-v2 clearfix image-gallery zoomable"

# each url for 4each page is the same except for the page number
# we will be splitting the url in two, and adding each page number
# in between to loop through them
womenFirstPartLink = "https://www.oxfam.org.uk/shop/womens-clothing/all?i=1;m_sort_shops=FirstMadeLive;page="
womenSecondPartLink = ";q=*;q1=Women%27s;show_all=products;x1=secondary_cat_1"
womenNumberOfPages = 268 # 268 number of pages within category, change to 1 if testing
womenPagesName = "women_pages" # name of txt file to save

menFirstPartLink = "https://www.oxfam.org.uk/shop/mens-clothing/all?i=1;m_sort_shops=FirstMadeLive;page="
menSecondPartLink = ";q=*;q1=men%27s;show_all=products;x1=secondary_cat_1"
menNumberOfPages = 71 # 71 number of pages within category, change to 1 if testing
menPagesName = "men_pages"

girlsFirstPartLink = "https://www.oxfam.org.uk/shop/kids-clothing/girls-clothing?i=1;m_sort_shops=FirstMadeLive;page="
girlsSecondPartLink = ";q=*;q1=Kids;q2=Girls%27+clothing;show_all=products;sp_s=productcreationdate;x1=secondary_cat_1;x2=secondary_cat_2"
girlsNumberOfPages = 4 # 4 number of pages within category, change to 1 if testing
girlsPagesName = "girls_pages"

boysFirstPartLink = "https://www.oxfam.org.uk/shop/kids-clothing/boys-clothing?i=1;m_sort_shops=FirstMadeLive;page="
boysSecondPartLink = ";q=*;q1=Kids;q2=Boys%27+clothing;show_all=products;sp_s=productcreationdate;x1=secondary_cat_1;x2=secondary_cat_2"
boysNumberOfPages = 3 # 3 number of pages within category, change to 1 if testing
boysPagesName = "boys_pages"

########################################################################################

helper_functions.firstCSV(csvName)

if women:
    print("Women scraping beginning...")
    
    # if we need to scrape pages, else skip
    if scrapePages:

        # creating txt file incase we need to go through scrapeProducts again
        helper_functions.createTXT(womenPagesName)
        
        # getting a list of all urls for products
        womenList = scrape_pages.getPageLinks(womenFirstPartLink, womenSecondPartLink, womenNumberOfPages, pagesClass)
        
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

if girls:
    print("Girls scraping beginning...")

    helper_functions.createTXT(girlsPagesName)

    if scrapePages:
        girlsList = scrape_pages.getPageLinks(girlsFirstPartLink, girlsSecondPartLink, girlsNumberOfPages, pagesClass)
        helper_functions.writingListToTXT(girlsPagesName, girlsList)
        print("Scraping pages of girls done")
    
    if scrapeProducts:
        scrape_products.scrapeToCSV(girlsPagesName, attributesClass, imagesClass, csvName)
        print("Scraping products of girls done")
    print("Girls scraping ending...")

if boys:
    print("Boys scraping beginning...")

    helper_functions.createTXT(boysPagesName)

    if scrapePages:
        boysList = scrape_pages.getPageLinks(boysFirstPartLink, boysSecondPartLink, boysNumberOfPages, pagesClass)
        helper_functions.writingListToTXT(boysPagesName, boysList)
        print("Scraping pages of boys done")
    
    if scrapeProducts:
        scrape_products.scrapeToCSV(boysPagesName, attributesClass, imagesClass, csvName)
        print("Scraping products of boys done")
    print("Boys scraping ending...")

print("All done")