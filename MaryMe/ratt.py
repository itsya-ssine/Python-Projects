import customtkinter as ctk
from random import randint

def move_no_button():
    while True:
        x = randint(1, 520) 
        y = randint(50, 360)  

        no_left, no_top = x, y
        no_right, no_bottom = x + 150, y + 35

        yes_left, yes_top = 380, 200
        yes_right, yes_bottom = 430, 235

        if not (no_right > yes_left and no_left < yes_right and
                no_bottom > yes_top and no_top < yes_bottom):
            break 

    no_button.place(x=x, y=y)


def yes():
    lab.destroy()
    no_button.destroy()
    yes_button.destroy()

    def aj_hh():
        aj_button.destroy()
        nv_button.destroy()

        ctk.CTkLabel(frame, text='Nn AJ hh',
                     font=("Helvetica", 50, "bold"),
        ).pack(padx=10,pady=150)


    nv_button = ctk.CTkButton(
        frame,
        text="NV",
        height=50,
        width=150,
        font=("Helvetica", 30, "bold"),
        command=aj_hh
    )
    nv_button.place(x=150, y=175)


    aj_button = ctk.CTkButton(
        frame,
        text="AJ",
        height=50,
        width=150,
        font=("Helvetica", 30, "bold"),
        command=elc.destroy
    )
    aj_button.place(x=380, y=175)

elc = ctk.CTk()
elc.geometry("720x450")
elc.title("RATTRAPAGE")
elc.resizable(False, False)
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

frame = ctk.CTkFrame(elc)
frame.pack(padx=20, pady=20, fill="both", expand=True)

lab = ctk.CTkLabel(frame,
                    text = 'RATTRAPAGE يتصل بك',
                    width = 400,
                    height = 30,
                    font = ("Helvetica", 30, "bold"))
lab.pack(padx = 10, pady = 10)

no_button = ctk.CTkButton(
    frame,
    text="رفض",
    height=35,
    width=150,
    font=("Helvetica", 20, "bold"),
    command=move_no_button
)
no_button.place(x=150, y=200)

yes_button = ctk.CTkButton(
    frame,
    text="قبول",
    height=35,
    width=150,
    font=("Helvetica", 20, "bold"),
    command=yes
)
yes_button.place(x=380, y=200)

elc.mainloop()