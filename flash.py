#! python3
# Flash cards project

from tkinter import *
from random import randint      # creates random integers

root = Tk()     
root.title('Flashcard App!')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  

# create function to determine add answer correct?
def addCorrect(num_1, num_2):
    pass

# Create add function
def add():
    hideMenuFrames()
    addFrame.pack(fill='both', expand=1)

    # create 2 random integers between 0 and 10
    global num1
    global num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(randint(0,10))
    num2.set(randint(0,10))

    # Put random integers on the screen
    addFlash = Label(addFrame, text=str(num1.get()) + ' + ' + str(num2.get()), font=('helvetica', 32) )
    addFlash.pack(pady=10)

    #Answer box for add function
    addAnswer = Entry(addFrame)
    addAnswer.pack(pady=5)

    #Answer button
    addButton = Button(addFrame, text='Answer', command=lambda: addCorrect(num1.get(),num2.get()))
    addButton.pack(pady=5)

# Create subtract function
def subtract():
    hideMenuFrames()
    subtractFrame.pack(fill='both', expand=1)

# Create multiply function
def multiply():
    hideMenuFrames()
    multiplyFrame.pack(fill='both', expand=1)

# Create divide function
def divide():
    hideMenuFrames()
    divideFrame.pack(fill='both', expand=1)

#Create hide frame function
def hideMenuFrames():
    addFrame.pack_forget()
    subtractFrame.pack_forget()
    multiplyFrame.pack_forget()
    divideFrame.pack_forget()


# Define Main Menu
myMenu = Menu(root)
root.config(menu=myMenu)


# Create Menu Items
mathMenu = Menu(myMenu)
myMenu.add_cascade(label='MathCards', menu=mathMenu)
mathMenu.add_command(label='Add', command=add)
mathMenu.add_command(label='Subtract', command=subtract)
mathMenu.add_command(label='Multiply', command=multiply)
mathMenu.add_command(label='Divide', command=divide)
mathMenu.add_separator()
mathMenu.add_command(label='Exit', command=root.quit)

# Create Math Frames
addFrame = Frame(root, width=400, height=400)
subtractFrame = Frame(root, width=400, height=400, bg='red')
multiplyFrame = Frame(root, width=400, height=400, bg='yellow')
divideFrame = Frame(root, width=400, height=400, bg='green')

root.mainloop()