#! python3

from cgitb import text
from tkinter import *
from tkinter import messagebox

root = Tk()     
root.title('Check Boxes')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

# Create Popup function
def popup():
    response = messagebox.askyesno('Popup Title', 'Look at my popup message!') #the showinfo shows the blue icon with an i
    myLabel = Label(root, text=response).pack(pady=10)

    if response == 1:
        myLabel = Label(root, text='you clicked yes!').pack(pady=10)
    else:
        myLabel = Label(root, text='you clicked no!').pack(pady=10)

# Popup boxes
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

popButton = Button(root, text='Click to Pop Up!', command=popup)
popButton.pack(pady=20)

root.mainloop()