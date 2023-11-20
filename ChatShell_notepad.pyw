try:
    import os
    import customtkinter
except ImportError:
    print("Не все библиотеки установлены.")
    os.system("pip install customtkinter")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")
colorback = "#F2F2F2"
color1 = "#2CC985"
color2 = "#0C955A"

app = customtkinter.CTk()
app.geometry("850x550")
app.title('Блокнот')
app.resizable(width=False, height=False)

def save():
    code = code_box.get("0.0", customtkinter.END)
    path = entry_path.get()

    file = open(path, encoding="utf!8", mode="w+")
    file.write(code)
    file.close()

def open_file():
    path = entry_path.get()

    file = open(path, encoding='utf!8', mode='r')
    code = file.read()
    code_box.insert("0.0", code)
    file.close()



tabview = customtkinter.CTkTabview(master=app, fg_color=colorback, segmented_button_selected_hover_color=color1, segmented_button_selected_color=color1, segmented_button_unselected_hover_color=color2, width=900, height=900)
tabview.place(relx=0.5, rely=0.82, anchor=customtkinter.CENTER)

tabview.add("Редактор")
tabview.add("Файл")

code_box = customtkinter.CTkTextbox(tabview.tab("Редактор"), width=800, height=470, border_color=color1, border_width=3)
code_box.place(relx=0.5, rely=0.29, anchor=customtkinter.CENTER)

label_path = customtkinter.CTkLabel(tabview.tab("Файл"), text="Путь к файлу: ", bg_color=colorback, font=("TkHeadingFont", 15.1))
label_path.place(relx=0.05, rely=0.05, anchor=customtkinter.W)

entry_path = customtkinter.CTkEntry(tabview.tab("Файл"), border_color=color1, width=260, placeholder_text=r"Например, C:\Users\Daniel\Documents\test.txt")
entry_path.place(relx=0.95, rely=0.05, anchor=customtkinter.E)

button_save = customtkinter.CTkButton(tabview.tab("Файл"), text="Сохранить", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 15), width=200, command=save)
button_save.place(relx=0.1, rely=0.55, anchor=customtkinter.W)

button_open = customtkinter.CTkButton(tabview.tab("Файл"), text="Открыть", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 15), width=200, command=open_file)
button_open.place(relx=0.9, rely=0.55, anchor=customtkinter.E)

app.mainloop()