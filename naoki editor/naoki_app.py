import customtkinter as ctk
from image_functions import *

# Global variables
mode = 'light'
current_image = None  # To store the original image

def switch_event():
    global mode
    mode = "dark" if switch_var.get() == "on" else "light"
    ctk.set_appearance_mode(mode)

# Initialize the main window
app = ctk.CTk()
app.title("Developed by @__itsnaoki__")
ctk.set_appearance_mode(mode)

# Configure grid layout
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Create the sidebar
side_bar = ctk.CTkFrame(app, corner_radius=26)
side_bar.grid(padx=10, pady=10, row=0, column=0, sticky="ns")

# Add the logo
logo_img = Image.open("icons\\logo.png")
logo = ctk.CTkImage(light_image=logo_img, dark_image=logo_img, size=(160, 57))

ctk.CTkLabel(side_bar, image=logo, text="").pack(padx=10, pady=10)

# Add a button to the sidebar to open an image
img_open = ctk.CTkImage(light_image=Image.open("icons\\img.png"), 
                        dark_image=Image.open("icons\\img.png"), 
                        size=(20, 20))

ctk.CTkButton(side_bar, 
    text="Open Image", 
    image=img_open,
    compound="left",
    font=("Helvetica", 16, 'bold'),
    corner_radius=16,
    width=160,
    height=35,
    command=lambda: globals().update(current_image=open_img(current_image, image_label))
).pack(padx=10)

# Add a button to the sidebar to save the image
img_save = ctk.CTkImage(light_image=Image.open("icons\\save.png"),
                        dark_image=Image.open("icons\\save.png"),
                        size=(18, 18))

ctk.CTkButton(side_bar, 
    text="Save Image", 
    image=img_save,
    compound="left",
    font=("Helvetica", 16, 'bold'),
    corner_radius=16,
    width=160,
    height=35,
    command=lambda: save_img(current_image)
).pack(padx=10, pady=10)

# Add a button to the sidebar to close the image
close_button = ctk.CTkButton(
    side_bar,
    text="Close Image",
    font=("Helvetica", 16, 'bold'),
    corner_radius=16,
    width=160,
    height=35,
    # command=close_img
    command=lambda: globals().update(current_image=close_img(current_image, image_label))
)
close_button.pack(padx=10)

# Add a switch for dark mode
switch_var = ctk.StringVar(value="off")
ctk.CTkSwitch(side_bar, 
    text="Dark mode", 
    command=switch_event,
    variable=switch_var, 
    onvalue="on", 
    offvalue="off"
).pack(side="bottom", padx=10, pady=10)

# Create the main application frame
app_frame = ctk.CTkFrame(app, corner_radius=26)
app_frame.grid(padx=10, pady=10, row=0, column=1, sticky="nsew")

# Create the image display frame
image_frame = ctk.CTkFrame(app_frame, corner_radius=16, width=720, height=480)
image_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Create the label to display the image
image_label = ctk.CTkLabel(image_frame, text="No Image yet", width=720, height=420)
image_label.pack(padx=20, pady=20, fill="both", expand=True)

# Create the horizontal scrollable toolbar
tools_frame = ctk.CTkScrollableFrame(
    app_frame,
    orientation="horizontal",
    height=75,
    corner_radius=16
)
tools_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Add buttons to the toolbar
icons = ["icons\\fliph.png", 
         "icons\\flipv.png", 
         "icons\\rotate.png", 
         "icons\\black.png", 
         "icons\\brightness.png",
         "icons\\contrast.png",
         "icons\\colors.png",
         "icons\\blur.png",
         "icons\\sharpen.png",
         "icons\\square.png"]

for i in range(len(icons)):
    icon = Image.open(icons[i]).resize((30, 30), Image.LANCZOS)
    ico = ctk.CTkImage(light_image=icon, dark_image=icon)
    
    ctk.CTkButton(
        tools_frame,
        text="",
        image=ico,
        width=50,
        height=50,
        corner_radius=100,
        hover_color=("white", "gray"),
        command=lambda i=i: globals().update(current_image=buttons_menu(i, current_image, image_label))
    ).pack(side="left", padx=5, pady=10)

# Run the application
app.mainloop()