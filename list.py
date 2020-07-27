import os
import sys

def list_files(startpath):
    writeToFile = open('musicList.md', 'w')
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)

        # If it has only 1 / that means that it is a parent dir and is an artist folder
        if (root.count('/')) == 1:
            print('{}{}/'.format(indent + "Artist: ", os.path.basename(root)), file = writeToFile)
        else:
            # otherwise it is an album folder
            print('{}{}/'.format(indent + "Album: ", os.path.basename(root)), file = writeToFile)

        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f), file = writeToFile)

    writeToFile.close()

list_files('./')
