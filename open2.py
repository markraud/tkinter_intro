#! python3
# how to open an image using the file dialog box

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()     
root.title('Hello World!')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

# Create open dialog box function
def openImage():
    # Open file dialog box  
    root.filename = filedialog.askopenfilename(initialdir='C:\\marks_work_docs\\development\\tkinter_intro', title='Open An Image File', filetypes=( ('JPG File', '*.jpg'), ('PNG File', '*.png'), ('All Files', '*.*')))
    # myLabel = Label(root, text=root.filename).pack(pady=10)  # this line just prints the path to the file you choose.   The root.filename holds the file path so we can use it below to call/open the image
    
    global myImg    #need to make this variable global otherwise it will error.   
    # open image and place on screen
    myImg = ImageTk.PhotoImage(Image.open(root.filename))
    imgLabel = Label(root, image=myImg)
    imgLabel.pack(pady=10)

myButton = Button(root, text='Open Image', command=openImage).pack(pady=10)

root.mainloop()