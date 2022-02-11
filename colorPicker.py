#! python3
# Color Chooser

from cgitb import text
from tkinter import *
from tkinter import colorchooser

root = Tk()     
root.title('Hello World!')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

def color():
    myColor = colorchooser.askcolor()[1]            # here if you designate the 0 index it will give you RGP color if you use 1 it will give you hex color
    myLabel = Label(root, text=myColor).pack()      # returns RGP and Hex color codes in a Python list


myButton = Button(root, text='Pick a color', command=color).pack()

root.mainloop()