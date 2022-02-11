#! python3
# how to create new windows .... multiple windows

from tkinter import *

root = Tk()     
root.title('Hello World!')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

# Create 2nd window function
def openWindow():
    newWindow = Toplevel()    # creates a new window in addition to the original window
    newWindow.title('Second Window')
    newWindow.geometry('300x200')
    newWindow.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

    myLabel = Label(newWindow, text='Look at my cool second window!').pack(pady=20)
    newWindow.mainloop()    # this closes the loop for the 2nd window.  The program will work if you forget this part but technically you are supposed to close it out

# Create New Windows
myButton = Button(root, text='Open 2nd Window', command=openWindow).pack()

root.mainloop()