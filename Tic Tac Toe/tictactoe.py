import customtkinter as ctk
from random import choice

# Initialize win/loss record
Win_Lose = [0, 0]
FILE = 'XO.txt'

# Load win/loss record from file
try:
    with open(FILE, 'r') as file:
        Win_Lose = [int(line.strip()) for line in file]
except FileNotFoundError:
    pass

# Reset the game board
def replay():
    for button in buttons:
        button.configure(text='')

# Retrieve the current board state as a tuple
def get_text():
    return tuple(button.cget('text') for button in buttons)

# Check for a winner or a draw
def check_winner():
    text = get_text()

    # Check rows and columns
    for i in range(0, 9, 3):  # Rows
        if text[i] == text[i + 1] == text[i + 2] != '':
            return text[i]
    for i in range(3):  # Columns
        if text[i] == text[i + 3] == text[i + 6] != '':
            return text[i]

    # Check diagonals
    if text[0] == text[4] == text[8] != '':
        return text[0]
    if text[2] == text[4] == text[6] != '':
        return text[2]

    # No winner yet
    return ''

# Handle winning logic and update scoreboard
def winner():
    win = check_winner()

    if win == '×':  # Player wins
        Win_Lose[0] += 1
        replay()
    elif win == '○':  # Computer wins
        Win_Lose[1] += 1
        replay()
    elif '' not in get_text():  # Draw
        replay()
        return

    # Update scoreboard display
    win_lose.configure(text=f'Win = {Win_Lose[0]}\t\tLose = {Win_Lose[1]}')

    # Save updated scores to file
    with open(FILE, 'w') as file:
        file.writelines([str(n) + '\n' for n in Win_Lose])

# Move function for buttons
def move(n, x):
    buttons[n].configure(text=x)

# Computer's move logic
def computer_move():
    text = get_text()
    empty_indices = [i for i, val in enumerate(text) if val == '']
    if empty_indices:
        move(choice(empty_indices), '○')
    winner()

# Player's move logic
def player_move(n):
    if buttons[n].cget('text') == '':  # Ensure the button isn't already clicked
        move(n, '×')
        winner()
        computer_move()

# Initialize the game window
game = ctk.CTk()
game.title('Tic Tac Toe')
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

# Title and scoreboard
title = ctk.CTkFrame(game, corner_radius=20)
title.pack(padx=20, pady=10, fill='x', expand=True)

win_lose = ctk.CTkLabel(
    title,
    font=('Roboto', 16, 'bold'),
    text=f'Win = {Win_Lose[0]}\t\tLose = {Win_Lose[1]}'
)
win_lose.pack(pady=5, padx=20)

# Game board frame
frame = ctk.CTkFrame(game, corner_radius=20)
frame.pack(padx=20, pady=20)

# Button creation function
def create_button(cmd):
    return ctk.CTkButton(
        frame,
        text='',
        width=80, height=80,
        corner_radius=10,
        font=('Roboto', 60, 'bold'),
        command=lambda: player_move(cmd)
    )

# Create buttons for the 3x3 grid
buttons = []
for i in range(9):
    button = create_button(i)
    buttons.append(button)
    button.grid(padx=10, pady=10, row=i // 3, column=i % 3)

# Run the game
game.mainloop()
