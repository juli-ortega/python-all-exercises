import sys

sys.path.append("C:/Users/miaca/Documents/Programacion/Functions")
from Functions import *

'''3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las 
posiciones en donde se encuentra b dentro de a. Ejemplo:'''
print("-------------")
print("Ejercicio 3")
string1 = input("Ingrese una frase: ")
short_phrase = input("Ingrese las letras o frase corta que quiera buscar: ")

positions = find_positions(string1, short_phrase)

print("Las posiciones en las que se encuentra '{}' en '{}' son:".format(string1, short_phrase))
print(positions)

'''1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.'''
print("-------------")
print("Ejercicio 1")
while True:
    num = int(input("Ingrese numero enteros positivos: "))
    if num<0:
        print("Error, ingresaste un numero negativo")
        continue
    else:
        print(f"El numero {num} contiene {count_digits(num)} digitos. ")
        break

'''9.	Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, y un número k, 
e imprima todas las posibles cadenas de longitud k formadas con los caracteres dados (permitiendo caracteres repetidos).'''
print("-------------")
print("Ejercicio 9")
list_of_character = []
print("Para finalizar solo presione (enter)")
while True:
    characters = input("Ingrese caracteres unicos: ")
    if len(characters)>1:
        print("Debe ingresar solamente un caracter")
        continue
    elif characters == "":
        break
    else:
        list_of_character.append(characters)

k = int(input("Elija un numero mayor a 1: "))

combinations(list_of_character,k)



