import tkinter as tk

root = tk.Tk()

a = tk.StringVar()
b = tk.StringVar()
sumar = tk.IntVar()
restar = tk.IntVar()
multiplicar = tk.IntVar()
dividir = tk.IntVar()
mensaje = tk.IntVar()

sw = True
def sumar():
    suma = int(a.get()) + int(b.get())
    mensaje.set(suma)
    a.set('')
    b.set('')
def restar():
    resta = int(a.get()) - int(b.get())
    mensaje.set(resta)
    a.set('')
    b.set('')
def multiplicar():
    multiplica = int(a.get()) * int(b.get())
    mensaje.set(multiplica)
    a.set('')
    b.set('')
def dividir():
    divide = int(a.get()) / int(b.get())
    mensaje.set(divide)
    a.set('')
    b.set('')

root.geometry('300x300')
root.title('Calculadora')

root.configure(bg="#009688")

tk.Label(root, text='Calculadora', bg="#009688", fg='white', font=('', 24)).place(x=65, y=20)

#Numero Uno
tk.Label(root, text='Digite un numero', bg="#009688", fg='white', font=('', 13)).place(x=30, y=80)
tk.Entry(root, justify='center', textvariable=a).place(x=32, y=110)
#Numero Dos
tk.Label(root, text='Digite un numero', bg="#009688", fg='white', font=('', 13)).place(x=30, y=140)
tk.Entry(root, justify='center', textvariable=b).place(x=32, y=170)

#Sumar
tk.Button(root, text='Sumar', bd=3, command=sumar).place(x=190, y=90)
#Restar
tk.Button(root, text='Rertar', bd=3, command=restar).place(x=190, y=135)
#Multiplicar
tk.Button(root, text='Multiplicar', bd=3, command=multiplicar).place(x=190, y=180)
#Dividir
tk.Button(root, text='Dividir', bd=3, command=dividir).place(x=190, y=225)
#Resultado
tk.Label(root, text='Resultado', bg="#009688", fg='white', font=('', 14)).place(x=47, y=195)
tk.Label(root, textvariable=mensaje, bg="#009688", fg='white', font=('', 20)).place(x=77, y=220)
#Salir
tk.Button(root, text='Salir', bd=3, command=root.destroy).place(x=130, y=268)

root.mainloop()
