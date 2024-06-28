import sys
import random
sys.path.append("C:/Users/miaca/Documents/Programacion/Functions")
from Functions import *
'''3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro
(título, autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en función de un 
campo específico, como el año de publicación o el autor.'''
print("-------------")
print("Ejercicio 3")

library = [
    {
        "Título": "Cien años de soledad",
        "Autor": "Gabriel García Márquez",
        "Año de Publicación": 1967,
        "Género": "Realismo mágico"
    },
    {
        "Título": "1984",
        "Autor": "George Orwell",
        "Año de Publicación": 1949,
        "Género": "Distopía"
    },
    {
        "Título": "El Gran Gatsby",
        "Autor": "F. Scott Fitzgerald",
        "Año de Publicación": 1925,
        "Género": "Ficción"
    },
    {
        "Título": "Matar a un ruiseñor",
        "Autor": "Harper Lee",
        "Año de Publicación": 1960,
        "Género": "Novela social"
    },
    {
        "Título": "Don Quijote de la Mancha",
        "Autor": "Miguel de Cervantes",
        "Año de Publicación": 1615,
        "Género": "Novela clásica"
    }
]

ordered_library = order_library(library)
for book in ordered_library:
    print(f"Título: {book['Título']}, Año de Publicación: {book['Año de Publicación']}")

'''4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su 
longitud. Puedes utilizar el método de ordenamiento de inserción.'''
print("-------------")
print("Ejercicio 4")
list_of_strings = []
print("Para finalizar ingrese 0")
while True:
    strings = input("Ingrese cadenas: ")
    if strings =="0":
        break
    else:
        list_of_strings.append(strings)

print("Odenado por longitud de cada cadena: ")
print(insertion_sort(list_of_strings))

'''7.	Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta lista 
de manera que primero estén los números ordenados de menor a mayor y luego las cadenas de caracteres ordenadas 
alfabéticamente.'''
print("-------------")
print("Ejercicio 7")
list_of_strings = []
list_with_numbers = []
print("Para finalizar ingrese 0")
while True:
    strings = input("Ingrese cadenas: ")
    if strings =="0":
        break
    else:
        list_of_strings.append(strings)
        list_with_numbers.append(random.randint(0,40))
print("Lista de numeros generada automaticamente:")
print(list_with_numbers)

print("Lista de numero ordenada: ")
print(insertion_sort_ints(list_with_numbers))

print("Lista de cadenas ordenada alfabeticamente: ")
print(order_strings_for_alpha(list_of_strings))

'''1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el 
método de ordenamiento de burbuja.'''
print("-------------")
print("Ejercicio 1")
list_with_numbers = []
print("Para finalizar ingrese 0")
while True:
    numbers = int(input("Ingrese numeros: "))
    if numbers == 0:
        break
    else:
        list_with_numbers.append(numbers)

print("Tu lista ordenada por el metodo de la burbuja:")
print(bubble_sort(list_with_numbers))

