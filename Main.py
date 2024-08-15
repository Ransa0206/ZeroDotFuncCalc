import math
import customtkinter as ctk

def calculate_sens():
    try:
        try:      
            x = float(entry_x.get())
            y = float(entry_y.get())
            z = float(entry_z.get())

            global sens1, sens2, sens3, sens4, sens5
            sens1 = (x ** 0.25) * (1 - (((math.log(y,10)) / y) - (x / 100000))) * ((math.log(z,10))**0.5) * 5
            sens2 = (x ** 0.25) * (1 - (((math.log(x,10)) / y) - (x / 100000))) * ((math.log(z,10))**0.5) * 5
            sens3 = (x ** 0.25) * (1 - ((y ** 0.5) / y) + (x / 100000)) * ((math.log10(z))**0.5) * 5
            sens4 = (x ** 0.25) * (1 - (((math.log(y,10)) / y**0.5) - (x / 100000))) * ((math.log(z,10))**0.5) * 5 
            sens5 = (x ** 0.25) * (1 - (((math.log(x,10)) / y**0.5) - (x / 100000))) * ((math.log(z,10))**0.5) * 5
            slider.configure(command=slider_sens_change, from_=1, to=5, number_of_steps=4)
            label_result.configure(text=f"Sens: {sens3:.4f}cm/360°\n<-彈性小  |   彈性大->")
            slider.set(3)
        except:
            x = float(entry_x.get())
            z = float(entry_z.get())
            easyModeSens = (x ** 0.25) *  ((math.log10(z))**0.5) * 5
            slider.configure(from_=0, to=0, number_of_steps=0)
            label_result.configure(text=f"Sens: {easyModeSens:.4f}cm/360°\n - - - - ->無法調節<- - - - - ")
    except ValueError:
        label_result.configure(text="Please enter valid numbers.")

def slider_sens_change(value):
    try:
        if value == 1:
            label_result.configure(text=f"Sens: {sens1:.4f}cm/360°\n<-彈性小  |   彈性大->")
        elif value == 2:
            label_result.configure(text=f"Sens: {sens2:.4f}cm/360°\n<-彈性小  |   彈性大->")
        elif value == 3:
            label_result.configure(text=f"Sens: {sens3:.4f}cm/360°\n<-彈性小  |   彈性大->")
        elif value == 4:
            label_result.configure(text=f"Sens: {sens4:.4f}cm/360°\n<-彈性小  |   彈性大->")ˊ
        elif value == 5:
            label_result.configure(text=f"Sens: {sens5:.4f}cm/360°\n<-彈性小  |   彈性大->")
    except ValueError:
        label_result.configure(text="Please enter x, y, z.")

def xyzGet():
    global x,y,z

    calculate_sens()

# 初始化畫面
app = ctk.CTk()
app.title("ZeroDotFunc Sens Calculator")
app.geometry("320x500")
app.resizable(0, 0)

# X, Y, Z輸入框
label_x = ctk.CTkLabel(app, text="X Value:")
label_x.pack(pady=10)
entry_x = ctk.CTkEntry(app)
entry_x.pack(pady=10)

label_y = ctk.CTkLabel(app, text="Y Value:")
label_y.pack(pady=10)
entry_y = ctk.CTkEntry(app)
entry_y.pack(pady=10)

label_z = ctk.CTkLabel(app, text="Z Value:")
label_z.pack(pady=10)
entry_z = ctk.CTkEntry(app)
entry_z.pack(pady=10)

# 計算按鈕
button_calculate = ctk.CTkButton(app, text="Calculate Sens", command=xyzGet)
button_calculate.pack(pady=20)

# 滑桿
slider = ctk.CTkSlider(app, command=slider_sens_change, from_=1, to=5, number_of_steps=4)
slider.pack(pady=10)

label_result = ctk.CTkLabel(app, text="")
label_result.pack(pady=10)

label_credit = ctk.CTkLabel(app, text="Func Design By: B站西島海 | Dev By: Ransa")
label_credit.pack(pady=10)

# 執行
app.mainloop()
