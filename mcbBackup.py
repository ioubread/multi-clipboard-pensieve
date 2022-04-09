from pathlib import Path
import os
import shelve
import datetime

# Possible adjustments
parentFolderOfBackups = "MCB-Backup-Folders"
prefixOfDatedSave = "MCB-Backup-"

# Getting today's date
td = datetime.datetime.today()
stringDateToday = (str(td.year)[-2:]) + str(td.month).rjust(2, "0") + str(td.day).rjust(2, "0")

# Directory management
originalDir = Path.cwd()
folderToBackup = Path(parentFolderOfBackups) / Path(str(prefixOfDatedSave) + stringDateToday)
Path(folderToBackup).mkdir(parents=True, exist_ok=True)
toFolder = Path.home() / Path('pythonData')
os.chdir(toFolder)

# Opening up existing save data
myShelf = shelve.open('mcb')

# Preparing naming of keys
lengthOfDict = str(len(myShelf))
charLenForIndex = len(str(lengthOfDict))

# Looping through key items
counter = 0
for key in myShelf:
    counter += 1

    # Creating padded key
    keyCounter = str(counter)
    paddedKey = str(keyCounter).rjust(charLenForIndex, "0")
    keyName = key
    theContent = myShelf[keyName]

    # Creating filename and filedirectory to save to
    fileNameToSaveTo = str(paddedKey) + "-" + str(keyName) + ".txt"
    filenameAndDirectoryPath = originalDir / folderToBackup / Path(fileNameToSaveTo)

    # Saving the data
    theSaveFile = open(filenameAndDirectoryPath, "w", encoding="utf-8")
    theSaveFile.write(theContent)
    theSaveFile.close()


# Closing up the program
os.chdir(originalDir)
myShelf.close()