#! python3
#how to create a 2nd menu using tkinter

from msilib.schema import RadioButton
from tkinter import *

root = Tk()     
root.title('Check Boxes')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

#Create Toppings function
def toppings():
    if v.get() == 'pepperoni':
        myLabel = Label(root, text='You ordered pepperoni')
    else:
        myLabel = Label(root, text='You don\'t want pepperoni')
    # myLabel = Label(root, text=v.get())
    myLabel.pack(pady=10)

# Check Boxes
v = StringVar()

myCheck = Checkbutton(root, text='Pepperoni', variable=v, onvalue='pepperoni', offvalue='no_pepperoni')
myCheck.deselect()
myCheck.pack()

myButton = Button(root, text='Select Toppings', command=toppings)
myButton.pack(pady=10)

root.mainloop()