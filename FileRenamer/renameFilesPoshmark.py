import os

#generate random integer values
from random import seed
from random import randint

# seed random number generator
seed(1)

folders = ["./Poshmark-adidas-hoodie", "./Poshmark-adidas-tshirt",
		   "./Poshmark-nike-hoodie", "./Poshmark-nike-tshirt"]

currWorkingDir = os.getcwd()

for folder in folders:
	thisFolderPath = os.path.abspath(folder)
	os.chdir(thisFolderPath)

	files = os.listdir(thisFolderPath)
	numberOfFiles = len(files)


	randomNumbers = []
	for _ in range(numberOfFiles):
		val = randint(10000, 99999)
		randomNumbers.append(val)

	for index, file in enumerate(files):
		oldName = os.path.abspath(file)
		newName = thisFolderPath + "/" + str(randomNumbers[index]) + ".jpg"
		os.rename(oldName, newName)

	os.chdir(currWorkingDir)