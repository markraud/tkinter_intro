#! python3
#how to create a 2nd menu using tkinter

from tkinter import *

root = Tk()     
root.title('Menu Items and stuff')
# root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

def fakeCommand():
    myLabel = Label(root, text='You clicked a menu item.')
    myLabel.pack()

def new():
    hideMenuFrames()
    currentStatus.set('File Status')
    fileFrame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

def hide():
    fileFrame.grid_forget()

def show():
    fileFrame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

def cut():
    hideMenuFrames()
    currentStatus.set('Cut Status')
    editFrame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

def hideMenuFrames():
    editFrame.grid_forget()
    fileFrame.grid_forget()

# Define a menu
myMenu = Menu(root)
root.config(menu=myMenu)

# Create menu items
fileMenu = Menu(myMenu)
myMenu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=new)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.quit)

# Create another submenu - Edit
editMenu = Menu(myMenu)
myMenu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut) #when you click/choose 'Cut" from the menu it will run the 'fakeCommand' function
editMenu.add_command(label='Copy', command=fakeCommand)
editMenu.add_command(label='Paste', command=fakeCommand)


# File Menu Frame
fileFrame = Frame(root, width=200, height=200, bd=5, bg='blue', relief='sunken')
# fileFrame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

frameLabel = Label(fileFrame, text='File Frame', font=('Helvetica', 20))
frameLabel.pack(padx=20, pady=20)

# Edit Menu Frame
editFrame = Frame(root, width=200, height=200, bd=5, bg='blue', relief='sunken')
# fileFrame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

editFrameLabel = Label(editFrame, text='Cut Frame', font=('Helvetica', 20))
editFrameLabel.pack(padx=20, pady=20)

currentStatus = StringVar()     #StringVar is a special type of variable that is a function - tkinter specific - this can update in realtime
currentStatus.set('Waiting')

myStatus = Label(root, textvariable=currentStatus, bd=2, relief='sunken', width=56, anchor='e')
myStatus.grid(row=1, column=0)

root.mainloop()