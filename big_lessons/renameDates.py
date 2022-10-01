#! python3
# Rename files with US date format MM-DD-YYYY to EU format DD-MM-YYYY
import os, shutil, re

# Create regex for finding files with US format date
datePattern = re.compile(r"""^(.*?) # text before date
    ((0|1)?\d)-     # month regex
    ((0|1|2|3)?\d)- # day regex
    ((19|20)\d\d)   # year regex
    (.*?)$          # text after date
""", re.VERBOSE)

# Cycle for finding files in current dir

for amerFilename in os.listdir('./big_lessons/dateFiles/'):
    mo = datePattern.search(amerFilename) # look into filename with regex

    if mo == None: # If filename doesn't exist date - skip
        continue
    # Getting parts of filename
    #allGropus = mo.groups()
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Create new filenames with EU date format 
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # Getting absolute path
    absWorkingDir = os.path.abspath('./big_lessons/dateFiles/')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # Rename file
    print(f'\n"{amerFilename}" renamed to "{euroFilename}"...')
    shutil.move(amerFilename, euroFilename)




