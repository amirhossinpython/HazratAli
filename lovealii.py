import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
import pygame



pygame.mixer.init()


def play_audio():
    pygame.mixer.music.load("Rasooli - Ali 6.mp3")
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()


def show_condolence():  
    
    condolence_message = (  
        "تسلیت به مناسبت شهادت مولا علی (ع)\n"  
        "بوی سجاده و خون می‌آید، ای عاشقانت علی!\n"  
        "ضربت خنجر غداران، شهادت را برایت رقم زد.\n\n"  
        
        "علی، ای همای رحمت، تو چه آیتی از خدا هستی\n"  
        "که همه سایه‌ها در برابر نور تو محوند. \n"  
        "دل اگر خداشناسی، به رخسار تو بنگر\n"  
        "من علی را شناختم، به خدا قسم، خدا را.\n\n"  
        
        "لعنت بر دشمنان علی (ع) و خاندان پیامبر (ص)"  
    )  
    
    messagebox.showinfo("تسلیت", condolence_message)  


def change_image():
    global current_image_index, photo
    current_image_index = (current_image_index + 1) % len(images)
    image = Image.open(images[current_image_index])
    image = image.resize((400, 400), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    root.after(4000, change_image)  


root = tk.Tk()
root.title("ضربت و شهادت")
root.geometry("1000x700")
root.configure(bg="#2c3e50")  


title_font = font.Font(family="B Nazanin", size=24, weight="bold")
text_font = font.Font(family="B Nazanin", size=16)
button_font = font.Font(family="B Nazanin", size=14)


images = ["IMG_20250320_003947_859.jpg", "IMG_20250320_003948_067.jpg", "ax-neveshteh-zarbat-khordan-imam-ali-1400-07.jpg", "IMG_20250320_003947_819.jpg"]
current_image_index = 0


image = Image.open(images[current_image_index])
image = image.resize((400, 400), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo, bg="#2c3e50")
image_label.pack(pady=20)


title_label = tk.Label(
    root,
    text="ضربت و شهادت",
    font=title_font,
    fg="#e74c3c",
    bg="#2c3e50"
)
title_label.pack(pady=10)


subtitle_label = tk.Label(
    root,
    text="بوی سجاده و خون می‌آید، ای عاشقانت علی!",
    font=text_font,
    fg="#ecf0f1",
    bg="#2c3e50"
)
subtitle_label.pack(pady=10)


condolence_button = tk.Button(
    root,
    text="تسلیت",
    command=show_condolence,
    font=button_font,
    bg="#3498db",
    fg="#ffffff",
    padx=20,
    pady=10,
    borderwidth=0
)
condolence_button.pack(pady=10)


play_button = tk.Button(
    root,
    text="شروع مداحی",
    command=play_audio,
    font=button_font,
    bg="#27ae60",
    fg="#ffffff",
    padx=20,
    pady=10,
    borderwidth=0
)
play_button.pack(pady=10)


stop_button = tk.Button(
    root,
    text="قطع مداحی",
    command=stop_audio,
    font=button_font,
    bg="#e74c3c",
    fg="#ffffff",
    padx=20,
    pady=10,
    borderwidth=0
)
stop_button.pack(pady=10)


root.after(4000, change_image)  


root.mainloop()