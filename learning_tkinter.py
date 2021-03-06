import tkinter
from tkinter import *


class ParentWindow(Frame): #Frame is the parent class within tkinter
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False) #user will not be able to resize
        self.master.geometry('{}x{}'.format(700, 400)) #size will be 700 by 400
        self.master.title('Learning Tkinter!')
        self.master.config(bg = 'lightgray') #makes background (bg) light gray

        self.varFname = StringVar()
        self.varLname = StringVar()

        self.lblFname = Label(self.master,text='First Name: ', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblFname.grid(row=0, column=0,padx=(30,0), pady=(30,0))

        self.lblLname = Label(self.master,text='Last Name: ', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblLname.grid(row=1, column=0,padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=('Helvetica', 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))
        
        self.txtFname = Entry(self.master,text=self.varFname, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtFname.grid(row=0, column=1,padx=(30,0), pady=(30,0))

        self.txtLname = Entry(self.master,text=self.varLname, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtLname.grid(row=1, column=1,padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text='Cancel', width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFname.get()
        ln = self.varLname.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy()




















if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #mainloop makes sure it continuously runs until we decide to close or quit
