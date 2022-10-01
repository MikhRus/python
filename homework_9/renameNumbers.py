import os, re, shutil
from tokenize import group


def findFiles(folder):
    filenameRegex = re.compile(r'^(.*?)(\d{3})(.*?)$')    # Regex for find files with name 
                                                # <somethink>000<somethink>
    previousFile = None # Name of previous file
    currentFile = None  # Get filename via Regex
    for file in sorted(os.listdir(folder)):
        currentFile = filenameRegex.search(file) # Get filename via Regex
        if currentFile == None:         # Skip files without numbers
            continue
        if previousFile == None:        # If this file first - save name
            previousFile = currentFile
            continue
        else:
            if int(currentFile.group(2)) > int(previousFile.group(2)) + 1:
                newName = currentFile.group(1) + \
                    str(int(previousFile.group(2)) + 1).zfill(3) + \
                        currentFile.group(3)
                oldFilename = os.path.join(folder, currentFile.group()) 
                newFilename = os.path.join(folder, newName)           
                shutil.move(oldFilename, newFilename)
                previousFile = filenameRegex.search(newFilename)
            else:
                previousFile = currentFile
                continue

        #print(str(int(name.group(2))+1).zfill(3))

findFiles('/home/mikhail/Desktop/Learning/python/homework_9/files/')