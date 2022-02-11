#! python3
#how to create a 2nd menu using tkinter

from msilib.schema import RadioButton
from tkinter import *

root = Tk()     
root.title('Radio Buttons')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

# Create radio button function
def radio():
    if v.get() == 'one':    #this will need to be set to 1 if using IntVar
        myLabel = Label(root, text='You clicked radio button one!')
    else:
        myLabel = Label(root, text='You clicked radio button two!')
    # myLabel = Label(root, text=v.get())       # gets the label based on what button you choose
    myLabel.pack(pady=10)

v = StringVar()
v.set('one')    # this sets the one radio button to be chosen upon starting the program
rbutton1 = Radiobutton(root, text='One', variable=v, value='one').pack()
rbutton2 = Radiobutton(root, text='Two', variable=v, value='two').pack()

# you can also do the same thing with IntVar
# v = IntVar()         
# rbutton1 = Radiobutton(root, text='One', variable=v, value=1).pack()
# rbutton2 = Radiobutton(root, text='Two', variable=v, value=2).pack()


myButton = Button(root, text='Click Me', command=radio)
myButton.pack(pady=20)

root.mainloop()