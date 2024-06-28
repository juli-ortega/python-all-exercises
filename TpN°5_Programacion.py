import sys

sys.path.append("C:/Users/miaca/Documents/Programacion/Functions")
from Functions import *

'''1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.'''
print("------------")
print("Ejercicio 1")
while True:
    dni = input("Ingrese su DNI: ")
    if return_dni(dni):
        break
    else:
        print("Error en el ingreso de du DNI, vuelva a intentarlo")

'''2.	Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras 
están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por 
parámetro.'''
print("------------")
print("Ejercicio 2")
phrase = input("Ingrese una frase: ")
end_word(phrase)

'''3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. 
Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el 
ingreso de un nombre vacio.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso 
será: nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un 
bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de 
letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
Nombre: María Ines Rosales
DNI: 25469648
ID -> Maria7254'''
print("------------")
print("Ejercicio 3")
name = input("Ingrese sus nombres y su primer apellido: ")
while True:
    dni = input("Ingrese su DNI: ")
    if return_dni(dni):
        break
    else:
        print("Error en el ingreso de du DNI, vuelva a intentarlo")

id = first_word(name)+dni[0:3]

print(f"Nombre: {name}")
print(f"DNI: {dni}")
print(f"ID: {id}")

'''4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una 
función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.'''
print("------------")
print("Ejercicio 4")
num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))

if num2 == num1:
    print("Los numeros son iguales")
elif get_num_mult(num1,num2):
    print("Un numero es multiplo de otro")
else:
    print("Ningun numero es multiplo de otro")

'''5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un 
programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya 
mostrando la media. El programa pedirá el número de días que se van a introducir.'''
print("------------")
print("Ejercicio 5")

days = int(input("Ingrese la cantidad de dias a introducir: "))

for i in range(days):
    print(f"Dia {i+1}")
    max = int(input("Ingrese la temperatura maxima: "))
    min = int(input("Ingrese la temperatura minima: "))
    print(f"La temperatura media del dia {i+1} es: {temp_max_min(max,min)}°C")

'''6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada 
letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.'''
print("------------")
print("Ejercicio 6")

phrase = input("Ingrese la frase: ")
print(split_letters(phrase))

'''7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un 
programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.'''
print("------------")
print("Ejercicio 7")
list_number = []
print("Para salir solo ingrese 0:")
while True:
    numbers = int(input("Ingrese un numero: "))
    if numbers == 0:
        break
    else:
        list_number.append(numbers)

maxim, minin = get_max_min(list_number)

print(f"El mayor es {maxim}")
print(f"El menor es {minin}")

'''8.	Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un 
programa principal que lea el radio de una circunferencia y muestre su área y perímetro.'''
print("------------")
print("Ejercicio 8")

radio = float(input("Ingrese el radio de la circurferencia: "))

area, perimeter = calculate(radio)

print(f"El area de la circurferencia es: {area:.2f}")
print(f"El perimetro de la circurferencia es: {perimeter:.2f}")

'''9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si 
el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado 
hacer login y si no se ha podido hacer login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente 
tenemos tres oportunidades para intentarlo.'''
print("------------")
print("Ejercicio 9")
attemps = [0]
while attemps[0]<3:
    user = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")
    if login(user,password,attemps):
        print("Acceso correcto")
        break
    else:
        print("Vuelva a intentarlo")

if attemps[0] ==3:
    print("Lo siento, te quedaste sin intentos")

'''10.	Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los 
precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio 
final de la compra.'''
print("------------")
print("Ejercicio 10")

dictio = {}

amount_product = int(input("Ingrese la cantidad de productos: "))
for i in range(amount_product):
    price = int(input("Ingrese el precio: $ "))
    discount = int(input("Ingrese el descuento que se le aplica: %"))
    dictio[price] = discount
new_dict = discount_prices(dictio)
for i in new_dict:
    print(f"${i} aplicado el descuento del queda en ${new_dict[i]}")

'''11.	Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la 
función dada a cada uno de los elementos de la lista.'''
print("------------")
print("Ejercicio 11")
list_add = []
print("Para finalizar ingrese 0")
while True:
    element = int(input("Ingrese numeros enteros: "))
    if element ==0:
        break
    list_add.append(element)

print(f"Lista antes: {list_add}")
print(f"Lista nueva: {mult_elements(list_add)}") 
print("Los numeros fueron multiplicados x2")

'''12.	Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.'''
print("------------")
print("Ejercicio 12")
phrase = input("Ingrese una frase: ")
print("Tu frase con sus palabras y sus longitudes: ")
print(new_dict_for_phrase(phrase))

'''13.	Escribir una función que calcule el módulo de un vector.'''
print("------------")
print("Ejercicio 13")
amount = int(input("Ingrese la cantidad de dimensiones del vector: "))
print(f"El modulo de un vector es:{module_of_vec(amount)}")

'''14.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana 
que lo decida.'''
print("------------")
print("Ejercicio 14")

number = int(input("Ingrese el numero: "))

if is_cousin(number):
    print("El numero es primo")
else:
    print("El numero no es primo")

'''15.	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad 
total de números leídos en total. Utilizar una o más funciones, según sea necesario.'''
print("------------")
print("Ejercicio 15")

list_fact = []
print("Para finalizar ingrese 0")
while True:
    numbers = int(input("Ingrese el numero: "))
    if numbers ==0:
        break
    list_fact.append(numbers)

for i in list_fact:
    print(f"El factorial de {i} es {factorial(i)}")

'''16.	Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el 
número, utilizando para ello una función que calcule la frecuencia.'''
print("------------")
print("Ejercicio 16")
num = input("Ingrese un numero entero: ")
digit = input("Ingrese el digito a buscar: ")

print(f"EL digito aparece {search_digit(num,digit)} veces")


'''17.	Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea 
primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de 
veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.'''
print("------------")
print("Ejercicio 17")
list_fact =[]
while True:
    num = int(input("Ingrese numeros primos: "))
    if not is_cousin(num):
        break
    list_fact.append(num)

for i in list_fact:
    digit = input("Ingrese el digito a buscar: ")
    print(f"La suma de sus digitos es de {add_digits(i)}")
    print(f"El digito {digit} se encuentra {search_digit(i,digit)} veces")

num_max, minin = get_max_min(list_fact)
print(f"El factorial de {num_max} es {factorial(num_max)} ")










