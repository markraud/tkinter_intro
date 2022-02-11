#! python3
# hello world gui using grid instead of pack
from tkinter import *

root = Tk()     
root.title('Hello World!')
root.geometry('400x400')

#create labels
myLabel = Label(root, text='Hello World!', fg='white', bg='black', font=('Helvtica', 32))
myLabel.grid(row=0 , column=0, columnspan=2) # 0,0 is the upper left hand corner
#columnspan=2 tells it to span across 2 columns.  You can also do this with rows

myLabel2 = Label(root, text='Second Thing!')
myLabel2.grid(row=1 , column=0, sticky=W)  #this will be on the 2nd row in the same column
# sticky will justify to the sides to top and bottom.... use North, South, East, West

myLabel3 = Label(root, text='Second Thing!')
myLabel3.grid(row=1 , column=1, )  #this will be on the 2nd row in the 2nd column



root.mainloop()     