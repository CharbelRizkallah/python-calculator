from tkinter import *

root = Tk()
root.title("CALCULATOR")

btnh = 5
btnw = 10
inn = ""
answer = Label(root,text="",height= 5,width=45)
answer.grid(columnspan = 4)

def seven():
    global inn 
    inn = inn + "7"
    global answer
    answer.config(text= inn)

btn7 = Button(root,text="7",height = btnh , width = btnw, command = seven, fg = "white" , bg= "black")
btn7.grid(row=1,column=0)

def eight():
    global inn 
    inn = inn + "8"
    global answer
    answer.config(text= inn)

btn8 = Button(root,text="8",height = btnh , width = btnw,command = eight, fg = "white" , bg= "black")
btn8.grid(row=1,column=1)

def nine():
    global inn 
    inn = inn + "9"
    global answer
    answer.config(text= inn)

btn9 = Button(root,text="9",height = btnh , width = btnw,command = nine, fg = "white" , bg= "black")
btn9.grid(row=1,column=2)

def division():
    global inn 
    inn = inn + "/"
    global answer
    answer.config(text= inn)

btndiv = Button(root,text="/",height = btnh , width = btnw,command = division, fg = "white" , bg= "black")
btndiv.grid(row=1,column=3)


def four():
    global inn 
    inn = inn + "4"
    global answer
    answer.config(text= inn)

btn4 = Button(root,text="4",height = btnh , width = btnw,command = four, fg = "white" , bg= "black")
btn4.grid(row=2,column=0)


def five():
    global inn 
    inn = inn + "5"
    global answer
    answer.config(text= inn)

btn5 = Button(root,text="5",height = btnh , width = btnw,command = five, fg = "white" , bg= "black")
btn5.grid(row=2,column=1)


def six():
    global inn 
    inn = inn + "6"
    global answer
    answer.config(text= inn)

btn6 = Button(root,text="6",height = btnh , width = btnw,command = six, fg = "white" , bg= "black")
btn6.grid(row=2,column=2)


def multiply():
    global inn 
    inn = inn + "*"
    global answer
    answer.config(text= inn)

btnmul = Button(root,text="X",height = btnh , width = btnw,command = multiply, fg = "white" , bg= "black")
btnmul.grid(row=2,column=3)


def one():
    global inn 
    inn = inn + "1"
    global answer
    answer.config(text= inn)

btn1 = Button(root,text="1",height = btnh , width = btnw,command = one, fg = "white" , bg= "black")
btn1.grid(row=3,column=0)


def two():
    global inn 
    inn = inn + "2"
    global answer
    answer.config(text= inn)

btn2 = Button(root,text="2",height = btnh , width = btnw,command = two, fg = "white" , bg= "black")
btn2.grid(row=3,column=1)


def three():
    global inn 
    inn = inn + "3"
    global answer
    answer.config(text= inn)

btn3 = Button(root,text="3",height = btnh , width = btnw,command = three, fg = "white" , bg= "black")
btn3.grid(row=3,column=2)


def minus():
    global inn 
    inn = inn + "-"
    global answer
    answer.config(text= inn)

btnmin = Button(root,text="-",height = btnh , width = btnw,command = minus, fg = "white" , bg= "black")
btnmin.grid(row=3,column=3)


def zero():
    global inn 
    inn = inn + "0"
    global answer
    answer.config(text= inn)

btn0 = Button(root,text="0",height = btnh , width = btnw,command = zero, fg = "white" , bg= "black")
btn0.grid(row=4,column=1)


def plus():
    global inn 
    inn = inn + "+"
    global answer
    answer.config(text= inn)

btnplus = Button(root,text="+",height = btnh , width = btnw,command = plus, fg = "white" , bg= "black")
btnplus.grid(row=4,column=3)


def equal():
    global inn 
    global answer
    ann = ""
    if inn[0] == "0":
        for i in inn:
            if i == "0":
                continue
            ann = ann + i
    else:
        ann = inn
    answer.config(text=str(eval(ann)))

btnequal = Button(root,text="=",height = btnh , width = btnw,command = equal, fg = "white" , bg= "black")
btnequal.grid(row=4,column=2)


def clear():
    global inn 
    inn = ""
    global answer
    answer.config(text=inn)

btnclr = Button(root,text="clear",height = btnh , width = btnw,command = clear, fg = "white" , bg= "black")
btnclr.grid(row=4,column=0)

root.mainloop()