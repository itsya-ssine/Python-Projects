from PIL import Image
from tkinter.filedialog import *


path = askopenfilename()
img = Image.open(path)
save_path = asksaveasfilename()

img.save(save_path + "_elc.jpg", optimize = True, quality = 50)