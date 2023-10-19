import funciones
while True:
    number = int(input("ingrese un numero: "))
    if number !=0:
        print(funciones.sumar_digitos(number))
    else:
        break