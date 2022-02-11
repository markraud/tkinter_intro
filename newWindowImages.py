#! python3
# how to create new windows .... multiple windows

from tkinter import *
from PIL import ImageTk, Image

root = Tk()     
root.title('Hello World!')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

# Create 2nd window function
def openWindow():
    newWindow = Toplevel()    # creates a new window in addition to the original window
    newWindow.title('Second Window')
    newWindow.geometry('500x700')
    newWindow.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

    myLabel = Label(newWindow, text='Look at my cool second window!').pack(pady=20)

    myImg = ImageTk.PhotoImage(Image.open('treeImage.jpg'))
    imgLabel = Label(newWindow, image=myImg)
    imgLabel.pack(pady=5)

    destroyButton = Button(newWindow, text='Quit', command=newWindow.destroy)   # this is a button that closes out the 2nd window
    destroyButton.pack(pady=5)

    #Minimize the original window
    # hideButton = Button(newWindow, text='Hide Main Window', command=root.iconify)  
    # showButton = Button(newWindow, text='Show Main Window', command=root.deiconify)  
    
    #Withdraw Original Window
    hideButton = Button(newWindow, text='Hide/Withdraw Main Window', command=root.withdraw)  
    showButton = Button(newWindow, text='Show Main Window', command=root.deiconify)  

    killOriginal = Button(newWindow, text='Quit original', command=root.destroy).pack()
    

    hideButton.pack()
    showButton.pack()
    
    newWindow.mainloop()    # this closes the loop for the 2nd window.  The program may work if you forget this part but technically you are supposed to close it out

# Create New Windows
myButton = Button(root, text='Open 2nd Window', command=openWindow).pack()

root.mainloop()