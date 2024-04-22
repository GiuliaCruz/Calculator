from tkinter import *

root = Tk()
root.title('Your Calculator')
root.geometry('408x355') #size
root.minsize(408,355)
root.maxsize(408,355)

number1 = '.'
division = FALSE
multiplication = FALSE
addition = FALSE
subtraction = FALSE
root.configure(background = '#3f448c')

e = Entry(root,width = 15, borderwidth = 4, relief =FLAT, fg ='#FFFFFF',
          bg ='#7178df', font =('futura', 25, 'bold'), justify = CENTER)
e.grid(
    row = 0,
    column = 0,
    columnspan = 4,
    pady = 2 
)
#commands
def button_click(num):
    e.insert(END, num)

def button_division():
    global number1
    global division
    division = TRUE
    number1 = e.get()
    e.delete(0, END)

def button_multiplication():
    global number1
    global multiplication
    multiplication = TRUE
    number1 = e.get()
    e.delete(0, END)

def button_subtraction():
    global number1
    global subtraction
    subtraction = TRUE
    number1 = e.get()
    e.delete(0, END)

def button_addition():
    global number1
    global addition
    addition = TRUE
    number1 = e.get()
    e.delete(0, END)

def button_clear():
    e.delete(0, END)

def button_equal():
    global subtraction
    global addition
    global multiplication
    global division
    number2 = e.get()
    e.delete(0, END)
    if addition == True:
        e.insert(0, int(number1) + int(number2))
        addition = FALSE

    if multiplication == TRUE:
        e.insert(0, int(number1) * int(number2))
        multiplication = FALSE

    if subtraction == TRUE:
        e.insert(0, int(number1) - int(number2))
        subtraction == FALSE

    if division == True:
        e.insert(0, int(number1) / int(number2))
        division == FALSE
#mathematical operations
divide = Button(root,
                text = '÷',
                padx = 44, #largura
                pady = 20, #altura
                command = button_division,
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
divide.grid(row = 0, column = 4)

multiplication = Button(root,
                text = '×',
                padx = 44, #largura
                pady = 20, #altura
                command = button_multiplication,
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
multiplication.grid(row = 1, column = 4)

subtraction = Button(root,
                text = '–',
                padx = 44, 
                pady = 20, 
                command = button_subtraction,
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
subtraction.grid(row = 2, column = 4)

addition = Button(root,
                text = '+',
                padx = 44, 
                pady = 20, 
                command = button_addition,
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
addition.grid(row = 3, column = 4)

clear = Button(root,
                text = 'C',
                padx = 43, 
                pady = 20, 
                command = button_clear,
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
clear.grid(row = 4, column = 4)

equal = Button(root,
                text = '=',
                padx = 43, 
                pady = 20, 
                command = button_equal,
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
equal.grid(row = 4, column = 3)

#first row
one = Button(root,
                text = '1',
                padx = 40, 
                pady = 20, 
                command = lambda: button_click(1),
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
one.grid(row = 1,column = 1)

two = Button(root,
                text = '2',
                padx = 40, 
                pady = 20, 
                command = lambda: button_click(2),
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
two.grid(row = 1,column = 2)

three = Button(root,
                text = '3',
                padx = 43, 
                pady = 20, 
                command = lambda: button_click(3),
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
three.grid(row = 1,column = 3)

#second row
four = Button(root,
                text = '4',
                padx = 40, 
                pady = 20, 
                command = lambda: button_click(4),
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
four.grid(row = 2,column = 1)

five = Button(root,
                text = '5',
                padx = 40, 
                pady = 20, 
                command = lambda: button_click(5),
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
five.grid(row = 2,column = 2)

six = Button(root,
                text = '6',
                padx = 43, 
                pady = 20, 
                command = lambda: button_click(6),
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
six.grid(row = 2,column = 3)

#Third row
seven = Button(root,
                text = '7',
                padx = 40, 
                pady = 20, 
                command = lambda: button_click(7),
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
seven.grid(row = 3,column = 1)

eight = Button(root,
                text = '8',
                padx = 40, 
                pady = 20, 
                command = lambda: button_click(8),
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
eight.grid(row = 3,column = 2)

nine = Button(root,
                text = '9',
                padx = 43, 
                pady = 20, 
                command = lambda: button_click(9),
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
nine.grid(row = 3,column = 3)

#fourth row
zero = Button(root,
                text = '0',
                padx = 91, 
                pady = 20, 
                command = lambda: button_click(0),
                fg = '#FFFFFF',
                activeforeground = '#FFFFFF',
                bg = '#5a61bd',
                activebackground ='#5a61bd',
                relief = FLAT,
                font = ('futura', 12, 'bold')
)
zero.grid(row = 4,column = 1, columnspan = 2)

root.mainloop()