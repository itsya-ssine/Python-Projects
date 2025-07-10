import customtkinter as ctk
from PIL import Image

def sign_in():
    pass

def sign_up():
    pass

def icons_menu(i):
    pass

root = ctk.CTk()
root.title("Sign In")
root.geometry("1000x500")
root.iconbitmap("icon.ico")
root.configure(fg_color="white")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
ctk.set_appearance_mode("light")


frame1 = ctk.CTkFrame(root, fg_color="white", corner_radius=0)
frame1.grid(row=0, column=0, sticky="nsew")

frame2 = ctk.CTkFrame(root, fg_color="#624CAB", corner_radius=100)
frame2.grid(row=0, column=1, sticky="nsew")

title_font = ctk.CTkFont("Alexandria ExtraBold", 50, "bold")
label_font = ctk.CTkFont("Gill Sans Nova", 12)

# Frame 1 -----------------------------------------------------
ctk.CTkLabel(frame1,text='').pack(pady=10)

ctk.CTkLabel(
    frame1,
    text = "Sign In",
    font = title_font
).pack()

f1 = ctk.CTkFrame(frame1, fg_color="white")
f1.pack()

email = ctk.CTkImage(Image.open("envelope.png"), size=(30, 30))
facebook = ctk.CTkImage(Image.open("facebook.png"), size=(30, 30))
github = ctk.CTkImage(Image.open("github.png"), size=(30, 30))
linkedin = ctk.CTkImage(Image.open("linkedin.png"), size=(30, 30))

icons = [email, facebook, github, linkedin]

for i in range(4):
    ctk.CTkButton(
        f1,
        text="",
        image=icons[i],
        fg_color="transparent",
        border_width=None,
        width=50,
        height=50,
        hover_color="white",
        cursor="hand2", 
        command=lambda: icons_menu(i)
    ).grid(row=0, column=i, padx=5, pady=5)

ctk.CTkLabel(
    frame1,
    text="or use email password",
    font=label_font
).pack()

email_entry = ctk.CTkEntry(
    frame1,
    width=400,
    height=35,
    border_width=0.6,
    corner_radius=10,
    placeholder_text="Email"
).pack(padx=30, pady=10)

email_entry = ctk.CTkEntry(
    frame1,
    width=400,
    height=35,
    border_width=0.6,
    corner_radius=10,
    placeholder_text="Password"
).pack(padx=30, pady=10)

ctk.CTkButton(
    frame1,
    text="Forget Your Password ?",
    fg_color="transparent",
    hover_color="white",
    text_color="black",
    font=label_font,
    cursor="hand2"
).pack(pady=10)

ctk.CTkButton(
    frame1,
    text="Sign In",
    font=("Gill Sans Nova", 24, "bold"),
    fg_color="#624CAB",
    hover_color="#35256A",
    corner_radius=10,
    cursor="hand2",
    width=200,
    height=45,
    command=sign_in
).pack()
# -------------------------------------------------------------

# Frame 2 -----------------------------------------------------
ctk.CTkLabel(frame2,text='').pack(pady=50)

ctk.CTkLabel(
    frame2,
    text = "Hello !",
    text_color="white",
    font = title_font
).pack(pady=10)

ctk.CTkLabel(
    frame2,
text="Follow @coding_elc for more content about programming",
    text_color="white",
    font=label_font
).pack(padx=80)

ctk.CTkButton(
    frame2,
    text="Sign Up",
    font=("Gill Sans Nova", 20, "bold"),
    fg_color="transparent",
    hover_color="#624CAB",
    border_color="white",
    border_width=1,
    corner_radius=10,
    cursor="hand2",
    width=200,
    height=45,
    command=sign_up
).pack(pady=20)
# -------------------------------------------------------------



root.mainloop()