from tkinter import *
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

# Create the main window
root = Tk()
root.title("Display Image with Tkinter")

def generate_qr():
    # Generate QR code
    text = input_field.get()
    qr_image = qrcode.make(text)
    
    # Save QR code as an image
    qr_image.save("qrcode.png")
    
    # Display the QR code
    img = Image.open("qrcode.png")
    img = ImageTk.PhotoImage(img)
    
    # Update the label with the QR code
    qr_label.config(image=img)
    qr_label.image = img

def save_qr():
    # Generate QR code
    text = input_field.get()
    qr_image = qrcode.make(text)
    
    # Open a file dialog to select where to save the image
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    
    if file_path:
        # Save the QR code to the selected file
        qr_image.save(file_path)

# Input field for text
input_field = Entry(root)
input_field.grid(row=0, column=1)

# Label for instruction
label = Label(root, text='Enter text:', bg='cyan')
label.grid(row=0, column=0)

# Button to generate QR code
Button1 = Button(root, text="Generate QR Code", command=generate_qr)
Button1.grid(row=0, column=2)

# Button to save QR code
Button2 = Button(root, text="Save QR Code", command=save_qr)
Button2.grid(row=0, column=3)

# Label to display the QR code
qr_label = Label(root)
qr_label.grid(row=1, column=0, columnspan=4)

root.mainloop()