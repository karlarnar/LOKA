# our modules
import get_page_number
import send_request_to_website
import scrape_products
import soup_jobs
import print_statements


def Run(category, csvName, imagesPath):

    # getting the total pages to scrape
    totalPages = get_page_number.GetPageNumber(category)

    for page in range(1, totalPages + 1):
        pageToCheck = category + str(page)

        soup = send_request_to_website.GetSoup(pageToCheck)

        prodLinks = soup_jobs.GetProductLinks(soup)

        if prodLinks:
            # scraping product one by one
            for idx, p in enumerate(prodLinks):
                prodHref = soup_jobs.GetProductHref(p)

                if prodHref:
                    scrape_products.ScrapingProduct(prodHref["href"], csvName, imagesPath)

                print_statements.PrintProductNumberDone(idx + 1, page, totalPages)

        print_statements.PrintPageNumberDone(page, totalPages)