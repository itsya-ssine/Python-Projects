from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
import numpy as np

# Global variables
mode = 'light'
current_image = None  # To store the original image

def open_img():
    global current_image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    
    if file_path:
        # Open and store the original image
        current_image = Image.open(file_path)

        # Create a copy of the image for display purposes
        display_image = current_image.copy()

        # Set a max display size while maintaining aspect ratio
        max_width, max_height = 720, 420
        display_image.thumbnail((max_width, max_height), Image.LANCZOS)

        # Convert to CTkImage
        ctk_img = ctk.CTkImage(light_image=display_image, dark_image=display_image, size=(display_image.width, display_image.height))

        # Update the label
        image_label.configure(image=ctk_img, text="")
        image_label.image = ctk_img  # Keep a reference to avoid garbage collection

def save_img():
    global current_image
    if current_image:
        # Ask the user where to save the image
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("BMP files", "*.bmp"), ("GIF files", "*.gif")]
        )

        if file_path:
            # Save the original image
            current_image.save(file_path)

def close_img():
    global current_image
    # Reset the current_image variable
    current_image = None

    # Clear the image from the label
    image_label.configure(image=None, text="")
    image_label.image = None  # Remove the reference to the image

import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

def buttons_menu(index):
    global current_image
    if current_image:
        # Convert the image to a NumPy array (if needed)
        image_array = np.array(current_image)

        if index == 0:  # Flip horizontally
            res_array = np.flip(image_array, axis=1)
        elif index == 1:  # Flip vertically
            res_array = np.flip(image_array, axis=0)
        elif index == 2:  # Rotate 90 degrees counterclockwise
            res_array = np.rot90(image_array)
        elif index == 3:  # Convert to grayscale
            if len(image_array.shape) == 3:  # Check if the image is RGB
                res_array = np.dot(image_array[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
            else:
                res_array = image_array  # If already grayscale, do nothing
        elif index == 4:  # Adjust brightness
            enhancer = ImageEnhance.Brightness(current_image)
            res_image = enhancer.enhance(1.5)  # Increase brightness by 50%
            res_array = np.array(res_image)
        elif index == 5:  # Adjust contrast
            enhancer = ImageEnhance.Contrast(current_image)
            res_image = enhancer.enhance(1.5)  # Increase contrast by 50%
            res_array = np.array(res_image)
        elif index == 6:  # Invert colors
            res_array = 255 - image_array  # Invert the image
        elif index == 7:  # Apply blur
            res_image = current_image.filter(ImageFilter.BLUR)
            res_array = np.array(res_image)
        elif index == 8:  # Apply sharpening
            res_image = current_image.filter(ImageFilter.SHARPEN)
            res_array = np.array(res_image)
        elif index == 9:  # Edge detection
            res_image = current_image.filter(ImageFilter.FIND_EDGES)
            res_array = np.array(res_image)
        else:
            return  # Do nothing for other buttons

        # Convert the result array back to a PIL image
        res_image = Image.fromarray(res_array)

        # Update the global current_image
        current_image = res_image

        # Create a display copy of the result image
        display_image = res_image.copy()
        max_width, max_height = 720, 420
        display_image.thumbnail((max_width, max_height), Image.LANCZOS)

        # Convert to CTkImage and update the label
        ctk_img = ctk.CTkImage(light_image=display_image, dark_image=display_image, size=(display_image.width, display_image.height))
        image_label.configure(image=ctk_img, text="")
        image_label.image = ctk_img

def switch_event():
    global mode
    mode = "dark" if switch_var.get() == "on" else "light"
    ctk.set_appearance_mode(mode)

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
logo_img = Image.open("logo.png")
logo = ctk.CTkImage(light_image=logo_img, dark_image=logo_img, size=(160, 57))

ctk.CTkLabel(side_bar, image=logo, text="").pack(padx=10, pady=10)

# Add a button to the sidebar to open an image
img_open = ctk.CTkImage(light_image=Image.open("img.png"), dark_image=Image.open("img.png"), size=(20, 20))

ctk.CTkButton(side_bar, 
    text="Open Image", 
    image=img_open,
    compound="left",
    font=("Helvetica", 16, 'bold'),
    corner_radius=16,
    width=160,
    height=35,
    command=open_img
).pack(padx=10)

# Add a button to the sidebar to save the image
img_save = ctk.CTkImage(light_image=Image.open("save.png"), dark_image=Image.open("save.png"), size=(18, 18))

ctk.CTkButton(side_bar, 
    text="Save Image", 
    image=img_save,
    compound="left",
    font=("Helvetica", 16, 'bold'),
    corner_radius=16,
    width=160,
    height=35,
    command=save_img
).pack(padx=10, pady=10)

# Add a button to the sidebar to close the image
close_button = ctk.CTkButton(
    side_bar,
    text="Close Image",
    font=("Helvetica", 16, 'bold'),
    corner_radius=16,
    width=160,
    height=35,
    command=close_img  # Call the close_img function
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
image_label = ctk.CTkLabel(image_frame, text="", width=720, height=420)
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
        command=lambda i=i: buttons_menu(i)
    ).pack(side="left", padx=5, pady=10)

# Run the application
app.mainloop()