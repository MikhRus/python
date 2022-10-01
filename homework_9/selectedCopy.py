#! python3
# Copy only .py files into new folder

import os, shutil, re
from pathlib import Path

filePattern = re.compile(r'.*\.py')


def copyFiles(folder):
    newFolder = Path(folder) / 'Only .py files'
    newFolder.mkdir(parents=True, exist_ok=True)
    for foldername, subfolders, filenames in os.walk(folder):
        #currentDir = os.path.basename(foldername)
        #test = currentDir.startswith('Only .py files')
        if os.path.basename(foldername).startswith('Only .py files'):
            continue 
        print(f'Looking in {foldername}...')
        # Find .py files
        for filename in filenames:
            file = filePattern.search(filename)
            if file == None:
                continue
            print(f'File {filename} copied...')
            oldPath = os.path.join(os.path.abspath(foldername),filename)   #os.path.abspath(foldername)          
            newPath = os.path.join(os.path.abspath(newFolder),filename)     
            shutil.copy(oldPath, newPath)
    print('Done!')

copyFiles('/home/mikhail/Desktop/Learning/python/')
