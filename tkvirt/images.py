#! python3
# hello world gui using grid instead of pack
# going to install and use Pillow for images.... use $ pip install Pillow
from tkinter import *
from PIL import ImageTk, Image      #import from Pillow

root = Tk()     
root.title('How to add an Icon!')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\tkvirt\\myicon.ico')  #this added the icon file

def clicked():
    input = e.get()       #this stores what is typed in the entry widget in the variable input
    myLabel2 = Label(root, text='Hello ' + input)        #adding the e.get() or input for the text will take whatever you type in the input box and print it below when you click the button
    myLabel2.pack()

# Add Image
myImage = ImageTk.PhotoImage(Image.open('treeImage.jpg'))
imageLabel = Label(image=myImage)
imageLabel.pack()

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