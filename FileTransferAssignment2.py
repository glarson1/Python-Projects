import os
import datetime as dt
import time
import shutil

today = time.time()
todayhours = today / 3600







FolderA ='C:/Users/gabri/OneDrive/Documents/GitHub/Python-Projects/FolderA/'

destination = 'C:/Users/gabri/OneDrive/Documents/GitHub/Python-Projects/FolderB/'

for file in os.listdir(FolderA):
    filemod = os.path.getmtime(FolderA + file)
    filehours = filemod / 3600
    difference = todayhours - filehours
    #print(difference, file)
    
    if difference < 24:
       shutil.move(FolderA+file, destination)

