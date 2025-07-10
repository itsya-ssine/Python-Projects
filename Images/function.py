from tkinter.filedialog import askopenfilename, asksaveasfilename
import customtkinter as ctk
from PIL import Image, ImageTk

def open_image():
    path = askopenfilename()
    if path:
        image = Image.open(path)
        img = ctk.CTkImage(light_image=image, dark_image=image, size=(720, 480))
        return img
    return None

def save_image(img):
    path = asksaveasfilename(defaultextension=".png", filetypes=[("*PNG Files", "*.png")])
