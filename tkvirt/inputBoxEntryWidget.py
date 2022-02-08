#! python3
# hello world gui using grid instead of pack
from tkinter import *

root = Tk()     
root.title('Hello World!')
root.geometry('400x400')

def clicked():
    input = e.get()       #this stores what is typed in the entry widget in the variable input
    myLabel2 = Label(root, text='Hello ' + input)        #adding the e.get() or input for the text will take whatever you type in the input box and print it below when you click the button
    myLabel2.pack()

#create label
myLabel = Label(root, text='Enter your name:')
myLabel.pack()

#create Entry Widget(Input Box)
e = Entry(root, font=('Helvtica', 18))
e.pack(pady=20)

#create button
myButton = Button(root, text='Click Me!', command=clicked)      #this will call the "clicked" function when pushed
myButton.pack(pady=20)




root.mainloop()   