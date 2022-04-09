from pathlib import Path
import os
import shelve

# Possible adjustments
folderOfBackups = "MCB-Backup-Folders"
toFolder = Path.home() / Path('pythonData')

# Directory management
originalDir = Path.cwd()
directoryOfFolders = sorted(os.listdir(folderOfBackups))
latestSavefileOfMCB = directoryOfFolders[-1]
directoryToLatestSavefile = Path(folderOfBackups) / Path(latestSavefileOfMCB)

# Getting all save files
allSavefiles = sorted(os.listdir(directoryToLatestSavefile))

# Starting dictionary for MCB
myShelfSavedata = dict()

# Looping through save files
for filename in allSavefiles:

    # Name management
    reversedFilename = filename[::-1]
    reversedFilenameWithoutExtension = (reversedFilename.partition("."))[2]
    filenameWithoutExtension = reversedFilenameWithoutExtension[::-1]
    filenameFinal = (filenameWithoutExtension.partition("-"))[2]

    # Getting content
    theFile = open(str(directoryToLatestSavefile / Path(filename)), encoding='utf-8', mode='r')
    theContent = theFile.read()
    theFile.close()
    
    # Saving it to prepared myShelf data
    myShelfSavedata[filenameFinal] = theContent

# Opening up Shelve
os.chdir(toFolder)
myShelf = shelve.open('mcb')

# Saving into myShelf
for key, value in myShelfSavedata.items():
    myShelf[key] = value

# Closing the program
myShelf.close()