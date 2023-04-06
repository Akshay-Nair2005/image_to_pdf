import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from tkinter import font as tkfont
from PIL import ImageTk, Image
import time
import os


# function to convert images to PDF
def images_to_pdf(images, pdf_name):
    try:
        # create a new pdf file
        pdf = Image.open(images[0])
        pdf.save(pdf_name, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
        messagebox.showinfo("Success", "Images have been successfully converted to PDF.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to convert images to PDF.\nError: " + str(e))
# function to select images
def select_images():
    images = filedialog.askopenfilenames(title="Select Images", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"),("All files", "*.*")), initialdir = "C:/")
    return images
# function to select pdf name and path
def select_pdf():
    pdf = filedialog.asksaveasfilename(title="Save PDF As", defaultextension=".pdf", initialdir = "C:/", filetypes=(("PDF files", "*.pdf"),("All files", "*.*")))
    return pdf
# create GUI
root = tk.Tk()
root.title("Convert Images to PDF")
root.wm_attributes('-fullscreen',True)
root.configure(bg="white")
root.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

#create a canvas
canvas = tk.Canvas(root, width=700, height=3500)
canvas.pack(fill="both", expand=True)

#Add image
img = Image.open("convert_img to_pdf.png")
img = img.resize((800, 600), Image.LANCZOS)
bg_img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=bg_img, anchor="nw")


def resize_bg(event):
    new_width = event.width
    new_height = event.height
    bg_img_resize = img.resize((new_width, new_height), Image.LANCZOS)
    canvas.bg_img = ImageTk.PhotoImage(bg_img_resize)
    canvas.itemconfig(bg, image=canvas.bg_img)

bg = canvas.create_image(0, 0, image=bg_img, anchor="nw")
canvas.bind('<Configure>', resize_bg)
#select image
select_images_btn = tk.Button(root, text="Select Images", font=("Helvetica", 17),relief = "ridge", command=select_images,width=20,height=3,bg="#ECE5FA")
select_images_btn.place(x=530,y=240)

#select pdf
select_pdf_btn = tk.Button(root, text="Select PDF", font=("Helvetica", 17),relief = "ridge", command=select_pdf,width=20,height=3,bg="#ECE5FA")
select_pdf_btn.place(x=530,y=390)

#convert button
convert_btn = tk.Button(root, text="Convert", font=("Helvetica", 17),relief = "ridge", command=lambda: images_to_pdf(select_images(), select_pdf()),width=20,height=3,bg="#ECE5FA")
convert_btn.place(x=530,y=530)

# Button for closing
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 17),relief = "ridge", command=root.destroy,bg="#A881A7",width=10,height=2)
exit_button.place(x=20,y=660)

root.mainloop()
