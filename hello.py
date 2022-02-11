#! python3
# first hello world gui
from tkinter import *

root = Tk()     #create an instance
root.title('Hello World!')
root.geometry('400x400')

#create a lable with forground white, background black, font Helvtica @32 pix 
# you can also set the height=200 and width=200 of a label this will make more sense when using a grid system
myLabel = Label(root, text='Hello World!', fg='white', bg='black', font=('Helvtica', 32))
myLabel.pack()  #you can use a pack or a grid system
#label with sunken relief.  You can do sunken, raised, groove and ridge.  Can also give it a state of; disabled(normal is the default)
myLabel2 = Label(root, text='Second Thing!', relief='ridge', state='disabled')
myLabel2.(pady=50)  #here we are setting the padding on either the x or y axis(here its y axis)


root.mainloop()     #create the main loop that runs all the time.  Do this at the bottom of the program 