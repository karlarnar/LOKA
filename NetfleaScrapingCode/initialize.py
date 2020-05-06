# Path is used to create files on the system
from pathlib import Path

# csv is used to work with csv files
import csv

def InitializeProject(csvName):
    # creating the .csv document and adding the headers
    f = csv.writer(open(csvName, "w"))
    f.writerow(["Type", "Brand", "Colour", "ImgName"])

    # creating an images folder to hold our images
    imagesFolder = Path.cwd().joinpath('images')
    imagesFolder.mkdir(parents=True, exist_ok=True)

    return imagesFolder