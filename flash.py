#! python3
# Flash cards project

from tkinter import *
from random import randint      # creates random integers

root = Tk()     
root.title('Flashcard App!')
root.geometry('400x400')
root.iconbitmap('C:\\marks_work_docs\\development\\tkinter_intro\\myicon.ico')  


# create function to determine subtract answer correct?
def subtractCorrect(num_1, num_2):   
    correct = num_1 - num_2
    
    # Correct and Incorrect message
    outputAnswerCorrect = StringVar()
    outputAnswerIncorrect = StringVar()
    outputAnswerCorrect.set('Correct ' + str(num_1) + ' - ' + str(num_2) + ' = ' + str(correct))
    outputAnswerIncorrect.set('Incorrect ' + str(num_1) + ' - ' + str(num_2) + ' = ' + str(correct) + ', Not ' + subtractAnswer.get())

    if int(subtractAnswer.get()) == correct:
        subtractCorrectLabel.config(text=outputAnswerCorrect.get())
    else:
        subtractCorrectLabel.config(text=outputAnswerIncorrect.get())

    # Clear the answer box(subtractAnswer)
    subtractAnswer.delete(0, 'end')  # the 0 is the first index and it holds whatever you typed in the Entry box

    # Generate two new random numbers(these are IntVars so we should just need to set them)
    num1.set(randint(0,10))
    num2.set(randint(0,10))
    subtractFlash.config(text=str(num1.get()) + ' - ' + str(num2.get()), font=('helvetica', 72) )

# Create subtract function
def subtract():
    hideMenuFrames()
    subtractFrame.pack(fill='both', expand=1)

    # create 2 random integers between 0 and 10
    global num1
    global num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(randint(0,10))
    num2.set(randint(0,10))

    # Put random integers on the screen
    global subtractFlash
    subtractFlash = Label(subtractFrame, text=str(num1.get()) + ' - ' + str(num2.get()), font=('helvetica', 72))
    subtractFlash.pack(pady=10)

    #Answer box for subtract function
    global subtractAnswer
    subtractAnswer = Entry(subtractFrame)
    subtractAnswer.pack(pady=5)

    #Answer button
    subtractButton = Button(subtractFrame, text='Answer', command=lambda: subtractCorrect(num1.get(),num2.get()))
    subtractButton.pack(pady=5)

    # Correct or Incorrect Message
    global subtractCorrectLabel
    subtractCorrectLabel = Label(subtractFrame, text='Enter Your Answer Above')
    subtractCorrectLabel.pack(pady=5)


# create function to determine add answer correct?
def addCorrect(num_1, num_2):   
    # Calculate the actual answer.  these num_1/num_2 get passed in from the addButton(usin underscores cause they are different)
    correct = num_1 + num_2
    
    # Correct and Incorrect message
    outputAnswerCorrect = StringVar()
    outputAnswerIncorrect = StringVar()
    outputAnswerCorrect.set('Correct ' + str(num_1) + ' + ' + str(num_2) + ' = ' + str(correct))
    outputAnswerIncorrect.set('Incorrect ' + str(num_1) + ' + ' + str(num_2) + ' = ' + str(correct) + ', Not ' + addAnswer.get())

    if int(addAnswer.get()) == correct:
        addCorrectLabel.config(text=outputAnswerCorrect.get())
    else:
        addCorrectLabel.config(text=outputAnswerIncorrect.get())

    # Clear the answer box(addAnswer)
    addAnswer.delete(0, 'end')  # the 0 is the first index and it holds whatever you typed in the Entry box

    # Generate two new random numbers(these are IntVars so we should just need to set them)
    num1.set(randint(0,10))
    num2.set(randint(0,10))
    addFlash.config(text=str(num1.get()) + ' + ' + str(num2.get()), font=('helvetica', 72) )

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
    global addFlash
    addFlash = Label(addFrame, text=str(num1.get()) + ' + ' + str(num2.get()), font=('helvetica', 72) )
    addFlash.pack(pady=10)

    #Answer box for add function
    global addAnswer
    addAnswer = Entry(addFrame)
    addAnswer.pack(pady=5)

    #Answer button
    addButton = Button(addFrame, text='Answer', command=lambda: addCorrect(num1.get(),num2.get()))
    addButton.pack(pady=5)

    # Correct or Incorrect Message
    global addCorrectLabel
    addCorrectLabel = Label(addFrame, text='Enter Your Answer Above')
    addCorrectLabel.pack(pady=5)

# Create subtract function  ##### this section will need to be removed
# def subtract():
#     hideMenuFrames()
#     subtractFrame.pack(fill='both', expand=1)

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
subtractFrame = Frame(root, width=400, height=400)
multiplyFrame = Frame(root, width=400, height=400, bg='yellow')
divideFrame = Frame(root, width=400, height=400, bg='green')

root.mainloop()