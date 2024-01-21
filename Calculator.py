from tkinter import *
main = Tk()
main.title('Калькулятор by Phoenix')
lf4 = Label(main,text = 'Cоздатель : Phoenix')  
lf5 = Label(main,text = 'VK : official.sasha')
l1 = Label(main, text = 'Ответ тут ', height= 2, width = 30,bg='silver')
b1 = Button(main,text = '+', height= 5, width = 10, bg='gold')
b2 = Button(main,text = '-', height= 5, width = 10, bg='pink') 
b3 = Button(main,text = ' * ', height= 5, width = 10, bg='red')
b4 = Button(main,text = '/', height= 5, width = 10, bg='green')
b5= Button(main,text = 'Перевод в Двоичную', height= 5, width = 20, bg='grey')
b6= Button(main,text = 'Перевод в Троичную', height= 5, width = 20, bg='grey')
b7= Button(main,text = 'Перевод в Восьмеричную', height= 5, width = 20, bg='grey')
b8= Button(main,text = 'Перевод в Шестнадцатиричную', height= 5, width = 20, bg='grey')

e1 = Entry(main)
e2 = Entry(main)
def ButtonFunc1():
    text1 = e1.get()
    text2 = e2.get()
    res = int(text1)+int(text2)
    l1['text'] = res
b1['command'] = ButtonFunc1
def ButtonFunc2():
    text1 = e1.get()
    text2 = e2.get()
    ttt = int(text1)-int(text2)
    l1['text'] = ttt
b2['command'] = ButtonFunc2
def ButtonFunc3():
    text1 = e1.get()
    text2 = e2.get()
    gip = int(text1)*int(text2)
    l1['text'] = gip
b3['command'] = ButtonFunc3

def ButtonFunc4():
    text1 = e1.get()
    text2 = e2.get()
    jor = int(text1)/int(text2)
    l1['text'] = jor
b4['command'] = ButtonFunc4
def ButtonFunc5():
    global b
    text1 = e1.get()
    text2 = e2.get()
    decimal_num1 = int(text1)
    binary_num = bin(decimal_num1)[2:]
    l1['text'] = binary_num
b5['command'] = ButtonFunc5

def ButtonFunc6():
    text1 = e1.get()
    decimal_num =  int(text1)
    ternary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 3
        decimal_num = decimal_num // 3
        ternary_num = str(remainder) + ternary_num
    l1['text'] = ternary_num
b6['command'] = ButtonFunc6


def ButtonFunc7():
    text1 = e1.get()
    decimal_num =  int(text1)
    ternary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 8
        decimal_num = decimal_num // 8
        ternary_num = str(remainder) + ternary_num
    l1['text'] = ternary_num
b7['command'] = ButtonFunc7


def ButtonFunc8():
    text1 = e1.get()
    decimal_num =  int(text1)
    hex_num = hex(decimal_num)[2:].upper() 
    l1['text'] = hex_num
b8['command'] = ButtonFunc8


lf4.pack()
lf5.pack()
e1.pack()
e2.pack()
l1.pack(side=BOTTOM)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=RIGHT)
b4.pack(side=RIGHT)
b5.pack(side=RIGHT)
b6.pack(side=LEFT)
b7.pack(side=RIGHT)
b8.pack(side=LEFT)
main.mainloop()