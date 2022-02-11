#! python3

from cgitb import text
from select import select
from tkinter import *
from tkinter import ttk

root = Tk()     
root.title('Check Boxes')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

# Create the select function
def select():
    if myCombo.get() == 'Monday':
        myLabel = Label(root, text='you clicked monday').pack(pady=10)
    if myCombo.get() == 'Tuesday':
        myLabel = Label(root, text='you clicked tuesday').pack(pady=10)
    if myCombo.get() == 'Wednesday':
        myLabel = Label(root, text='you clicked wednesday').pack(pady=10)
    
    # myLabel = Label(root, text=myCombo.get()).pack(pady=10)

# Combo boxes
options = [
    'Monday',
    'Tuesday',
    'Wednesday',
]

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)  #pass in the index for the first thing in the dictionary - this is Monday
myCombo.pack(pady=10)

myButton = Button(root, text='Select', command=select).pack()

root.mainloop()