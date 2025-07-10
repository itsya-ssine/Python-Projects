from tkinter.filedialog import *
import customtkinter as ctk
from PIL import Image

def open_image():
    path = askopenfilename()
    img = Image.open(path)

    def save_image():
        save_path = asksaveasfilename()
        img.save(save_path + "_elc.jpg", optimize = True, quality = 50)
        save_button.destroy()

    save_button = ctk.CTkButton(
        frame,
        text='SAVE',
        height=35,
        width=300,
        font=("Roboto", 16, "bold"),
        corner_radius=10,
        command=save_image)
    save_button.pack(padx = 20, pady = 20)

app = ctk.CTk()
app.title("COMPRESS IMAGE")
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

frame = ctk.CTkFrame(app, corner_radius=30)
frame.pack(padx=20, pady=20, fill="both", expand=True)

lab = ctk.CTkLabel(
    frame,
    text = 'OPEN IMAGE:',
    width = 300,
    height = 30,
    font = ("Roboto", 24, "bold"))
lab.pack(padx = 10, pady = 20)

open_button = ctk.CTkButton(
    frame,
    text='OPEN',
    height=35,
    width=300,
    font=("Roboto", 16, "bold"),
    corner_radius=10,
    command=open_image)
open_button.pack(padx = 20, pady = 20)

app.mainloop()