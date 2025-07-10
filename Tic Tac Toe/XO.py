import customtkinter as ctk
from random import randint

Win_Lose = [0, 0]
FILE = 'XO.txt'

try:
    with open(FILE, 'r') as file:
        Win_Lose = [int(line.strip()) for line in file]
except FileNotFoundError:
    pass

def replay():
    for button in buttons:
        button.configure(text='')

def get_text():
    return tuple(button.cget('text') for button in buttons)

def check_winner():
    text = get_text()

    if text[0]==text[1]==text[2]==text[3]==text[6]=='':
        return ''

    for i in range(0, 9, 3):
        if text[i] == text[i+1] == text[i+2]:
            return text[i]
    
    for i in range(0, 3):
        if text[i] == text[i+3] == text[i+6]:
            return text[i]
    
    if text[0] == text[4] == text[8]:
        return text[0]
    if text[2] == text[4] == text[6]:
        return text[2]
    
    return ''

def winner():
    win = check_winner()

    if win == '×':
        Win_Lose[0] += 1
        replay()
    elif win == '○':
        Win_Lose[1] += 1
        replay()
    else:
        if '' not in get_text():
            replay()
            return

    win_lose.configure(text='Win = '+str(Win_Lose[0])+'\tLose = '+str(Win_Lose[1]))
    
    with open(FILE, 'w') as file:
        file.writelines([str(n)+'\n' for n in Win_Lose])

def move(n, x):
    buttons[n].configure(text=x)

def computer_move():
    text = get_text()
    x = randint(0, 8)

    while (text[x] != ''):
        x = randint(0, 8)
    
    move(x, '○')
    winner()
    
def player_move(n):
    move(n, '×')
    winner()
    computer_move()

game = ctk.CTk()
game.title('XO game')
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

title = ctk.CTkFrame(game, corner_radius=20)
title.pack(padx=20, pady=10, fill='x', expand=True)

win_lose = ctk.CTkLabel(
    title,
    font=('Roboto', 16, 'bold'),
    text='Win = ' + str(Win_Lose[0]) + '\tLose = ' + str(Win_Lose[1]))
win_lose.pack(pady = 5, padx = 20)

frame = ctk.CTkFrame(game, corner_radius=20)
frame.pack(padx=20, pady=20)

def create_button(cmd):
    return ctk.CTkButton(
        frame,
        text='',
        width=80, height=80,
        corner_radius=10,
        font=('Roboto', 60, 'bold'),
        command=lambda: player_move(cmd))

buttons = []
for i in range(9):
    button = create_button(i)
    buttons.append(button)
    button.grid(padx=10, pady=10, row=i%3, column=i//3)

game.mainloop()