from tkinter import *
main = Tk()
main.title('Калькулятор by Phoenix')
lf4 = Label(main,text = 'Cоздатель : Phoenix')  
lf5 = Label(main,text = 'Telegram: @phoenix_wb')
l1 = Label(main, text = 'Ответ тут ', height= 2, width = 30,bg='silver')
b1 = Button(main,text = '+', height= 5, width = 10, bg='gold')
b2 = Button(main,text = '-', height= 5, width = 10, bg='pink') 
b3 = Button(main,text = ' * ', height= 5, width = 10, bg='red')
b4 = Button(main,text = '/', height= 5, width = 10, bg='green')
b5= Button(main,text = 'Перевод', height= 5, width = 10, bg='grey')
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
b = ''
def ButtonFunc5():
    global b
    text1 = e1.get()
    text2 = e2.get()
    while int(text1)> 1:
        if int(text1) % 2 == 0:
            b = b +'0'
            print(b)
            l1['text'] = b
        if int(text1) % 2 <= 1:
            b = b + '1'
            print(b)
            return
            l1['text'] = b

    l1['text'] = b
b5['command'] = ButtonFunc5
lf4.pack()
lf5.pack()
e1.pack()
e2.pack()
l1.pack(side=BOTTOM)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=RIGHT)
b4.pack(side=RIGHT)
b5.pack(side=TOP)
main.mainloop()