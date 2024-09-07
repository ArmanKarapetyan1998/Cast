from  tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window=Tk()
window.title('Cats')
window.geometry('600x480')
label=Label()
label.pack()

url='https://dog.ceo/dog-api/'
img=load_image(url)

if img:
    label.config(image=img)
    label.image=img
window.mainloop()
