#! python3
# Grid Forget - we need to clear out the previous entries because it just writes over the old

from tkinter import *
from PIL import ImageTk, Image

root = Tk()     
root.title('Hello World!')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

# Create open submit function
def submit():
    global helloLabel   # this needs to be global so we can use it in the 'clear' function
    helloLabel = Label(root, text='Hello ' + e.get())
    helloLabel.grid(row=3, column=0)

# Create clear function to erase the helloLabel with either grid_forget or destroy
def clear():
    helloLabel.grid_forget()        #this will hide it and you can bring it back
    # helloLabel.destroy()          #this removes it and you can't get it back(in this case it kinda does the same thing)

# Forget
myLabel = Label(root, text='Enter Your Name:').grid(row=0, column=0)

e = Entry(root)
e.grid(row=1, column=0)

myButton = Button(root, text='Submit', command=submit).grid(row=2, column=0)

clearButton = Button(root, text='Clear', command=clear).grid(row=2, column=1)

root.mainloop()