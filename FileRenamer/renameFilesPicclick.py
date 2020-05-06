import os

#generate random integer values
from random import seed
from random import randint

# seed random number generator
seed(1)

folders = ["./picclick-Adidas-Hoodie", "./picclick-Adidas-Tshirt",
		   "./picclick-Nike-Hoodie", "./picclick-Nike-Tshirt"]

currWorkingDir = os.getcwd()

for folder in folders:
	thisFolderPath = os.path.abspath(folder)
	os.chdir(thisFolderPath)

	files = os.listdir(thisFolderPath)
	numberOfFiles = len(files)


	randomNumbers = []
	for _ in range(numberOfFiles):
		val = randint(1000000000, 9999999999)
		randomNumbers.append(val)

	for index, file in enumerate(files):
		oldName = os.path.abspath(file)
		newName = thisFolderPath + "/" + str(randomNumbers[index]) + ".jpg"
		os.rename(oldName, newName)

	os.chdir(currWorkingDir)