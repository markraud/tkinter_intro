#! python3
#how to create and use menues with tkinter

from tkinter import *

root = Tk()     
root.title('pack_forget and destroy')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

def fakeCommand():
    pass

# Define a menu
myMenu = Menu(root)
root.config(menu=myMenu)

# Create menu items
fileMenu = Menu(myMenu)
myMenu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=fakeCommand)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.quit)



root.mainloop()