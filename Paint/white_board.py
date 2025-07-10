from PIL import Image, ImageGrab
from tkinter.filedialog import *
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

root = ctk.CTk()
root.title("Paint")
root.geometry("1050x570")
root.iconbitmap("FILES\\paint\\icon.ico")
root.resizable(False, False)

last_x = 0
last_y = 0
color = 'black'

def change_color(new_color):
    global color
    color = new_color

def start_drawing(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line((last_x, last_y, event.x, event.y), fill=color, width=get_current_value(),
                       capstyle='round', smooth=True)
    last_x, last_y = event.x, event.y

def save_image():
    x = app_frame.winfo_rootx() + canvas.winfo_x()
    y = app_frame.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    path = asksaveasfilename()

    ImageGrab.grab().crop((x, y, x1, y1)).save(path + '.png')


app_frame = ctk.CTkFrame(root)
app_frame.pack(padx=10, pady=10, fill='both', expand=True)


color_box = ctk.CTkFrame(app_frame, corner_radius=50)
color_box.place(x=15, y=15)

def create_button(button_color, y):
    button = ctk.CTkButton(
        color_box,
        text = '',
        width = 40,
        height = 40,
        corner_radius = 20,
        fg_color = button_color,
        hover_color = button_color,
        command = lambda: change_color(button_color)
    )
    button.pack(pady=y, padx=10)

colors = ('black', 'gray', 'red', '#0066ff', '#008d28', '#ff49a7', '#ff8a00', '#00baff', 'yellow')

for i, clr in enumerate(colors):
    create_button(clr, (not i%2)*10)


era = Image.open("FILES\\paint\\goma.png")
eraser_icon = ctk.CTkImage(light_image=era, dark_image=era, size=(30, 30))

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


canvas = tk.Canvas(app_frame, width=1375, height=700, background='white', cursor='hand2')
canvas.place(x=135, y=30)

canvas.bind('<1>', start_drawing)
canvas.bind('<B1-Motion>', draw)

current_value = ctk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_change(event):
    value_label.configure(text=get_current_value())

pen = Image.open('FILES\\paint\\pen.png')
pen_img = ctk.CTkImage(light_image=pen, dark_image=pen, size=(30, 30))
ctk.CTkLabel(
    app_frame,
    image=pen_img,
    text='',
).place(x=100, y=504)

slider = ctk.CTkSlider(
    app_frame, 
    from_=0, 
    to=100, 
    orientation='horizontal',
    command=slider_change,
    variable=current_value
)
slider.place(x=140, y=512)

value_label = ctk.CTkLabel(app_frame, text=get_current_value())
value_label.place(x=350, y=505)


clear = Image.open('FILES\\paint\\clear.png')
clear_img = ctk.CTkImage(light_image=clear, dark_image=clear, size=(25, 25))

ctk.CTkButton(
    app_frame,
    image=clear_img,
    text=' CLEAR',
    font=("Helvetica", 16, "bold"),
    command=lambda: canvas.delete('all')
).place(x=700, y=504)


save = Image.open('FILES\\paint\\save.png')
save_img = ctk.CTkImage(light_image=save, dark_image=save, size=(25, 25))

ctk.CTkButton(
    app_frame,
    image=save_img,
    text=' SAVE',
    font=("Helvetica", 16, "bold"),
    command=save_image
).place(x=850, y=504)

root.mainloop()