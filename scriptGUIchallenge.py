import tkinter
from tkinter import *
from tkinter import filedialog
fd = filedialog

class ParentWindow(Frame): #Frame is the parent class within tkinter
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True) 
        self.master.geometry('{}x{}'.format(700, 200)) 
        self.master.title('Check files')
        
        self.btnBrowse1 = Button(self.master, text='Browse...', width=15, height=1, command=showPath)
        self.btnBrowse1.grid(row=0, column=0,padx=(20,0), pady=(40,0))


        self.btnBrowse2 = Button(self.master, text='Browse...', width=15, height=1, command='')
        self.btnBrowse2.grid(row=1, column=0,padx=(20,0), pady=(50,0))

        self.btnCheck = Button(self.master, text='Check for files...', width=15, height=3, command='')
        self.btnCheck.grid(row=2, column=0,padx=(20,0), pady=(60,0))

        self.btnClose = Button(self.master, text='Close Program', width=15, height=3, command='')
        self.btnClose.grid(row=2, column=1,padx=(100,0), pady=(55,0))

        self.txtBox1 = Entry(self.master,text='', font=('Helvetica', 16), width=30,)
        self.txtBox1.grid(row=0, column=1,padx=(20,0), pady=(40,0))

        self.txtBox2 = Entry(self.master,text='', font=('Helvetica', 16), width=30,)
        self.txtBox2.grid(row=1, column=1,padx=(20,0), pady=(40,0))



def showPath():
    path = fd.askdirectory()
    print(path)






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)

