'''1-	Escribir un programa que pida al usuario una palabra y la 
muestre por pantalla 10 veces.'''
print("-------------")
print("Ejercicio 1")
word = input("Ingrese una palabra: ")
for i in range(10):
    print(word)

'''2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los 
años que ha cumplido (desde 1 hasta su edad).'''
print("-------------")
print("Ejercicio 2")
age = int(input("Ingrese su edad: "))
for i in range(1,age+1):
    print(i)    

'''3-	Escribir un programa que pida al usuario un número entero positivo y muestre por 
pantalla todos los números impares desde 1 hasta ese número separados por comas.'''
print("-------------")

print("Ejercicio 3")
num = int(input("Ingrese un numero entero positivo: "))
if num <= 0:
    print("Error, ingrese un numero positivo")
    exit()

for i in range(1,num+1,2):
    print(i)

'''4-	Escribir un programa que pida al usuario un número entero positivo y muestre por 
pantalla la cuenta atrás desde ese número hasta cero separados por comas.'''
print("-------------")

print("Ejercicio 4")
num = int(input("Ingrese un numero entero positivo: "))
if num <= 0:
    print("Error, ingrese un numero positivo")
    exit()

for i in range(num,-1,-1):
    print(i)

'''5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
 y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que 
 dura la inversión.'''
print("-------------")
print("Ejercicio 5")
amount_money = int(input("Ingrese la cantidad de dinero a invertir: "))
annual_interest = float(input("Ingrese el interes anual %"))
years = int(input("Cantidad de años: "))
money_invested = 0
for i in range(years):
    money_invested += amount_money * (annual_interest/100)

amount_money +=money_invested
print (f"Total a ganar en {years} años ${amount_money}")

'''6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
triángulo rectángulo como el de más abajo, de altura el número introducido.'''
print("-------------")
print("Ejercicio 6")
num = input("Ingrese un numero entero: ")
num_int = int(num)
total = num
for i in range(num_int):
    if i == 0:
        print(num)
    elif i >=1:
        total += num
        print(total)

'''7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.'''
print("-------------")

print("Ejercicio 7")
for i in range(1,11):
    print(f"Tabla del {i}:")
    for j in range (10):
        print(f"{i} x {j} = {i*j}")

'''8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
triángulo rectángulo como el de más abajo.'''
print("-------------")

print("Ejercicio 8")

number = int(input("Ingrese un numero entero: "))

for i in range(number):
    for j in range(i):
        print(number, end="")
    print("")

'''9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''
print("-------------")
print("Ejercicio 9")
password = input("Ingrese la contraseña: ")

while True:
    if password == "Maiz123":
        print("Correcto")
        break
    else:
        print("Contraseña incorrecta")
        break

'''10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es 
un número primo o no.'''
print("-------------")
print("Ejercicio 10")
while True:
    number = int(input("Ingrese un nombre para saber si es primo o no: "))
    if number == 0:
        print("No es primo")
        break
    if number <= 1:
        print("No es primo")
        break
    elif number <= 3:
        print("Es primo")
        break
    elif number % 2 == 0 or number % 3 == 0:
        print("No es primo")
        break
    condition = True
    for i in range(5, int(number**0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            condition = False
            break
    if condition == True:
        print("Es primo")
        break
    else:
        print("No es primo")
        break

'''11-	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a 
una las letras de la palabra introducida empezando por la última.'''
print("-------------")
print("Ejercicio 11")

word = input("Ingrese una palabra: ")

for i in range(-1,-(len(word))-1,-1):
    print(word[i], end="")
    
print("")

'''12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, y 
muestre por pantalla el número de veces que aparece la letra en la frase.'''
print("-------------")
print("Ejercicio 12")

word = input("Ingrese una frase: ")
letter = input("Ingrese la letra a verificar: ")
word = word.upper()
letter = letter.upper()
count = 0
for i in range(len(word)):
    if word[i]==letter:
        count +=1
print(f"La letra esta {count} veces")

'''13-	Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que 
el usuario escriba “salir” que terminará.'''
print("-------------")
print("Ejercicio 13")
while True:
    words_eco = input("Ingrese una palabra: ")
    words_eco = words_eco.lower()
    if words_eco=="salir":
        break
    else:
        print(words_eco)

'''14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y 
cuáles impares desde el primero hasta el segundo.'''
print("-------------")
print("Ejercicio 14")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un segundo numero: "))
if num1>num2:
    for i in range(num2,num1):
        if i % 2 == 0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")
elif num2>num1:
    for i in range(num1,num2):
        if i % 2 == 0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")
elif num1==num2:
    if num1 % 2 ==0:
        print("Los numeros son pares")
    else:
        print("Los numeros son impares")

'''15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.'''
print("-------------")
print("Ejercicio 15")
while True:
    num = int(input("Ingrese un numero mayor que 0: "))
    if num<=0:
        continue
    for i in range(1,num+1):
        if num % i == 0:
            print(f"{i} es divisor de {num}")
    break

'''16-	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números 
y escriba cuántos negativos ha introducido.'''
print("-------------")
print("Ejercicio 16")

num = int(input("Ingrese la cantidad de numero a introducir: "))
count = 0
for i in range(num):
    numbers = int(input(f"Ingrese el numero {i+1}: "))
    if numbers < 0:
        count+=1
print(f"La cantidad de numeros negativos es de {count}")

'''17-	Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales 
que aparecen en esa frase (sin repetirlas).'''
print("-------------")
print("Ejercicio 17")
phrase = input("Ingrese una frase: ")

phrase = phrase.lower()
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for i in range(len(phrase)):
    if phrase[i]=="a":
        count_a +=1
    elif phrase[i]=="e":
        count_e +=1
    elif phrase[i]=="i":
        count_i +=1 
    elif phrase[i]=="o":
        count_o +=1
    elif phrase[i]=="u":
        count_u +=1

if count_a>=1:
    print("A, ",end="")
if count_e>=1:
    print("E, ",end="")
if count_i>=1:
    print("I, ",end="")    
if count_o>=1:
    print("O, ",end="")
if count_u>=1:
    print("U, ",end="")
print("")

if count_a == 0 and count_e == 0 and count_i == 0 and count_o == 0 and count_u == 0:
    print("No hay vocales en su frase")

'''18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de 
los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…'''
print("-------------")
print("Ejercicio 18")
previous1 = 0
previous2 = 1
resul = 0
for i in range(10):
    if i == 0:
        print(0)
    elif i == 1:
        print(1)
    elif i>1:
        resul = previous1+previous2
        print(resul)
        previous1 = previous2
        previous2 = resul

'''19-	Escriba un programa que simule una alcancía. El programa solicitará primero una 
cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa 
solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado 
iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean 
positivas.'''
print("-------------")
print("Ejercicio 19")
while True:
    money_saving = int(input("Ingrese la cantidad de dinero a ahorrar: "))
    if money_saving<=0:
        print("Error, ingrese una cantidad correcta")
    else:
        break
stored = 0
while True:
    put_money = int(input("Cantidad de dinero a ahorrar ahora: $"))
    if put_money <=0:
        print("Error, ingrese una cantidad correcta")
        continue
    stored += put_money
    if stored>=money_saving:
        print("Felicidades has llegado al objetivo!")
        print(f"Has ahorrado: ${stored}")
        break

'''20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos 
los números ingresados.'''
print("-------------")
print("Ejercicio 20")
add_numbers = 0
while True:
    numbers = int(input("Ingrese un numero o 0 para salir: "))
    if numbers ==0:
        print(f"La suma de todos los numeros ingresados es:{add_numbers}")
        break
    add_numbers +=numbers

'''21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número 
ingresado.'''
print("-------------")
print("Ejercicio 21")
num_greater = 0 
while True:
    numbers = int(input("Ingrese un numero o 0 para salir: "))
    if numbers==0:
        print(f"El mayor numero ingresado fue: {num_greater}")
        break
    elif numbers > num_greater:
        num_greater = numbers

'''22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que 
lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números 
ingresados por el usuario fueron números pares.'''
print("-------------")
print("Ejercicio 22")
num_peers = 0
while True:
    add = 0
    numbers = int(input("Ingrese un numero entero positivo o (-1) para SALIR: "))
    if numbers==-1:
        break
    elif numbers<0:
        print("No se permiten numeros negativos")
        continue

    if numbers %2 ==0:
        num_peers += 1
    while numbers > 0:
        digit = numbers % 10  
        add += digit  
        numbers //= 10  
    print(f"Suma de los digitos es: {add} ")
    print("")
print(f"La cantidad de numeros pares es de {num_peers}")

'''23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la 
cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario 
ingrese el monto 0.'''
print("-------------")
print("Ejercicio 23")
print("Para salir pulse: 0")
while True:
    amount_buys = float(input("Ingrese el monto de la compra: "))
    if amount_buys == 0:
        break

'''24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, 
informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de 
descuento.'''
print("-------------")
print("Ejercicio 24")
add = 0
print("Para salir pulse: 0")
while True:
    amount_buys = int(input("Ingrese el monto de la compra: "))
    if amount_buys <0:
        print("No se permiten numeros negativos")
        continue
    elif amount_buys == 0:
        break
    add += amount_buys
    print(f"Suma por ahora: {add}")

if add>1000:
    add = add - add*0.10
    print(f"Total: ${add}. Descuento del %10 aplicado")
else:
    print(f"Total: ${add}. El descuento del %10 no fue aplicado, su compra no supera los $1.000") 

'''25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos 
los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.''' 
print("-------------")
print("Ejercicio 25")

number = int(input("Ingrese un numero: "))
multiplication = 1
if number == 0:
    resul = 1
for i in range(1,number+1):
    multiplication *= i
if number ==0:
    print(f"EL factorial de {number} es {resul}")
print(f"El factorial de {number} es {multiplication}")
    








        

    