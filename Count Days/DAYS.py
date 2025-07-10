import customtkinter as ctk

FICHIER = 'days.txt'

try:
    fp = open(FICHIER, 'r')
    days = int(fp.read())
    fp.close()
except FileNotFoundError:
    fp = open(FICHIER, 'w')
    days = 0
    fp.close

def update(day):
    lab.configure(text = str(day) + ' DAYS')

def new():
    fp = open(FICHIER, 'w')
    fp.write(str(days + 1))
    fp.close()
    update(days + 1)

def fuck():
    fp = open(FICHIER, 'w')
    fp.write('0')
    fp.close()
    update(0)

root = ctk.CTk()
root.geometry("720x430")
root.title('90 DAYS')
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

frame = ctk.CTkFrame(root)
frame.pack(padx = 20, pady = 20, fill = 'both', expand = True)

lab = ctk.CTkLabel(frame,
                    text = str(days) + ' DAYS',
                    width = 400,
                    height = 30,
                    font = ("Roboto", 50, "bold"))
lab.grid(row = 0, column = 0, columnspan = 2, padx = 40, pady = 50, sticky="nsew")

no = ctk.CTkButton(frame,
                    text = 'NEW DAY',
                    height = 35,
                    width = 150,
                    font = ("Roboto", 25, "bold"),
                    command = new)
no.grid(row = 1, column = 0, padx = 50, pady = 50, sticky="nsew")

yes = ctk.CTkButton(frame,
                    text = 'FUCK',
                    height = 35,
                    width = 150,
                    font = ("Roboto", 25, "bold"),
                    command = fuck)
yes.grid(row = 1, column = 1, padx = 50, pady = 50, sticky="nsew")

frame.grid_rowconfigure(0, weight=2)
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

root.mainloop()