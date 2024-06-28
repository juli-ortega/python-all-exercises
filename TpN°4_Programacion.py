'''1-   Create a while loop with the following characteristics:

• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x.
'''
print("Ejercicio 1")
x=0
while x !=30:
    print(f"El valor de x : {x}")
    x+=1

    if x==15:
        print(f"La ejecucion se rompio cuando x = {x}")
        break
    elif x == 4 or x==6 or x==10:
        print(f"El valor {x} de x fue salteado")
        x+=1
        continue

'''1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. 
Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.'''
print("------------")
print("Ejercicio 2")
while True:
    line = input("Ingrese lineas: ")
    if line =="":
        print("Ha finalizado la entrada de lineas")
        break

'''2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos

Ejemplo de una entrada:
D 200
D 200
R 100
D 50
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería: 350 '''
print("------------")
print("Ejercicio 3")
deposit = 0

while True:
    print(f"Saldo actual: {deposit}")
    operation = input("Ingrese su operacion: (D) Depositar , (R) Retirar , (ENTER) Finalizar ")
    if operation =="":
        print(f"Ha finalizado total en el banco: ${deposit}")
        break

    number = int(operation[2:])
    select = operation[0]
    select = select.upper()

    if select=="D":
        deposit += number
        print("Su dinero ha sido depositado")
    elif select=="R":
        if deposit>number:
            deposit-= number
            print("Retirando...")
        else:
            print("Dinero insuficiente")

'''3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero. Imprimir la cantidad total de números primos ingresados.
Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.'''
print("------------")
print("Ejercicio 4")
print("Presione 0 para finalizar:")
prime_numbers = 0
while True:
    number = int(input("Ingrese numero mayores que 0: "))
    if number == 0:
        break
    if number <= 1:
        continue
    elif number <= 3:
        prime_numbers+=1
        continue
    elif number % 2 == 0 or number % 3 == 0:
        continue
    condition = True
    for i in range(5, int(number**0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            condition = False
            break
    if condition == True:
        prime_numbers +=1

print(f"La cantidad de numeros primos fue de: {prime_numbers}")

'''4.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, 
que sean bisiestos y múltiplos de 10. Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser 
divisible por 100, excepto que también sea divisible por 400.'''
print("------------")
print("Ejercicio 5")
year1 = int(input("Ingrese el primer año: "))
year2 = int(input("Ingrese el segundo año: "))

if year1>year2:
    for i in range(year2,year1):
        if i%4==0 and i%100 !=0 and i%10==0:
            print(f"{i} es multiplo de 10 y es un año bisiesto")
        elif i%4==0 and i%100 ==0 and i%400==0 and i%10==0:
            print(f"{i} es multiplo de 10 y es un año bisiesto")
        elif i%4==0 and i%100 !=0:
            print(f"{i} es un año bisiesto pero no es multiplo de 10")
        elif i%4==0 and i%100 ==0 and i%400==0:
            print(f"{i} es un año bisiesto pero no es multiplo de 10")
        elif i%10==0:
            print(f"{i} No es un año bisiesto pero es multiplo de 10")
        else:
            print(f"{i} No es un año bisiesto y tampoco es multiplo de 10")

elif year2>year1:
    for i in range(year1,year2):
        if i%4==0 and i%100 !=0 and i%10==0:
            print(f"{i} es multiplo de 10 y es un año bisiesto")
        elif i%4==0 and i%100 ==0 and i%400==0 and i%10==0:
            print(f"{i} es multiplo de 10 y es un año bisiesto")
        elif i%4==0 and i%100 !=0:
            print(f"{i} es un año bisiesto pero no es multiplo de 10")
        elif i%4==0 and i%100 ==0 and i%400==0:
            print(f"{i} es un año bisiesto pero no es multiplo de 10")
        elif i%10==0:
            print(f"{i} No es un año bisiesto pero es multiplo de 10")
        else:
            print(f"{i} No es un año bisiesto y tampoco es multiplo de 10")
else:
    print("Los años ingresados son iguales")

'''5.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración 
continue para omitir los números impares.'''
print("------------")
print("Ejercicio 6")

for i in range(1,21):
    if i % 2 !=0:
        continue
    else:
        print(i)

'''6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el 
número, usa break para salir del bucle.'''

list_number = [2,4,5,6,7,89,23,43,65]
condition = True
for i in list_number:
    number = int(input("Encuentra el numero en la lista: "))
    if number in list_number:
        condition = False
        print("Numero encontrado en la lista")
        break

if condition:
    print("El numero no se encontro en la lista")
print(list_number)

'''7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para 
permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle 
(Mostrar un mensaje por cada opción elegida).'''

while True:
    print("---------Menu-------\n"
          "(1) Depositar\n"
          "(2) Retirar\n"
          "(3) Saldo\n"
          "(0) Finalizar")
    choice = input()
    if choice == "1":
        print("Depositando...")
    elif choice == "2":
        print("Retirando...")
    elif choice == "3":
        print("Tu saldo: $38.900")
    elif choice == "0":
        break
        



