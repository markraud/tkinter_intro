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

# create function to determine the multiply answer correct?
def multiplyCorrect(num_1, num_2):   
    correct = num_1 * num_2
    
    # Correct and Incorrect message
    outputAnswerCorrect = StringVar()
    outputAnswerIncorrect = StringVar()
    outputAnswerCorrect.set('Correct ' + str(num_1) + ' x ' + str(num_2) + ' = ' + str(correct))
    outputAnswerIncorrect.set('Incorrect ' + str(num_1) + ' x ' + str(num_2) + ' = ' + str(correct) + ', Not ' + multiplyAnswer.get())

    if int(multiplyAnswer.get()) == correct:
        multiplyCorrectLabel.config(text=outputAnswerCorrect.get())
    else:
        multiplyCorrectLabel.config(text=outputAnswerIncorrect.get())

    # Clear the answer box(multiplyAnswer)
    multiplyAnswer.delete(0, 'end')  # the 0 is the first index and it holds whatever you typed in the Entry box

    # Generate two new random numbers(these are IntVars so we should just need to set them)
    num1.set(randint(0,10))
    num2.set(randint(0,10))
    multiplyFlash.config(text=str(num1.get()) + ' x ' + str(num2.get()), font=('helvetica', 72) )

# Create multiply function
def multiply():
    hideMenuFrames()
    multiplyFrame.pack(fill='both', expand=1)

    # create 2 random integers between 0 and 10
    global num1
    global num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(randint(0,10))
    num2.set(randint(0,10))

    # Put random integers on the screen
    global multiplyFlash
    multiplyFlash = Label(multiplyFrame, text=str(num1.get()) + ' x ' + str(num2.get()), font=('helvetica', 72) )
    multiplyFlash.pack(pady=10)

    #Answer box for multiply function
    global multiplyAnswer
    multiplyAnswer = Entry(multiplyFrame)
    multiplyAnswer.pack(pady=5)

    #Answer button
    multiplyButton = Button(multiplyFrame, text='Answer', command=lambda: multiplyCorrect(num1.get(),num2.get()))
    multiplyButton.pack(pady=5)

    # Correct or Incorrect Message
    global multiplyCorrectLabel
    multiplyCorrectLabel = Label(multiplyFrame, text='Enter Your Answer Above')
    multiplyCorrectLabel.pack(pady=5)


#############################################################################
# create function to determine the divide answer correct?
def divideCorrect(num_1, num_2):   
    correct = num_1 / num_2
    
    # Correct and Incorrect message
    outputAnswerCorrect = StringVar()
    outputAnswerIncorrect = StringVar()
    outputAnswerCorrect.set('Correct ' + str(num_1) + ' / ' + str(num_2) + ' = ' + str(correct))
    outputAnswerIncorrect.set('Incorrect ' + str(num_1) + ' / ' + str(num_2) + ' = ' + str(correct) + ', Not ' + divideAnswer.get())

    if float(divideAnswer.get()) == correct:        # had to make this a float here 
        divideCorrectLabel.config(text=outputAnswerCorrect.get())
    else:
        divideCorrectLabel.config(text=outputAnswerIncorrect.get())

    # Clear the answer box(divideAnswer)
    divideAnswer.delete(0, 'end')  # the 0 is the first index and it holds whatever you typed in the Entry box

    # Generate two new random numbers(these are IntVars so we should just need to set them)
    num1.set(randint(0,10))
    num2.set(randint(1,10))
    divideFlash.config(text=str(num1.get()) + ' / ' + str(num2.get()), font=('helvetica', 72) )

# Create divide function
def divide():
    hideMenuFrames()
    divideFrame.pack(fill='both', expand=1)

    # create 2 random integers between 0 and 10
    global num1
    global num2
    num1 = IntVar()
    num2 = IntVar()
    num1.set(randint(0,10))
    num2.set(randint(1,10))

    # Put random integers on the screen
    global divideFlash
    divideFlash = Label(divideFrame, text=str(num1.get()) + ' / ' + str(num2.get()), font=('helvetica', 72) )
    divideFlash.pack(pady=10)

    #Answer box for divide function
    global divideAnswer
    divideAnswer = Entry(divideFrame)
    divideAnswer.pack(pady=5)

    #Answer button
    divideButton = Button(divideFrame, text='Answer', command=lambda: divideCorrect(num1.get(),num2.get()))
    divideButton.pack(pady=5)

    # Correct or Incorrect Message
    global divideCorrectLabel
    divideCorrectLabel = Label(divideFrame, text='Enter Your Answer Above')
    divideCorrectLabel.pack(pady=5)

           
##################################################################################

#Create hide frame function
def hideMenuFrames():
    # destroy the children widgets in each frame
    for widget in addFrame.winfo_children():    
        widget.destroy()
    for widget in subtractFrame.winfo_children():    
        widget.destroy()
    for widget in multiplyFrame.winfo_children():    
        widget.destroy()
    for widget in divideFrame.winfo_children():    
        widget.destroy()
    for widget in startFrame.winfo_children():    
        widget.destroy()
    
    # hide all frames
    addFrame.pack_forget()
    subtractFrame.pack_forget()
    multiplyFrame.pack_forget()
    divideFrame.pack_forget()
    startFrame.pack_forget()

# Start Screen
def home():
    hideMenuFrames()
    startFrame.pack(fill='both', expand=1)
    startLabel = Label(startFrame, text='Welcome To Math Flashcards!', font=('Helvetica',18)).pack(pady=40)
    # button to flashcards
    aButton = Button(startFrame, text='Addition Flashcards', command=add).pack(pady=5)
    sButton = Button(startFrame, text='Subtraction Flashcards', command=subtract).pack(pady=5)
    mButton = Button(startFrame, text='Multiplication Flashcards', command=multiply).pack(pady=5)
    dButton = Button(startFrame, text='Division Flashcards', command=divide).pack(pady=5)

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
mathMenu.add_command(label='Home', command=home)
mathMenu.add_command(label='Exit', command=root.quit)

# Create Math Frames
addFrame = Frame(root, width=400, height=400)
subtractFrame = Frame(root, width=400, height=400)
multiplyFrame = Frame(root, width=400, height=400)
divideFrame = Frame(root, width=400, height=400)
startFrame = Frame(root, height=400, width=400)

#show the start screen
home()


root.mainloop()