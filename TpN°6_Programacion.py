import sys

sys.path.append("C:/Users/miaca/Documents/Programacion/Functions")
from Functions import *

'''6.	Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, 
finalizando al ingresar 'x'. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, 
finalizando al ingresar 'x'.
a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.'''

print("------------")
print("Ejercicio 6")

list_primary = []
list_high = []
print("Ingrese los nombres de los alumnos del nivel primario: ")
print("Para finalizar ingrese 'X' ")
while True:
    students = input("Nombre: ")
    condition = students.upper()
    if condition == "X":
        break
    else:
        list_primary.append(students)

print("Ingrese los nombres de los alumnos del nivel secundario: ")
print("Para finalizar ingrese 'X' ")

while True:
    students = input("Nombre: ")
    condition = students.upper()
    if condition == "X":
        break
    else:
        list_high.append(students)

list_primary = lower_list(list_primary)
list_high = lower_list(list_high)

names_any_repeat_primary = set(list_primary)
names_any_repeat_high = set(list_high)

print("Lista primaria sin nombres repetidos: ")
print(names_any_repeat_primary)
print("Lista secundario sin nombres repetidos: ")
print(names_any_repeat_high)

dictio_with_repeat_primary = count_of_names_repeat(list_primary)

for names, counts in dictio_with_repeat_primary.items():
    if counts > 1:
        print(f"{names} se repite {counts} veces.")

dictio_with_repeat_high = count_of_names_repeat(list_high)

for names, counts in dictio_with_repeat_high.items():
    if counts > 1:
        print(f"{names} se repite {counts} veces.")

for i in list_primary:
    if not i in list_high:
        print(f"El nombre {i} no se repite en el nivel secundario")

'''7.	Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 
50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados.'''
print("------------")
print("Ejercicio 7")
list_of_string = []
for i in range(2):
    strings = input(f"Ingrese la cade {i+1}: ")
    strings = strings.lower()
    for j in strings:
        list_of_string.append(j)
    
list_of_string = count_of_names_repeat(list_of_string)

for letter, counts in list_of_string.items():
    print(f"'{letter}' = {counts} ")

'''8.	Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, participaron en un 
campeonato de fútbol con modalidad todos contra todos.
Los goles anotados en cada encuentro se registraron en el siguiente cuadro:
Escriba un programa que:
o	Lea el cuadro de goles en un arreglo de dos dimensiones.
o	Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
o	Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
o	Determine la cantidad de puntos obtenidos por cada equipo.
'''
print("------------")
print("Ejercicio 8")
teams = [[0,4,2,1], [5,0,3,2], [0,2,0,1] ,[1,0,2,0]]

resuls = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]


for i in range(len(teams)):
    for j in range(len(teams[i])):
        if i == j:
            continue
        else:
            goals_teams_i = teams[i][j]
            goals_teams_j = teams[j][i]
            #Goles marcados
            resuls[i][3] +=goals_teams_i
            #Goles recibidos
            resuls[i][4] += goals_teams_j

            if goals_teams_i>goals_teams_j:
                resuls[i][0] +=1
                #Suma puntos al primer equipo
                resuls[i][5] +=3
            elif goals_teams_i<goals_teams_j:
                resuls[i][2] +=1
                #Suma puntos al segundo equipo
            else:
                #Empate y suma de puntos
                resuls[i][1] +=1
                resuls[i][5] +=1

print("             G   E   P  GM  GR  PUNTOS")

for i in range(len(resuls)):
    print(f"Equipo {i+1 :2}:", end=" ")
    for j in range(len(resuls[i])):
        print(f"{resuls[i][j] :3}", end=" ")
    print("")

'''10.	Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
a.	la diagonal principal.
b.	la diagonal inversa.'''
print("------------")
print("Ejercicio 10")
matrix = [[8,7,9,2],[5,6,3,7],[4,6,9,0],[2,3,4,3]]
print("Matriz normal: ")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
    print("")

print("Diagonal de la matriz: ")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==j:
            print(matrix[i][j], end=" ")

print("")

print("Diagonal inversa: ")
column = len(matrix[0])
for i in range(len(matrix)):
    print(matrix[i][-(i+1)], end=" ")
print("")












