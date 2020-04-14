sw = True

def sumar():
    a = int(input('Digite primer numero: '))
    b = int(input('Digite segundo numero: '))
    suma = a+b
    print('La suma es igual a: ',suma)
def restar():
    a = int(input('Digite primer numero: '))
    b = int(input('Digite segundo numero: '))
    resta = a - b
    print('La resta es igual a: ',resta)
def multiplicar():
    a = int(input('Digite primer numero: '))
    b = int(input('Digite segundo numero: '))
    multiplica = a * b
    print('La multiplicacion es igual a: ',multiplica)
def dividir():
    a = int(input('Digite primer numero: '))
    b = int(input('Digite segundo numero: '))
    divide = a/b
    print('La division es igual a: ',divide)
def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False
def opc_no_disponible():
    print('Opcion no disponible')


menu = '''
*******Calculadora********
\t 1 -> Sumar
\t 2 -> Restar
\t 3 -> Multiplicar
\t 4 -> Dividir
\t 5 -> Salir
'''
while sw:
    print(menu)
    opc = int(input('Donde desea ingresar: '))
    if opc is 1:
        sumar()
    elif opc is 2:
        restar()
    elif opc is 3:
        multiplicar()
    elif opc is 4:
        dividir()
    elif opc is 5:
        terminar_programa()
    else:
        opc_no_disponible()