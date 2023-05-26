import PIL
from PIL import ImageTk
import tkinter
from tkinter import *
from tkinter import filedialog
from docx2pdf import convert
from pillow_heif import register_heif_opener
import platform
import pathlib
import os


# Resets the GUI title and removes indicator icons
def close():
    window.quit()

# opens file dialog to allow user to choose the file they want to convert and saves a copy as a...
# JPEG in the same directory
def convert_to_jpg():
    register_heif_opener()
    if platform.system() == "Windows":
        filepath = filedialog.askopenfilename(initialdir="C:/")
        
    else:
        filepath = filedialog.askopenfilename(initialdir="/home/")
    try:
        if type(filepath) is tuple:
            label2.place(x=250, y=150)
            label.config(text="Unsuccesful :(")
            window.after(4000,setTextBack)
        else:
            img = PIL.Image.open(""+filepath)
            newImg = img.convert('RGB')
            newImg.save(filepath[:-4]+" JPEG.jpg") 
            label1.place(x=250, y=150)
            label.config(text="Successful!")
            label3.config(text="You can find your converted image at "+filepath[:-4]+" JPEG.jpg")
            window.after(4000,setTextBack)
    except:
        label2.place(x=250, y=150)
        label.config(text="Unsuccessful :(")
        window.after(4000,close)

# opens file dialog to allow user to choose the .docx file they want to convert and saves a copy...
# as a .pdf file in the same directory
def convert_to_pdf():
    if platform.system() == "Windows":
        filepath = filedialog.askopenfilename(initialdir="C:/")
        try:
            if type(filepath) is tuple:
                label2.place(x=250, y=150)
                label.config(text="Unsuccessful :(")
                window.after(4000,setTextBack)
            else: 
                convert(filepath)
                label1.place(x=250, y=150)
                label.config(text="Successful!")
                label3.config(text="You can find your converted file at "+filepath[:-4]+".pdf")
                window.after(4000,setTextBack)
        except:
            label2.place(x=250, y=150)
            label.config(text="Unsuccessful :(")
            window.after(4000,setTextBack)
    else:
        filepath = filedialog.askopenfilename(initialdir="/home/")
        try:
            if type(filepath) is tuple:
                label2.place(x=250, y=150)
                label.config(text="Unsuccessful :(")
                window.after(4000,setTextBack)
            else:
                path = pathlib.Path(filepath)
                newname = pathlib.Path(path.parent, path.name)
                path.rename(newname)
                print(os.path.dirname(filepath))
                os.system('libreoffice --headless --convert-to pdf '+str(path)+' --outdir '+os.path.dirname(filepath))
                label1.place(x=250, y=150)
                label.config(text="Successful!")
                label3.config(text="You can find your converted file at "+filepath[:-4]+".pdf")
                window.after(4000,setTextBack)
        except Exception as e:
            print(e)
            label2.place(x=250, y=150)
            label.config(text="Unsuccessful :(")
            window.after(4000,setTextBack)
        
#---------------------------------------
#shows Graphical User Interface for user
#---------------------------------------
window = Tk()
window.geometry("800x500")
window.title("File Converter")

#Title text
label = Label(window, text="Welcome to File Converter", font=('Arial',18))
label.pack(pady=20)


# "Convert to JPG" and "Convert to PDF" Buttons
buttonFrame = Frame(window)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
jpgButton = Button(buttonFrame, text="Convert to JPG",font=('Arial',16),activebackground='gray', bg='#D3D3D3',highlightbackground='black', command = convert_to_jpg)
jpgButton.grid(row=0,column=0, sticky=W+E)
pdfButton = Button(buttonFrame, text="Convert to PDF",font=('Arial',16), activebackground='gray', bg='#D3D3D3', highlightbackground='black', command = convert_to_pdf)
pdfButton.grid(row = 0, column = 1, sticky=W+E)
buttonFrame.pack(fill='x')

# Visual cues for user (checkmark and x-mark)
image1 = PIL.Image.open("checkmark-png-5.png")
check = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=check)
label1.image = check

image2 = PIL.Image.open("x-png-15.png")
xMark = ImageTk.PhotoImage(image2)
label2 = tkinter.Label(image=xMark)
label2.image = xMark

label3 = tkinter.Label(window, text = "What would you like to do?", font = ('Arial',16))
label3.pack(side = BOTTOM, pady = 20)
#Application Title and Icon
window.title("File Converter")
icon = ImageTk.PhotoImage(PIL.Image.open("icon.png"))
window.iconphoto(False, icon)

# Displays the GUI with its elements
window.mainloop()



