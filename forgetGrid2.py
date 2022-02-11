#! python3
# Grid Forget - we need to clear out the previous entries because it just writes over the old
# here instead of using the clear button we want to force it to clear when we click the 'submit' button so that every time we submit something new it clears out the old before entering new. 
from tkinter import *
from PIL import ImageTk, Image

root = Tk()     
root.title('Hello World!')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

helloLabel = Label(root)    # this sets up the variable so it can be 'cleared' on the first submit(see clear function below)

# Create open submit function
def submit():
    global helloLabel  
    clear()     #if we add the clear function to the submit function then it will clear out the old but we will also need to define helloLabel as a global variable and set it to something. WE do that above the submit function. 
    helloLabel = Label(root, text='Hello ' + e.get())
    helloLabel.grid(row=3, column=0)

# Create clear function to erase the helloLabel with either grid_forget or destroy
def clear():
    helloLabel.grid_forget()        #this will hide it and you can bring it back
    # helloLabel.destroy()          #this removes it and you can't get it back(in this case it kinda does the same thing)

# Forget
myLabel = Label(root, text='Enter Your Name:').grid(row=0, column=0)

e = Entry(root)
e.grid(row=1, column=0)

myButton = Button(root, text='Submit', command=submit).grid(row=2, column=0)

clearButton = Button(root, text='Clear', command=clear).grid(row=2, column=1)

root.mainloop()