import webbrowser
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

       


        self.txtBody = Entry(self.master,text='', font=('Helvetica', 16)) #this is where the user will input what they want in the body of their webpage
        self.txtBody.grid(row=0, column=1,padx=(30,0), pady=(30,0))            #formatting for location of the input

        self.btnSubmit = Button(self.master, text='Submit and create', width=15, height=2, command= self.getText) #This creates a button that will take the input and create a webpage with it included
        self.btnSubmit.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NE) #location formatting


    def getText(self): #created a function that will be added to the button
       
        f = open("basic.html", "w") #this will create a file named basic.html if one does not already exits. 'w' stands for write
        body = "<html><body><h1>Stay tuned for our amazing summer sale!</h1>{}</body></html>".format(self.txtBody.get()) #created a variable that is going to tbe the layout for the html with
        f.write(body)                                                                                                #a {} for the string the user inputted to go using .format
        f.close()
        
        basicHTML = 'C:/Users/gabri/OneDrive/Documents/GitHub/Python-Projects/basic.html' #this is the path the newly created .html will be at

        webbrowser.open_new_tab(basicHTML) #this will open the basic.html in a new tab in browser



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
