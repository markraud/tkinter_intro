#! python3
# hello world gui using grid instead of pack
from tkinter import *

root = Tk()     
root.title('Hello World!')
root.geometry('400x400')

def clicked():
    myLabel2 = Label(root, text='You clicked the button!').pack()
    #you can do the pack like above or like this.... myLabel2.pack()  
    
#create label
myLabel = Label(root, text='Hello World!', fg='white', bg='black', font=('Helvtica', 32))
myLabel.pack()

#create button
myButton = Button(root, text='Click Me!', command=clicked)      #this will call the "clicked" function when pushed
myButton.pack(pady=20)

root.mainloop()     