#! python3
#how to create a 2nd menu using tkinter

from tkinter import *

root = Tk()     
root.title('Menu Items and stuff')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

def fakeCommand():
    myLabel = Label(root, text='You clicked a menu item.')
    myLabel.pack()

# Define a menu
myMenu = Menu(root)
root.config(menu=myMenu)

# Create menu items
fileMenu = Menu(myMenu)
myMenu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=fakeCommand)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.quit)

# Create another submenu - Edit
editMenu = Menu(myMenu)
myMenu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=fakeCommand) #when you click/choose 'Cut" from the menu it will run the 'fakeCommand' function
editMenu.add_command(label='Copy', command=fakeCommand)
editMenu.add_command(label='Paste', command=fakeCommand)

root.mainloop()