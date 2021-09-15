import shutil
import os

#set where the source of the files are
source = 'C:/Users/gabri/OneDrive/Desktop/FolderA/'

#set the destination path to folderB
destination = 'C:/Users/gabri/OneDrive/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
