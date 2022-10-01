
import os


def findLargeFiles(folder):
    items = []
    for foldername, subfolders, filenames in os.walk(folder):
        if os.path.getsize(foldername) > 100000000:
            items.append(foldername)
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername,filename)) > 100000000:
                items.append(filename)
    for item in items:
        print(f'Size of {item} over then 100Mb.')

findLargeFiles('/home/mikhail/Downloads/')