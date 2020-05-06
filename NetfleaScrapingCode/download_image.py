# os used for wget
import os

def WgetImage(url, imagesPath):
    try:
        wgetStr = "wget -P " + str(imagesPath) + " " + url
        os.system(wgetStr)
    except OSError as e:
        print("Failed to wget " + str(imagesPath), e.strerror)
