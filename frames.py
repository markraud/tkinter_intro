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

def hide():
    myFrame.grid_forget()

def show():
    myFrame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

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

showButton = Button(root, text='Show', command=show)
hideButton = Button(root, text='hide', command=hide)

showButton.grid(row=0, column=0)
hideButton.grid(row=0, column=1)

myFrame = Frame(root, width=200, height=200, bd=5, bg='blue', relief='sunken')
myFrame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

frameLabel = Label(myFrame, text='Hello World!', font=('Helvetica', 20))
frameLabel.pack(padx=20, pady=20)
root.mainloop()