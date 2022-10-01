#! python3
# Create backup zip-file with increment number of copy. Copy all files in this archive

import zipfile, os

def backupToZip(folder):
    # Create backup all files from "folder" into ZIP-file
    folder = os.path.abspath(folder) # only absolyte path

    # Determining correct name of folder for function
    number = 1 
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'

        if not os.path.exists(zipFilename):
            break
        number = number + 1 

    print(f'Create new ZIP-file {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files form {foldername}...')
        # Add into ZIP-file current folder
        backupZip.write(foldername)

        # Add into ZIP-file all files from current folder
        for filename in filenames:
            newBase = os.path.basename(filename)
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # Dont copy archive ZIP-files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
backupToZip('/home/mikhail/Desktop/Learning/python/big_lessons')