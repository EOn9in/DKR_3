from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def function(x):
  f = x**3 + x**2 + 5*x + 3
  return f
def pervoobraznaya(x):
  per = (x**4)/4 + (x**3)/3 + 2.5*x**2 + 3*x
  return per

def integrel():
    a = int(aa.get())
    b = int(bb.get())
    n = int(nn.get())
    h=(b-a)/n
    s=(function(a)+function(b))/2
    x = a + h
    for i in range(n-1):
        s+=function(x)
        x+=h
    s*=h
    p = pervoobraznaya(b)-pervoobraznaya(a)
    messagebox.showinfo('Результат', f'Приближённое значение (м-д трапеций) ≈ {s}',
                        detail=f"Точное значение = {p} \n Погрешность = {abs(p-s)} ",)
    


def ExitApp():
    MsgBox = messagebox.askquestion ('Выход из программы','Вы уверены, что хотите выйти?',icon = 'error')
    if MsgBox == 'yes':
       root.destroy()
    else:
        messagebox.showinfo('С возвращением!','Мы рады, что вы остались с нами!')


root = Tk()
root.title("Вычисление площади фигуры, ограниченной кривой")
root.geometry("670x400")

frame = Frame(root,padx=10,pady=10)
frame.pack(expand=True)

label = Label(frame,text='Задание (Вариант 12):',font=("Arial", 14))
label.pack()
label_1 = Label(frame,text='1. Реализовать программу вычисления площади фигуры, ограниченной кривой 1*x^3+(1)*x^2+(5)*x+(3) и осью ОХ.')
label_1.pack()
label_2 = Label(frame,text = '2. Вычисление определенного интеграла должно выполняться численно, с применением метода трапеций')
label_2.pack()
label_3 = Label(frame,text = '3. Пределы интегрирования вводятся пользователем.')
label_3.pack()
label_4 = Label(frame,text = '4. Взаимодействие с пользователем должно осуществляться посредством case-меню.')
label_4.pack()
label_5 = Label(frame,text = '5. Требуется реализовать возможность оценки погрешности полученного результата.')
label_5.pack()
label_6 = Label(frame,text = '6. Необходимо использовать процедуры и функции там, где это целесообразно.')
label_6.pack()

button = Button(frame, text="Понятно!", command=lambda: button.pack_forget())
button.pack()

a = Label(frame,text = "Введите точку а (a<b)")
a.pack()

aa = Entry(frame)
aa.pack()
 
b = Label(frame,text="Введите точку b")
b.pack()

bb = Entry(frame)
bb.pack()

n = Label(frame,text="Введите количество разбиений (n)")
n.pack()

nn = Entry(frame)
nn.pack()

btn = Button(frame, text='Расчитать',command = integrel)
btn.pack(fill =X)

buttonEg = Button (frame, text='Выход',command=ExitApp)
buttonEg.pack(anchor=SE)



def motionUP(event):
    children = frame.winfo_children()
    if event.widget in children:
        index = children.index(event.widget)
        index -= 1
        if index > -1:
            children[index].focus_set()
 
 
def motionDOWN(event):
    children = frame.winfo_children()
    if event.widget in children:
        index = children.index(event.widget)
        index += 1
        if index < len(children):
            children[index].focus_set()

 
root.bind('<Up>', motionUP)
root.bind('<Down>', motionDOWN)


root.mainloop()
