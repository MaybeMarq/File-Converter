import PIL
from PIL import Image, ImageTk
import tkinter
from tkinter import *
from tkinter import filedialog
from docx2pdf import convert
from pillow_heif import register_heif_opener


# opens file dialog to allow user to choose the file they want to convert and saves a copy as a...
# JPEG in the same directory
def convert_to_jpg():
    register_heif_opener()
    filepath = filedialog.askopenfilename()
    try:
        img = PIL.Image.open(""+filepath)
        newImg = img.convert('RGB')
        newImg.save(filepath[:-4]+" JPEG.jpg") 
        label1.place(x=250, y=150)
    except:
        label2.place(x=250, y=150)

# opens file dialog to allow user to choose the .docx file they want to convert and saves a copy...
# as a .pdf file in the same directory
def convert_to_pdf():
    filepath = filedialog.askopenfilename()
    try:
        convert(filepath)
        label1.place(x=250, y=150)
    except:
        label2.place(x=250, y=150)
    
#---------------------------------------
#shows Graphical User Interface for user
#---------------------------------------
window = Tk()
window.geometry("800x500")
window.title("File Convertor")

#Title
label = Label(window, text="Welcome to File Convertor", font=('Arial',18))
label.pack(pady=20)

#Buttons
buttonFrame = Frame(window)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
jpgButton = Button(buttonFrame, text="Convert to JPG",font=('Arial',16),activebackground='red', bg='#D3D3D3',highlightbackground='red', command = convert_to_jpg)
jpgButton.grid(row=0,column=0, sticky=W+E)
pdfButton = Button(buttonFrame, text="Convert to PDF",font=('Arial',16), activebackground='red', bg='#D3D3D3', highlightbackground='red', command = convert_to_pdf)
pdfButton.grid(row = 0, column = 1, sticky=W+E)
buttonFrame.pack(fill='x')

#Visual cues for user (checkmark and x-mark)
image1 = PIL.Image.open("checkmark-png-5.png")
check = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=check)
label1.image = check

image2 = PIL.Image.open("x-png-15.png")
xMark = ImageTk.PhotoImage(image1)
label2 = tkinter.Label(image=xMark)
label2.image = xMark

window.mainloop()



