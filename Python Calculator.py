# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:56:52 2022

@author: Aidan
"""

#Simple calculator using Form
#Click on numbers and add numbers together


from tkinter import *

#global variable
#global operation
variable = 0
operation = ""

def printNum(x):
    print(x)
    
def clicked(x):
    if (input_box.get() == "0"):
        input_box.delete(0, "end")
    input_box.insert( len(input_box.get()), x)
    
def clearAll():
    clearBox()
    global variable
    variable = 0
    
def clearBox():
    input_box.delete(0, "end")
    input_box.insert( len(input_box.get()), "0")
    
def opClick(x):
    global variable
    global operation
    if(variable == 0):
        variable = int(input_box.get())
    else:
        equalClick()
    operation = x
    clearBox()
    
def equalClick():
    global operation
    global variable
    temp = None
    if(operation == "+"):
        temp = variable + int(input_box.get())
    elif(operation == "-"):
        temp = variable - int(input_box.get())
    elif(operation == "*"):
        temp = variable * int(input_box.get())
    elif(operation == "/"):
        if(int(input_box.get()) != 0):
           temp = int(variable / int(input_box.get()))
    else:
        temp = int(input_box.get())
    variable = temp
    input_box.delete(0, "end")
    input_box.insert(len(input_box.get()), variable)
    operation = ""
    

root = Tk()
root.geometry("500x500")
root.title("Simple Calculator")

input_frame = Frame(root)
input_frame.pack(expand = YES, fill = BOTH)


input_box = Entry(input_frame, width = 50)
input_box.configure(font = ("Arial", 20, ""))
input_box.grid(row=0, column = 0)
clearBox()

buttonFont = ("Arial", 15)
button_frame = Frame(root)
button_frame.pack(expand = YES, fill = BOTH)
#Should be easier with manual buttons
for i in range(0, 9):
    b1 = Button(button_frame, text = str(i+1), font = buttonFont, command = lambda i = i: clicked(str(i+1)), 
                padx = 30, pady = 30)
    b1.grid(row = int(i/3 + 1), column = i%3)
    
zero = Button(button_frame, text = "0", font = buttonFont, command = lambda: clicked("0"), padx = 30, pady = 30)
zero.grid(row = 4, column = 0)

clear = Button(button_frame, text = "C", font = buttonFont, command = clearAll, padx = 30, pady = 30)
clear.grid(row = 4, column = 1)

equal = Button(button_frame, text = "=", font = buttonFont, command = equalClick, padx = 30, pady = 30)
equal.grid(row = 4, column = 2)
    
add = Button(button_frame, text = "+", font = buttonFont, command = lambda: opClick("+"), padx = 30, pady = 30)
add.grid(row = 1, column = 3)
minus = Button(button_frame, text = "-", font = buttonFont, command = lambda: opClick("-"), padx = 30, pady = 30)
minus.grid(row = 2, column = 3)
mul = Button(button_frame, text = "*", font = buttonFont, command = lambda: opClick("*"), padx = 30, pady = 30)
mul.grid(row = 3, column = 3)
div = Button(button_frame, text = "/", font = buttonFont, command = lambda: opClick("/"), padx = 30, pady = 30)
div.grid(row = 4, column = 3)

root.mainloop()