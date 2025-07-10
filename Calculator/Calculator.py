import customtkinter as ctk

# Function to evaluate the expression in the entry widget
def calc():
    expression = ent.get()  # Get the current expression from the entry widget
    try:
        # Evaluate the expression
        result = eval(expression, {"__builtins__": None}, {})
        # Enable the entry, delete current text, and insert the result
        ent.configure(state='normal')
        ent.delete(0, ctk.END)
        ent.insert(0, str(result))
        ent.configure(state='readonly')  # Set back to readonly mode
    except:
        # If there's an error, silently pass
        pass

# Function to insert a character into the entry widget
def ins(c):
    ent.configure(state='normal')  # Temporarily enable the entry widget
    ent.insert(ctk.END, c)  # Insert the character at the end
    ent.configure(state='readonly')  # Set the entry widget back to readonly

# Function to delete the last character from the entry widget
def dele():
    l = len(ent.get())  # Get the length of the current text in the entry
    if l:  # If the length is greater than 0 (not empty)
        ent.configure(state='normal')  # Temporarily enable the entry widget
        ent.delete(l - 1, ctk.END)  # Delete the last character
        ent.configure(state='readonly')  # Set the entry widget back to readonly

# Function to clear the entry widget
def clear():
    ent.configure(state='normal')  # Temporarily enable the entry widget
    ent.delete(0, ctk.END)  # Delete all characters
    ent.configure(state='readonly')  # Set the entry widget back to readonly

# Initialize the main window (root) using customtkinter
root = ctk.CTk()
root.title("Calculator")
ctk.set_appearance_mode('system')  # Set appearance mode to system default (light or dark)
ctk.set_default_color_theme('dark-blue')  # Set the default color theme to dark-blue

# Create a frame to hold the calculator components
frame = ctk.CTkFrame(root, corner_radius=17)
frame.pack(padx=10, pady=10)  # Add some padding around the frame

# Create the entry widget for displaying the current expression or result
ent = ctk.CTkEntry(frame, border_width=0, corner_radius=12, height=30, width=190)
ent.grid(row=0, column=0, columnspan=4, padx=5, pady=5)  # Place it in the grid
ent.configure(state='readonly')  # Initially set the entry widget to readonly mode

# Create the button for closing the application
ctk.CTkButton(frame, corner_radius=12, text='X', width=40, height=40,
              command=root.quit).grid(padx=5, pady=5, column=0, row=1)

# Create the button for clearing the entry
ctk.CTkButton(frame, corner_radius=12, text='C', width=40, height=40,
              command=clear).grid(padx=5, pady=5, column=1, row=1)

# Create the button for deleting the last character
ctk.CTkButton(frame, corner_radius=12, text='<-', width=40, height=40,
              command=dele).grid(padx=5, pady=5, column=2, row=1)

# Create the button for division ("/")
ctk.CTkButton(frame, corner_radius=12, text='/', width=40, height=40,
              command=lambda: ins('/')).grid(padx=5, pady=5, column=3, row=1)

# List of button labels (numbers and basic operations)
buttons = ['7', '8', '9', '*',
           '4', '5', '6', '-',
           '1', '2', '3', '+',
           '0', '.']

# Loop through the list of buttons and create buttons for each one
for i, char in enumerate(buttons):
    ctk.CTkButton(frame, corner_radius=12, text=char, width=40, height=40,
                  command=lambda char=char: ins(char)  # Insert the corresponding character
                  ).grid(padx=5, pady=5, column=i % 4, row=i // 4 + 2)  # Place the button in the grid

# Create the "=" button to evaluate the expression
ctk.CTkButton(frame, corner_radius=12, text='=', width=90, height=40,
              command=calc).grid(padx=5, pady=5, column=2, row=5, columnspan=2)

# Start the main loop to display the window
root.mainloop()