from  tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        image_data=BytesIO(response.content)
        img=Image.open(image_data)
        img.thumbnail((600,480),Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Ошибка- {e}!')
        return None

def open_new_window():
    tag=tag_entry.get()
    url_tag=f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)
    if img:
        new_window=Toplevel()
        new_window.title('Картинки с котиками')
        new_window.geometry('600x480')
        label = Label(new_window,image=img)
        label.pack()
        label.image = img

window=Tk()
mainmenu=Menu(window)
window.config(menu=mainmenu)
filemenu=Menu(mainmenu,tearoff=0)
filemenu.add_command(label='Загрузить изображение',command=open_new_window)
mainmenu.add_cascade(label='Файл',menu=filemenu)
tag_entry=Entry()
tag_entry.pack()
load_button=Button(text='Загрузить по тегу',command=open_new_window)
load_button.pack()


window.title('Cats')
window.geometry('600x520')

#update_button=Button(text='Обновить',command=set_image)
#update_button.pack()


url='https://cataas.com/cat'
#open_new_window()
window.mainloop()
