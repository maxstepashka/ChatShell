# загрузка библиотек
try:
    import os
    import customtkinter
except ImportError:
    print("Не все библиотеки установлены.")
    os.system("pip install customtkinter")



# конфигурация интерфейса
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")
colorback = "#F2F2F2"
color1 = "#2CC985"
color2 = "#0C955A"
customtkinter.set_default_color_theme("dark-blue")
app = customtkinter.CTk()
app.geometry("250x330")
app.title('Калькулятор')
app.resizable(width=False, height=False)



vir = ""
vir_label = customtkinter.StringVar()



# функции кнопок
def seven():
    global vir
    vir = vir + "7"
    vir_label.set(vir)

def eight():
    global vir
    vir = vir + "8"
    vir_label.set(vir)

def nine():
    global vir
    vir = vir + "9"
    vir_label.set(vir)

def four():
    global vir
    vir = vir + "4"
    vir_label.set(vir)

def five():
    global vir
    vir = vir + "5"
    vir_label.set(vir)

def six():
    global vir
    vir = vir + "6"
    vir_label.set(vir)

def one():
    global vir
    vir = vir + "1"
    vir_label.set(vir)

def two():
    global vir
    vir = vir + "2"
    vir_label.set(vir)

def three():
    global vir
    vir = vir + "3"
    vir_label.set(vir)

def zero():
    global vir
    vir = vir + "0"
    vir_label.set(vir)

def point():
    global vir
    vir = vir + "."
    vir_label.set(vir)

def ac():
    global vir
    vir = ""
    vir_label.set(vir)


def plus():
    global vir
    vir = vir + "+"
    vir_label.set(vir)

def minus():
    global vir
    vir = vir + "-"
    vir_label.set(vir)

def umn():
    global vir
    vir = vir + "*"
    vir_label.set(vir)
def delenie():
    global vir
    vir = vir + "/"
    vir_label.set(vir)
def evaluate_vir():
    global vir
    vir = str(eval(vir))
    vir_label.set(vir)



# отрисовака интерфейса
label = customtkinter.CTkLabel(master=app, textvariable=vir_label, bg_color=colorback, font=("TkHeadingFont", 15.1))
label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

button_7 = customtkinter.CTkButton(master=app, text="7", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=seven)
button_7.place(relx=0.2, rely=0.25, anchor=customtkinter.CENTER)

button_8 = customtkinter.CTkButton(master=app, text="8", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=eight)
button_8.place(relx=0.4, rely=0.25, anchor=customtkinter.CENTER)

button_9 = customtkinter.CTkButton(master=app, text="9", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=nine)
button_9.place(relx=0.6, rely=0.25, anchor=customtkinter.CENTER)

button_plus = customtkinter.CTkButton(master=app, text="+", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=plus)
button_plus.place(relx=0.8, rely=0.25, anchor=customtkinter.CENTER)

button_4 = customtkinter.CTkButton(master=app, text="4", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=four)
button_4.place(relx=0.2, rely=0.41, anchor=customtkinter.CENTER)

button_5 = customtkinter.CTkButton(master=app, text="5", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=five)
button_5.place(relx=0.4, rely=0.41, anchor=customtkinter.CENTER)

button_6 = customtkinter.CTkButton(master=app, text="6", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=six)
button_6.place(relx=0.6, rely=0.41, anchor=customtkinter.CENTER)

button_minus = customtkinter.CTkButton(master=app, text="-", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=minus)
button_minus.place(relx=0.8, rely=0.41, anchor=customtkinter.CENTER)

button_1 = customtkinter.CTkButton(master=app, text="1", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=one)
button_1.place(relx=0.2, rely=0.57, anchor=customtkinter.CENTER)

button_2 = customtkinter.CTkButton(master=app, text="2", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=two)
button_2.place(relx=0.4, rely=0.57, anchor=customtkinter.CENTER)

button_3 = customtkinter.CTkButton(master=app, text="3", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=three)
button_3.place(relx=0.6, rely=0.57, anchor=customtkinter.CENTER)

button_umn = customtkinter.CTkButton(master=app, text="*", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=umn)
button_umn.place(relx=0.8, rely=0.57, anchor=customtkinter.CENTER)

button_ac = customtkinter.CTkButton(master=app, text="AC", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=ac)
button_ac.place(relx=0.2, rely=0.73, anchor=customtkinter.CENTER)

button_0 = customtkinter.CTkButton(master=app, text="0", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=zero)
button_0.place(relx=0.4, rely=0.73, anchor=customtkinter.CENTER)

button_point = customtkinter.CTkButton(master=app, text=".", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=point)
button_point.place(relx=0.6, rely=0.73, anchor=customtkinter.CENTER)

button_del = customtkinter.CTkButton(master=app, text="/", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=40, height=40, command=delenie)
button_del.place(relx=0.8, rely=0.73, anchor=customtkinter.CENTER)

button_eval = customtkinter.CTkButton(master=app, text="=", fg_color=color1, hover_color=color2, font=("TkHeadingFont", 18), width=190, height=40, command=evaluate_vir)
button_eval.place(relx=0.5, rely=0.89, anchor=customtkinter.CENTER)

app.mainloop()