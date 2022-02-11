#! python3
# how to create an open file dialog box

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()     
root.title('Hello World!')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

# Open file dialog box  (both methods works for the initial path)
# root.filename = filedialog.askopenfilename(initialdir='/marks_work_docs/development/tkinter_intro', title='Open An Image File', filetypes=( ('PNG FILe', '*.png'), ('All Files', '*.*') ))

root.filename = filedialog.askopenfilename(initialdir='C:\\marks_work_docs\\development\\tkinter_intro', title='Open An Image File', filetypes=( ('JPG File', '*.jpg'), ('PNG File', '*.png'), ('All Files', '*.*') ))

root.mainloop()