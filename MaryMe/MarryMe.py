import customtkinter as ctk
from random import randint
from PIL import Image

# Function to randomly place the "NO" button
def move_no_button():
    no_width, no_height = 150, 35  # Dimensions of the "NO" button
    yes_x, yes_y = 380, 200  # Position of the "YES" button
    yes_width, yes_height = 150, 35  # Dimensions of the "YES" button

    while True:
        # Generate random coordinates for the "NO" button
        x = randint(1, 520)  # Ensure the button stays within the window width
        y = randint(60, 360)  # Ensure the button stays within the window height

        # Check for overlap using bounding box logic
        no_left, no_top = x, y
        no_right, no_bottom = x + no_width, y + no_height

        yes_left, yes_top = yes_x, yes_y
        yes_right, yes_bottom = yes_x + yes_width, yes_y + yes_height

        # Check if the "NO" button overlaps the "YES" button
        if not (no_right > yes_left and no_left < yes_right and
                no_bottom > yes_top and no_top < yes_bottom):
            break  # Exit loop if there is no overlap

    no_button.place(x=x, y=y)

# Function to display the "I LOVE YOU" message
def on_yes_click():
    lab.destroy()
    no_button.destroy()
    yes_button.destroy()

    ima = Image.open('i_love_you.png')

    img = ctk.CTkImage(light_image=ima, dark_image=ima, size = (500,500))
    label = ctk.CTkLabel(frame, text = '', image = img)
    label.pack(padx = 20, pady = 20)


# Initialize the main window
elc = ctk.CTk()
elc.geometry("720x450")
elc.title("Love You")
elc.iconbitmap("icon.ico")
elc.resizable(False, False)
ctk.set_appearance_mode("light")

# Create a frame to hold widgets
frame = ctk.CTkFrame(elc)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Add a label with the proposal question
lab = ctk.CTkLabel(frame,
                    text = 'WILL YOU MARRY ME ?',
                    width = 400,
                    height = 30,
                    text_color='#ff005a',
                    font = ("Merienda ExtraBold", 30, "bold"))
lab.pack(padx = 10, pady = 10)

# Add the "NO" button that moves when clicked
no_button = ctk.CTkButton(
    frame,
    text="NO",
    height=35,
    width=150,
    fg_color='#ff5a94',
    hover_color='#ff3b80',
    font=("Helvetica", 16, "bold"),
    command=move_no_button
)
no_button.place(x=150, y=200)

# Add the "YES" button that displays the love message
yes_button = ctk.CTkButton(
    frame,
    text="YES",
    height=35,
    width=150,
    fg_color='#ff5a94',
    hover_color='#ff3b80',
    font=("Helvetica", 16, "bold"),
    command=on_yes_click
)
yes_button.place(x=380, y=200)

# Run the application
elc.mainloop()