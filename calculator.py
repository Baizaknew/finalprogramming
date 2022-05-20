# Использую стандартную библиотеку tkinter
from tkinter import *
# Использую библ функцию decimal для вычисления с большей точностью
from decimal import *

root = Tk()
root.title('Calculator')

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

saver = '' # использую для хранения набираемого числа.
stack = []  #  будем добавлять введенные числа и операции, которые надо совершить.

def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))

def click(text):
    global saver
    global stack
    if text == 'CE':
        stack.clear()
        saver = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        saver += text
        label.configure(text=saver)
    elif text == '.':
        if saver.find('.') == -1:
            saver += text
            label.configure(text=saver)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            saver = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])
                stack.append(text)
                saver = ''
                label.configure(text='0')

label = Label(root, text='0', width=50, height=5)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

button = Button(root, text='CE', command=lambda text='CE': click(text))
button.grid(row=1, column=3, sticky="nsew")
for row in range(4):
    for col in range(4):
        button = Button(root, text=buttons[row][col],
                command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()