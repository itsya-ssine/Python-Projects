import customtkinter as ctk
from random import randint

def cmd():
    x = randint(1, 550)
    y = randint(50, 300)

    while x <= 530 and x >= 320 and y <= 235 and y >= 165:
        x = randint(1, 550)
        y = randint(50, 300)

    no.place(x = x, y = y)

def yesb():
    lab.destroy()
    no.destroy()
    yes.destroy()

    la = ctk.CTkLabel(frame,
                    text = 'Kifach nta osm ? hh',
                    width = 400,
                    height = 30,
                    font = ("Roboto", 30, "bold"))
    la.pack(padx = 10, pady = 40)

elc = ctk.CTk()
elc.geometry("720x430")
elc.title('Gay hh')
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

frame = ctk.CTkFrame(elc)
frame.pack(padx = 20, pady = 20, fill = 'both', expand = True)

lab = ctk.CTkLabel(frame,
                    text = 'ARE YOU GAY ?',
                    width = 400,
                    height = 30,
                    font = ("Roboto", 24, "bold"))
lab.pack(padx = 10, pady = 20)

no = ctk.CTkButton(frame,
                    text = 'NO',
                    height = 35,
                    width = 150,
                    font = ("Roboto", 16, "bold"),
                    command = cmd)
no.place(x = 150, y = 200)

yes = ctk.CTkButton(frame,
                    text = 'YES',
                    height = 35,
                    width = 150,
                    font = ("Roboto", 16, "bold"),
                    command = yesb)
yes.place(x = 380, y = 200)

elc.mainloop()