# Использую стандартную библиотеку tkinter
from tkinter import *
import random
root = Tk()
root.title('Tic-tac-toe')
game_run = True
field = []
krestik_count = 0

# проверяю нажатия кнопок
# Устанавливаю глобальные переменные game_run и krestik_count в начальные значения.

def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global krestik_count
    krestik_count = 0

def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global krestik_count
        krestik_count += 1
        check_win('X')
        if game_run and krestik_count < 5:
            computer_move()
            check_win('O')

# проверяю победу
# Переменная krornolik – это символ «X» или «O», то есть крестики или нолики. Если задан «O», то проверяется: не победил ли компьютер.

def check_win(krornolik):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], krornolik)
        check_line(field[0][n], field[1][n], field[2][n], krornolik)
    check_line(field[0][0], field[1][1], field[2][2], krornolik)
    check_line(field[2][0], field[1][1], field[0][2], krornolik)

def check_line(a1,a2,a3,krornolik):
    if a1['text'] == krornolik and a2['text'] == krornolik and a3['text'] == krornolik:
        a1['background'] = a2['background'] = a3['background'] = 'red'
        global game_run
        game_run = False

# Алгоритм действия компьютера
def can_win(a1,a2,a3,krornolik):
    res = False
    if a1['text'] == krornolik and a2['text'] == krornolik and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == krornolik and a2['text'] == ' ' and a3['text'] == krornolik:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == krornolik and a3['text'] == krornolik:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

# Чисто интерфейс
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=8, height=5,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='NEW GAME', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()





