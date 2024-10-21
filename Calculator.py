'''
Calculator Builder - Starter Code
Author: Mohammed Farzaan Fahim
Date: 9/3/2024

[Project Description]

'''
"""
TODO:
SETUP
1. Draw out your calculator on paper - think about what buttons should be included and how to arrange them
    MUST INCLUDE: 0,1,2,3,4,5,6,7,8,9,+,-,*,/, CLEAR, =, DEL (or DELETE or BACKSPACE)
    OPTIONAL: any buttons you choose, like on OFF button linked to root.quit()
2. From this drawing determine what row and column each button should be placed in
3. Pick out a colour-scheme so that your design is attractive

black - background(frame) , baby blue - screen(output) , red - detete and clear button(widgets) , white - other buttons(widgets)

CODING
1. Create a Label that uses the 'expression' StringVar as its textvariable
2. Customize the CalcButton class so that creating your Buttons is easy and standardized
    2.1 Add more parameters to the __init__ function so your buttons can be created inside it
    2.2 Set the 'command' for your Buttons to be 'self.onClick' so that you can use the premade functions
3. Create a Label that uses the 'expression' StringVar as its textvariable - this is the top of the calculator where the expression appears
4. Create your Buttons using the CalcButton class. Some buttons you may want to create without it, especially if they have special commands.
    4.1 Your '=' button, for example, should have its command set to the 'evaluate' function instead
    4.2 Your 'CLEAR' button should have its command set to the 'clear' function

"""


from tkinter import *
root = Tk()
root.geometry('200x250')
expression = StringVar()


class CalcButton():
    def __init__(self, frame, char, bg, fg, x, y, rspan, cspan, command=None,):  # add extra parameters
        if command == None:
            command = self.onClick
        # this should be the character on the button, like '2' or '+' as a one character string
        self.char = char

          # create your Button and store it as the 'obj' instance variable
        self.obj = Button(frame, command=command, text=char, bg=bg, fg=fg)
        self.obj.grid( row= x, column= y, columnspan=cspan, rowspan=rspan, sticky= 'news')
        # are there any other pieces of information a button should store?

    def onClick(self):
        """
        This function simply adds this buttons character to the expression
        """
        expression.set(expression.get() + self.char)


def clear():
    """
    Clears the expression.
    """
    expression.set('')


def delete():
    """
    Removes the last character in expression.
    """
    expression.set(expression.get()[:-1])


def evaluate():
    """
    Calls the built-in function 'eval' which will evaluate a string according to Pythons evauation rules.
    Replaces the existing expression with the result of evaluating the expression.
    strip() removes any trailing whitespace (spaces or newline characters) since eval does not like them.
    Examples:
    eval('3+4') -> '7'
    eval('3 - 3 + 3 + 56') -> '59'              # spaces between numbers are optional
    eval('-2 * 6') -> '-12'                     # do not use 'x' for multiplication, must be '*'
    """
    expression.set(str(eval(expression.get().strip())))

# Mainframe groups the screen and button frames 
mainframe = Frame(root, bg = 'black', padx=10, pady=15)
mainframe.grid(row = 0, column= 0, sticky= 'news', columnspan= 4, rowspan= 6)
screenframe = Label(mainframe, bg= 'light cyan', fg = 'black',justify='right', textvariable=expression, width=mainframe.winfo_width())
screenframe.grid(row= 0, column= 0, sticky= 'news', columnspan=4, rowspan=1)
# Buttonframe groups all fo our buttons together
buttonframe = Frame(root, bg= '#1e1e1e', padx=8, pady=13)
buttonframe.grid(row= 1, column= 0, sticky='news', columnspan=4, rowspan=5)
# Create your buttons here
#
CalcButton(buttonframe, '0', 'white', 'black', 5, 0, 1, 1)
CalcButton(buttonframe, '1', 'white', 'black', 4, 2, 1, 1)
CalcButton(buttonframe, '2', 'white', 'black', 4, 1, 1, 1)
CalcButton(buttonframe, '3', 'white', 'black', 4, 0, 1, 1)
CalcButton(buttonframe, '4', 'white', 'black', 3, 2, 1, 1)
CalcButton(buttonframe, '5', 'white', 'black', 3, 1, 1, 1)
CalcButton(buttonframe, '6', 'white', 'black', 3, 0, 1, 1)
CalcButton(buttonframe, '7', 'white', 'black', 2, 2, 1, 1)
CalcButton(buttonframe, '8', 'white', 'black', 2, 1, 1, 1)
CalcButton(buttonframe, '9', 'white', 'black', 2, 0, 1, 1)
CalcButton(buttonframe, '.', 'light sky blue', 'black', 5, 1, 1, 1)
CalcButton(buttonframe, '=', 'light sky blue', 'black', 5, 2, 1, 1, command=evaluate)
CalcButton(buttonframe, '+', 'light sky blue', 'black', 4, 3, 2, 1)
CalcButton(buttonframe, '-', 'light sky blue', 'black', 3, 3, 1, 1)
CalcButton(buttonframe, 'x', 'light sky blue', 'black', 2, 3, 1, 1)
CalcButton(buttonframe, '÷', 'light sky blue', 'black', 1, 3, 1, 1)
CalcButton(buttonframe, '%', 'light sky blue', 'black', 1, 2, 1, 1)
CalcButton(buttonframe, 'DEL', 'brown1', 'black', 1, 1, 1, 1, command=delete)
CalcButton(buttonframe, 'CLR', 'brown1', 'black', 1, 0, 1, 1, command=clear)
# Configure your rows and columns here as needed - remember to configure the root as well as your frames!
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.columnconfigure(1, weight = 1)
for i in range(6):
    mainframe.rowconfigure(i, weight = 1)
for i in range(4):
    mainframe.columnconfigure(i, weight = 1)
    buttonframe.columnconfigure(i, weight = 1)
for i in range(5):
    buttonframe.rowconfigure(i, weight = 1)

root.mainloop()
