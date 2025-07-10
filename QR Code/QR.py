from tkinter import filedialog
import customtkinter as ctk
from PIL import Image
import qrcode
import io

def create_qrcode():
    qr = qrcode.QRCode(version=10, box_size=10, border=5)
    url = entry.get()  # Get URL from entry
    entry.delete(0, ctk.END)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Convert the PIL image to a format that CustomTkinter understands
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    pil_img = Image.open(img_bytes)
    
    # Convert to CTkImage
    qr_image = ctk.CTkImage(dark_image=pil_img, light_image=pil_img, size=(300, 300))
    
    # Set the image to the label and prevent garbage collection
    img_qr.image = qr_image
    img_qr.configure(image=qr_image)
    img_qr.pack(padx=10, pady=10)

    img_qr.pack(pady=10)
    save_button.pack(padx=10, pady=10)

def save_qr_code():
    # Save the QR code image to a file
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if file_path:
        img_qr.image._dark_image.save(file_path)

# Initialize the root window
root = ctk.CTk()
root.geometry('500x600')
root.title('QRCode')
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

# Create a frame for layout
frame = ctk.CTkFrame(root, corner_radius=20)
frame.pack(padx=20, pady=20, fill='both', expand=True)

# Label to prompt for URL
label = ctk.CTkLabel(frame, text='Enter your URL:', font=('Helvetica', 20, 'bold'))
label.pack(padx=10, pady=10)

# Entry widget to enter URL
entry = ctk.CTkEntry(frame, width=400, height=40, font=('Helvetica', 16), corner_radius=20)
entry.pack()

# Button to generate the QR code
button = ctk.CTkButton(
    frame, 
    width=400, 
    height=40, 
    text='GENERATE', 
    corner_radius=20, 
    font=('Helvetica', 16, 'bold'), 
    command=create_qrcode
)
button.pack(padx=10, pady=10)

# Label to display the generated QR code
img_qr = ctk.CTkLabel(frame, text='')

# Button to save the QR code
save_button = ctk.CTkButton(
    frame, 
    width=200, 
    height=40, 
    text='SAVE', 
    corner_radius=20, 
    font=('Helvetica', 16, 'bold'), 
    command=save_qr_code
)

# Run the main loop
root.mainloop()