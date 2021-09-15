import tkinter
from tkinter import *
from tkinter import filedialog as fd
import os
import datetime as dt
import time
import shutil
    
def fileCheckTransfer(): #method for transfering files modified in last 24 hours in one folder to another
    today = time.time() #gets epoch for os time
    todayhours = today / 3600 #converts seconds to hours
    CheckedFolder = txtBox1.get()+'/' #without this the file path will combine the folder and file name without the needed '/' in between
    destination = txtBox2.get()+'/'    #without this the file path will combine the folder and file name without the needed '/' in between
    for file in os.listdir(CheckedFolder):
        filemod = os.path.getmtime(CheckedFolder + file) #getting time for files in CheckedFolder
        filehours = filemod / 3600  #converts to hours
        difference = todayhours - filehours #the difference will tell us how long since last modification time in hours
        
        
        if difference < 24: #if last mod was less than 24 hours ago, do the following to move the file
           shutil.move(CheckedFolder+file, destination)




def folderToCheck():          #method that will allow user to select folder and path will be given to var CheckedFolder
    CheckedFolder = fd.askdirectory()
    txtBox1.delete(0,END) #This allows us to run program multiple times without having to exit out over and over
    txtBox1.insert(END,CheckedFolder) #this will put the folder path in the entry space
    
def ReceivingFolder(): #method that will allow user to select folder and path will be given to var destination
    destination = fd.askdirectory()
    txtBox2.delete(0,END)     #This allows us to run program multiple times without having to exit out over and over
    txtBox2.insert(END,destination)  #this will put the folder path in the entry space
    
window = Tk()


window.resizable(width=False, height=False) #user will not be able to resize
window.geometry('{}x{}'.format(700, 400)) #size will be 700 by 400
window.title('Learning Tkinter!')
window.config(bg = 'lightgray') #makes background (bg) light gray

btnSubmit = Button(window, text='Checked folder', width=15, height=2, command=folderToCheck) #button that uses folderToCheck method
btnSubmit.grid(row=0, column=0,padx=(0,0), pady=(30,0), sticky=NE)

btnSubmit = Button(window, text='Receiving folder', width=15, height=2, command=ReceivingFolder) #button that uses ReceivingFolder method
btnSubmit.grid(row=0, column=1,padx=(0,0), pady=(30,0), sticky=NE)

btnSubmit = Button(window, text='Initiate file check', width=15, height=2, command=fileCheckTransfer) #button that uses fileCheckTransfer method
btnSubmit.grid(row=0, column=2,padx=(0,0), pady=(30,0), sticky=NE)

txtBox1 = Entry(window, font=('Helvetica', 16), width=30) #entry that will hold file path from 'checked folder' button
txtBox1.grid(row=1, column=0,padx=(0,0), pady=(40,0))

txtBox2 = Entry(window, font=('Helvetica', 16), width=30) #entry that will hold file path from 'receiving folder' button
txtBox2.grid(row=2, column=0,padx=(0,0), pady=(40,0))

        




    
    




if __name__ == "__main__":
    window.mainloop()




        

    
