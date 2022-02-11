#! python3

from tkinter import *
from tkinter import messagebox

root = Tk()     
root.title('Check Boxes')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

# Create Popup function
def popup():
    # messagebox.showinfo('Popup Title', 'Look at my popup message!') #the showinfo shows the blue icon with an i
    # messagebox.showwarning('Popup Title', 'Look at my popup message!') #the showinfo shows the blue icon with an i
    # messagebox.showerror('Popup Title', 'Look at my popup message!') #the showinfo shows the blue icon with an i
    # messagebox.askquestion('Popup Title', 'Look at my popup message!') #the showinfo shows the blue icon with an i
    # messagebox.askokcancel('Popup Title', 'Look at my popup message!') #the showinfo shows the blue icon with an i
    messagebox.askyesno('Popup Title', 'Look at my popup message!') #the showinfo shows the blue icon with an i


# Popup boxes
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

popButton = Button(root, text='Click to Pop Up!', command=popup)
popButton.pack(pady=20)

root.mainloop()