from tkinter import *
from PIL import Image, ImageTk
from time import strftime

current_method = None

def time1():
    string = strftime('   %H:%M:%S')
    label.config(text=string)
    label.after(1000, time1)

def time():
    string = strftime('%I:%m:%S %p')
    label.config(text=string)
    label.after(1000, time)



def switch_method(method):
    global current_method
    current_method = method

root = Tk()
root.title("Digital Clock")
root.geometry("563x375")
root.resizable(False, False)

background_image = Image.open("CLOCK.jpg")
background_photo = ImageTk.PhotoImage(background_image)

canvas = Canvas(root, width=563, height=375)
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=background_photo)

fr1 = Frame(root, bg="black", bd=0)
fr1.place(x=40, y=110, width="150", height=100)
fr2 = Frame(root, bg="black", bd=0)  
fr2.place(x=40, y=38, width="290", height=80)

label = Label(fr2, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.place(x=0, y=5)

b1 = Button(fr1, text='12H', font="stencil", fg="black", bd=1, bg="white" , relief=SOLID, cursor='hand2', command=lambda: switch_method(time))
b1.place(x=5, y=10, width=60)

b2 = Button(fr1, text='24H', font="stencil", fg="black", bd=1, bg="white" , relief=SOLID, cursor='hand2', command=lambda: switch_method(time1))
b2.place(x=75, y=10, width=60)



def update_clock():
    if current_method:
        current_method()
    root.after(1000, update_clock)

update_clock()

root.mainloop()
