import customtkinter as ctk 
import random

# Create the main application window
root = ctk.CTk()
root.title("Dice") 
root.geometry("1000x600") 
root.resizable(False, False) 
ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("green") 
root.iconbitmap("FILES\\dice\\Dice.ico") 

# Create a frame to hold other widgets
frame = ctk.CTkFrame(root, corner_radius=40)
frame.pack(padx=20, pady=20, fill='both', expand=True)

# Label to display the dice faces, initially empty
dice = ctk.CTkLabel(frame, text='', font=("Robotto", 520))

# Function to simulate rolling dice
def roll():
    # Unicode characters for dice faces
    dices = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    # Display two random dice faces
    dice.configure(text=f'{random.choice(dices)}{random.choice(dices)}')
    dice.pack()

# Button to trigger the roll function
ctk.CTkButton(
    frame,
    text='ROLL', 
    font=('Blackpast', 48, 'bold'), 
    width=920, 
    height=80, 
    corner_radius=20,
    command=roll 
).pack(pady=20) 

# Start the main event loop
root.mainloop()
