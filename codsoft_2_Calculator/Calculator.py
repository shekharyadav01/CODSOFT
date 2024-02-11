import tkinter as tk
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("320x350")
root.resizable(0,0)
root.configure(bg="#000807")


result_var = tk.StringVar()

def button_click(button):
    global result_var
    if button == "=":
        try:
            result_var.set(eval(result_var.get()))
        except:
            result_var.set("Error")
    elif button == "C":
        result_var.set("")
    else:
        result_var.set(result_var.get() + button)

result = Label(root, textvariable=result_var,width=25,height=2,font=("Helvetica", 20))
result.pack()

b_c = Button(root,text="C",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command=lambda: button_click("C"))
b_c.place(x=10,y=100)
b_mul = Button(root,text="X",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command=lambda: button_click("*"))
b_mul.place(x=90,y=100)
b_div = Button(root,text="/",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command=lambda: button_click("/"))
b_div.place(x=170,y=100)
b_sub = Button(root,text="-",width=8,height=2,fg = "#FFFFFF",bg="#26573E",bd = 0,command=lambda: button_click("-"))
b_sub.place(x=250,y=100)

b7 = Button(root,text="7",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command=lambda: button_click("7"))
b7.place(x=10,y=150)
b8 = Button(root,text="8",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command = lambda:button_click("8"))
b8.place(x=90,y=150)
b9 = Button(root,text="9",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command = lambda:button_click("9"))
b9.place(x=170,y=150)
b_add = Button(root,text="+",width=8,height=2,fg = "#FFFFFF",bg="#26573E",bd = 0,command = lambda:button_click("+"))
b_add.place(x=250,y=150)

b4 = Button(root,text="4",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command = lambda:button_click("4"))
b4.place(x=10,y=200)
b5 = Button(root,text="5",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command = lambda:button_click("5"))
b5.place(x=90,y=200)
b6 = Button(root,text="6",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command = lambda:button_click("6"))
b6.place(x=170,y=200)
b_eq = Button(root,text="=",width=8,height=9,fg = "#FFFFFF",bg="#26573E",bd = 0,command = lambda:button_click("="))
b_eq.place(x=250,y=200)

b1 = Button(root,text="1",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command = lambda:button_click("1"))
b1.place(x=10,y=250)
b2 = Button(root,text="2",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command = lambda:button_click("2"))
b2.place(x=90,y=250)
b3 = Button(root,text="3",width=8,height=2,fg = "#FFFFFF",bg="#000807",bd = 0,command = lambda:button_click("3"))
b3.place(x=170,y=250)

b0 = Button(root,text="0",width=20,height=2,fg = "#FFFFFF",bg="#26573E",bd = 0,command = lambda:button_click("0"))
b0.place(x=10,y=300)
b_dec = Button(root,text=".",width=8,height=2,fg = "#FFFFFF",bg="#26573E",bd = 0,command = lambda:button_click("."))
b_dec.place(x=170,y=300)



root.mainloop()
