from tkinter import filedialog
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import customtkinter as ctk

# Global variable to store the CTkImage object
ctk_img = None

def open_img(current_image, image_label):
    global ctk_img
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

    if file_path:
        # Open and store the original image
        current_image = Image.open(file_path)

        # Create a copy of the image for display purposes
        display_image = current_image.copy()

        # Set a max display size while maintaining aspect ratio
        max_width, max_height = 720, 420
        display_image.thumbnail((max_width, max_height), Image.LANCZOS)

        # Convert to CTkImage and store it in the global variable
        ctk_img = ctk.CTkImage(light_image=display_image, dark_image=display_image, size=(display_image.width, display_image.height))

        # Update the label
        image_label.configure(image=ctk_img, text="")
        image_label.image = ctk_img  # Keep a reference to avoid garbage collection

    return current_image

def save_img(current_image):
    if current_image:
        # Ask the user where to save the image
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("BMP files", "*.bmp"), ("GIF files", "*.gif")]
        )

        if file_path:
            # Save the original image
            current_image.save(file_path)

def close_img(current_image, image_label):
    global ctk_img
    # Reset the current_image variable
    current_image = None

    empty_image = Image.new("RGBA", (720, 420), (0, 0, 0, 0))  # Transparent placeholder
    ctk_img = ctk.CTkImage(light_image=empty_image, dark_image=empty_image, size=(720, 420))

    image_label.configure(image=ctk_img, text="No Image yet")

def buttons_menu(index, current_image, image_label):
    global ctk_img
    if current_image:
        try:
            # Apply transformation based on button index
            if index == 0:
                res_image = current_image.transpose(Image.FLIP_LEFT_RIGHT)
            elif index == 1:
                res_image = current_image.transpose(Image.FLIP_TOP_BOTTOM)
            elif index == 2:
                res_image = current_image.rotate(90, expand=True)
            elif index == 3:
                res_image = current_image.convert("L")
            elif index == 4:
                res_image = ImageEnhance.Brightness(current_image).enhance(1.5)
            elif index == 5:
                res_image = ImageEnhance.Contrast(current_image).enhance(1.5)
            elif index == 6:
                res_image = Image.fromarray(255 - np.array(current_image))
            elif index == 7:
                res_image = current_image.filter(ImageFilter.BLUR)
            elif index == 8:
                res_image = current_image.filter(ImageFilter.SHARPEN)
            elif index == 9:
                res_image = current_image.filter(ImageFilter.FIND_EDGES)
            else:
                return current_image

            # Update current_image reference
            current_image = res_image

            # Resize for display
            display_image = res_image.copy()
            max_width, max_height = 720, 420
            display_image.thumbnail((max_width, max_height), Image.LANCZOS)

            # Convert to CTkImage
            ctk_img = ctk.CTkImage(light_image=display_image, dark_image=display_image, size=(display_image.width, display_image.height))

            # Update label
            image_label.configure(image=ctk_img, text="")
            image_label.image = ctk_img

        except :
            pass

    return current_image
