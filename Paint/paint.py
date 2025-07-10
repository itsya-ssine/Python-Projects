from PIL import Image, ImageGrab
from tkinter.filedialog import asksaveasfilename
import customtkinter as ctk
import tkinter as tk

# Set appearance and theme
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

# Initialize the main window
root = ctk.CTk()
root.title("White Board")
root.geometry("1050x570")
root.iconbitmap("FILES\\paint\\icon.ico")
root.resizable(False, False)

last_x = 0
last_y = 0
color = 'black'

# Change color function
def change_color(new_color):
    global color
    color = new_color

# Start drawing function
def start_drawing(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

# Draw function
def draw(event):
    global last_x, last_y
    canvas.create_line((last_x, last_y, event.x, event.y), fill=color, width=float(current_value.get()),
                       capstyle='round', smooth=True)
    last_x, last_y = event.x, event.y

# Save image function with error handling and format options
def save_image():
    x = app_frame.winfo_rootx() + canvas.winfo_x()
    y = app_frame.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    file_path = asksaveasfilename(defaultextension=".png",
                                  filetypes=[("PNG Files", "*.png"),
                                             ("JPEG Files", "*.jpg"),
                                             ("BMP Files", "*.bmp")])
    if file_path:
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

# Create app frame
app_frame = ctk.CTkFrame(root)
app_frame.pack(padx=10, pady=10, fill='both', expand=True)

# Color palette
color_box = ctk.CTkFrame(app_frame, corner_radius=50)
color_box.place(x=15, y=15)

def create_button(button_color, y):
    ctk.CTkButton(
        color_box,
        text='',
        width=40,
        height=40,
        corner_radius=20,
        fg_color=button_color,
        hover_color=button_color,
        command=lambda: change_color(button_color)
    ).pack(pady=y, padx=10)

colors = ('black', 'gray', 'red', '#0066ff', '#008d28', '#ff49a7', '#ff8a00', '#00baff', 'yellow')

for i, clr in enumerate(colors):
    create_button(clr, (not i % 2) * 10)

# Eraser button
eraser_icon = ctk.CTkImage(Image.open("FILES\\paint\\goma.png"), size=(30, 30))
ctk.CTkButton(
    color_box,
    image=eraser_icon,
    text='',
    fg_color='#cfcfcf',
    hover_color='#cfcfcf',
    width=40,
    height=40,
    command=lambda: change_color('white')
).pack(pady=10)

# Canvas
canvas = tk.Canvas(app_frame, width=1375, height=700, background='white', cursor='hand2')
canvas.place(x=135, y=30)

canvas.bind('<1>', start_drawing)
canvas.bind('<B1-Motion>', draw)

pen_img = ctk.CTkImage(Image.open('FILES\\paint\\pen.png'), size=(30, 30))
ctk.CTkLabel(app_frame, image=pen_img, text='').place(x=100, y=504)

# Pen size slider
current_value = ctk.DoubleVar(value=5.0)

def slider_change(value):
    value_label.configure(text=f"{float(value):.2f}")

slider = ctk.CTkSlider(app_frame, from_=1, to=30, orientation='horizontal', 
                       command=slider_change, variable=current_value)
slider.place(x=140, y=512)

value_label = ctk.CTkLabel(app_frame, text=f"{current_value.get():.2f}")
value_label.place(x=350, y=505)

# Clear button
clear_img = ctk.CTkImage(Image.open('FILES\\paint\\clear.png'), size=(25, 25))
ctk.CTkButton(
    app_frame,
    image=clear_img,
    text=' CLEAR',
    font=("Helvetica", 16, "bold"),
    command=lambda: canvas.delete('all')
).place(x=700, y=504)

# Save button
save_img = ctk.CTkImage(Image.open('FILES\\paint\\save.png'), size=(25, 25))
ctk.CTkButton(
    app_frame,
    image=save_img,
    text=' SAVE',
    font=("Helvetica", 16, "bold"),
    command=save_image
).place(x=850, y=504)

root.mainloop()