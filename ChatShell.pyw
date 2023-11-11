import os
import random
import webbrowser
import threading
try:
    import keyboard
    import customtkinter
except:
    os.system("pip install customtkinter keyboard")


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")
colorback = "#F2F2F2"
color1 = "#2CC985"
color2 = "#0C955A"
app = customtkinter.CTk()
app.geometry("310x40")
app.title('ChatShell')
app.attributes("-topmost", True)
app.attributes("-toolwindow", True)
#app.overrideredirect(True)
app.resizable(width = False, height = False)
app.winfo_x = 0

def send():
    com = message_entry.get().lower()
    message_entry.delete(0, 'end')
    # Встроеные приложения
    if "текстов" in com.lower() and "редакт" in com.lower() or "блокнот" in com.lower():
        os.startfile("ChatShell_notepad.pyw")

    if "калькул" in com.lower():
        os.startfile("ChatShell_calculator.pyw")
    # Сайты
    if "яндекс" in com.lower() and "музык" in com.lower():
        webbrowser.open("https://music.yandex.ru/home")

    if "яндекс" in com.lower() and "почт" in com.lower():
        webbrowser.open("https://mail.yandex.ru/")

    if "яндекс" in com.lower() and "диск" in com.lower():
        webbrowser.open("https://disk.yandex.ru/")

    if "яндекс" in com.lower() and "карт" in com.lower():
        webbrowser.open("https://yandex.ru/maps/")

    if "яндекс" in com.lower() and "такс" in com.lower():
        webbrowser.open("https://taxi.yandex.ru/")

    if "яндекс" in com.lower() and "браузер" in com.lower():
        webbrowser.open("https://ya.ru/")

    if "контакте" in com.lower() and "музык" not in com.lower() and "погод" not in com.lower() and "сообщен" not in com.lower() and "сообществ" not in com.lower() and "звонк" not in com.lower() and "друз" not in com.lower() and "фото" not in com.lower() and "видео" not in com.lower():
        webbrowser.open("https://m.vk.com")

    if "контакте" in com.lower() and "погод" in com.lower():
        webbrowser.open("https://vk.com/weather?ref=catalog_recent")

    if "контакте" in com.lower() and "сообщен" in com.lower():
        webbrowser.open("https://m.vk.com/mail")

    if "контакте" in com.lower() and "звонк" in com.lower():
        webbrowser.open("https://vk.com/calls")

    if "контакте" in com.lower() and "друз" in com.lower():
        webbrowser.open("https://vk.com/friends")

    if "контакте" in com.lower() and "сообществ" in com.lower():
        webbrowser.open("https://vk.com/groups")

    if "контакте" in com.lower() and "фото" in com.lower():
        webbrowser.open("https://m.vk.com/albums")

    if "контакте" in com.lower() and "видео" in com.lower():
        webbrowser.open("https://m.vk.com/video")

    if "контакте" in com.lower() and "музык" in com.lower():
        webbrowser.open("https://m.vk.com/audio")

    elif "видео" not in com.lower() and "музык" not in com.lower() and "песн" not in com.lower() and "найди" in com.lower() or "видео" not in com.lower() and "музык" not in com.lower() and "песн" not in com.lower() and "поищи" in com.lower() or "видео" not in com.lower() and "музык" not in com.lower() and "песн" not in com.lower() and "за гугле" in com.lower() or "видео" not in com.lower() and "музык" not in com.lower() and "песн" not in com.lower() and "как" in com.lower() or "видео" not in com.lower() and "музык" not in com.lower() and "песн" not in com.lower() and "кто" in com.lower() or "видео" not in com.lower() and "музык" not in com.lower() and "песн" not in com.lower() and "умеешь" not in com.lower() and "что" in com.lower() or "видео" not in com.lower() and "музык" not in com.lower() and "песн" not in com.lower() and "времен" not in com.lower() and "сколько" in com.lower() or "видео" not in com.lower() and "музык" not in com.lower() and "песн" not in com.lower() and "где" in com.lower() or "видео" not in com.lower() and "музык" not in com.lower() and "песн" not in com.lower() and "чем" in com.lower() or "видео" not in com.lower() and "музык" not in com.lower() and "песн" not in com.lower() and "когда" in com.lower():
        zapros = com.lower()
        zapros = zapros.lower().replace("найди ", "")
        zapros = zapros.lower().replace("поищи ", "")
        zapros = zapros.lower().replace("за гугле ", "")
        webbrowser.open("https://www.google.com/search?q=" + zapros)

    # Поиск видео
    elif "видео" in com.lower():
        zapros = com.lower()
        zapros = zapros.lower().replace("найди ", "")
        zapros = zapros.lower().replace("поищи ", "")
        zapros = zapros.lower().replace("включи ", "")
        zapros = zapros.lower().replace("ключи ", "")
        zapros = zapros.lower().replace("включить ", "")
        zapros = zapros.lower().replace("включил ", "")
        zapros = zapros.lower().replace("видео ", "")
        webbrowser.open("https://www.youtube.com/results?search_query=" + zapros)



    # Поиск музыки
    elif "яндекс" not in com.lower() and "контакте" not in com.lower() and "музык" in com.lower() or "яндекс" not in com.lower() and "контакте" not in com.lower() and "песн" in com.lower():
        zapros = com.lower()
        zapros = zapros.lower().replace("найди ", "")
        zapros = zapros.lower().replace("поищи ", "")
        zapros = zapros.lower().replace("включи ", "")
        zapros = zapros.lower().replace("ключи ", "")
        zapros = zapros.lower().replace("включить ", "")
        zapros = zapros.lower().replace("включил ", "")
        zapros = zapros.lower().replace("музыка ", "")
        zapros = zapros.lower().replace("музыку ", "")
        zapros = zapros.lower().replace("песня ", "")
        zapros = zapros.lower().replace("песню ", "")
        webbrowser.open("https://music.yandex.ru/search?text=" + zapros)

    elif com == "exit":
        quit()

def wait_for_enter():
    while True:
        keyboard.wait("enter")
        send()

enter_th = threading.Thread(target=wait_for_enter, daemon=True)
enter_th.start()



message_entry = customtkinter.CTkEntry(master=app, width=195, placeholder_text='Введите сообщение:', border_color=color1)
message_entry.place(relx=0.05, rely=0.5, anchor=customtkinter.W)

button_send = customtkinter.CTkButton(master=app, width=80, text='Отправить', command=send)
button_send.place(relx=0.95, rely=0.5, anchor=customtkinter.E)

app.mainloop()
