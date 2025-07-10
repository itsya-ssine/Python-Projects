import customtkinter as ctk
from textblob import TextBlob

root = ctk.CTk()
root.geometry('500x250')
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

def correct_text():
    word = entry.get()
    elc = TextBlob(word)
    right = str(elc.correct())
    correct.configure(text=f'Correct text : {right}')

frame = ctk.CTkFrame(root, corner_radius=20)
frame.pack(padx=20, pady=20, fill='both', expand=True)

label = ctk.CTkLabel(
    frame,
    text='Enter ur text:',
    font=('Roboto', 24, 'bold')
)
label.pack(padx=10, pady=10)

entry = ctk.CTkEntry(
    frame,
    width=400,
    height=40,
    font=('Roboto', 16),
    corner_radius=20
)
entry.pack(padx=10, pady=10)

button = ctk.CTkButton(
    frame,
    width=400,
    height=40,
    text='CHECK',
    corner_radius=20,
    font=('Roboto',16, 'bold'),
    command=correct_text
)
button.pack(padx=10)

correct = ctk.CTkLabel(
    frame,
    text='',
    font=('Roboto', 16, 'bold')
)
correct.pack(padx=10, pady=10)

root.mainloop()