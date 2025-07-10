from tkinter import filedialog
from PIL import Image
import customtkinter as ctk

mode = 'light'

def open_img():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    
    if file_path:
        img = Image.open(file_path)

        # Get the original image dimensions
        img_width, img_height = img.size

        # Set a max display size while maintaining aspect ratio
        max_width, max_height = 720, 420
        img.thumbnail((max_width, max_height), Image.LANCZOS)

        # Convert to CTkImage
        ctk_img = ctk.CTkImage(light_image=img, size=(img.width, img.height))

        # Update the label
        image_label.configure(image=ctk_img, text="")
        image_label.image = ctk_img  # Keep a reference to avoid garbage collection

def save_img():
    if hasattr(image_label, "image") and isinstance(image_label.image, ctk.CTkImage):
        # Get the image from CTkImage
        img = image_label.image._light_image  # Access the original PIL image

        # Ask the user where to save the image
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("BMP files", "*.bmp"), ("GIF files", "*.gif")]
        )

        if file_path:
            img.save(file_path)  # Save the image

def buttons_menu(n):
    pass

# Initialize the main window
app = ctk.CTk()
app.title("Developed by ")
ctk.set_appearance_mode(mode)

# Configure grid layout
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Create the sidebar
side_bar = ctk.CTkFrame(app, corner_radius=26)
side_bar.grid(padx=10, pady=10, row=0, column=0, sticky="ns")

# Add the logo
logo_img = Image.open("icons\logo.png")
logo = ctk.CTkImage(logo_img, size=(160, 57))

ctk.CTkLabel(side_bar,
    image=logo,
    text=""
).pack(padx=10, pady=10)

# Add a button to the sidebar to open an image
img_open = ctk.CTkImage(light_image=Image.open("icons\img.png"), size=(20, 20))

ctk.CTkButton(side_bar, 
    text="Open Image", 
    image=img_open,
    compound="left",
    font=("Helvetice", 16, 'bold'),
    corner_radius=16,
    width=160,
    height=35,
    command=open_img
).pack(padx=10)

# Add a button to the sidebar to save the image
img_save = ctk.CTkImage(light_image=Image.open("icons\save.png"), size=(18, 18))

ctk.CTkButton(side_bar, 
    text="Save Image", 
    image=img_save,
    compound="left",
    font=("Helvetice", 16, 'bold'),
    corner_radius=16,
    width=160,
    height=35,
    command=save_img
).pack(padx=10, pady=10)

def switch_event():
    global mode
    mode = "dark" if switch_var.get() == "on" else "light"
    ctk.set_appearance_mode(mode)

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
image_label = ctk.CTkLabel(image_frame, text="", width=720, height=420)
image_label.pack(padx=20, pady=20)

# Create the horizontal scrollable toolbar
tools_frame = ctk.CTkScrollableFrame(
    app_frame,
    orientation="horizontal",
    height=75,
    corner_radius=16
)
tools_frame.pack(padx=10, pady=10, fill="both", expand=True)

icons = ["icons\\fliph.png", "icons\\contrast.png", "icons\\black.png", "icons\\rotate.png"]

# Add buttons to the toolbar
for i in range(4):
    icon = Image.open(icons[i]).resize((30, 30), Image.LANCZOS)
    ico = ctk.CTkImage(icon)
    
    ctk.CTkButton(
        tools_frame,
        text="",
        image=ico,
        width=50,
        height=50,
        # fg_color="transparent",
        corner_radius=100,
        hover_color=("white", "gray"),
        command=lambda: buttons_menu(i)
    ).pack(side="left", padx=5, pady=10)

# Run the application
app.mainloop()