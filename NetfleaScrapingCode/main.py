# our modules
import initialize
import run
import print_statements

########################################################################################

# edit these before running program

# change to True to run scraper for given category
women = True
men = True
kids = True

# change this to the name of the dataset
csvName = "Netflea_Dataset.csv"

# "?limit=100&p=" is added to the end so that we can go through 100 products at once
womenCategory = "https://www.netflea.com/womens-clothing.html?limit=100&p="
menCategory = "https://www.netflea.com/mens-clothing.html?limit=100&p="
kidsCategory = "https://www.netflea.com/childrens-clothing.html?limit=100&p="

########################################################################################


# initializing the project and getting the path to the images folder
imagesPath = initialize.InitializeProject(csvName)
print_statements.InitDone()

if women:
    run.Run(womenCategory, csvName, imagesPath)
    print_statements.WomenDone()
    
if men:
    run.Run(menCategory, csvName, imagesPath)
    print_statements.MenDone()

if kids:
    run.Run(kidsCategory, csvName, imagesPath)
    print_statements.KidsDone()

print_statements.ScrapingDone()