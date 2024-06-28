#Funcion principal
def is_mutant(dna):
    if horizontal_check(dna):
        print("POR HORIZONTAL", end=", ")
        return True
    elif vertical_check(dna):
        print("POR VERTICAL", end=", ")
        return True
    elif diagonal_check(dna):
        print("POR DIAGONAL", end=", ")
        return True
    else:
        return False    
#Funcion horizontal para verificar
def horizontal_check(dna):
    for i in dna:
        for j in range(3):
            if i[j] == i[j+1] and i[j] == i[j+2] and i[j] == i[j+3]:
                #Marca con parentesis en los lugares que se encontraron
                i[j] = f"({i[j]})"
                i[j+1] = f"{i[j]}"
                i[j+2] = f"{i[j]}"
                i[j+3] = f"{i[j]}"
                return True
    return False
#Funcion vertical para verificar
def vertical_check(dna):
    for i in range(3):
        for j in range(6):
            if dna[i][j] == dna[i+1][j] and dna[i][j] == dna[i+2][j] and dna[i][j] == dna[i+3][j]:
                #Marca con parentesis en los lugares que se encontraron
                dna[i][j] = f"({dna[i][j]})"
                dna[i+1][j] = f"{dna[i][j]}"
                dna[i+2][j] = f"{dna[i][j]}"
                dna[i+3][j] = f"{dna[i][j]}"
                return True
    return False
#Funcion diagonal para verificar
def diagonal_check(dna):    
    for i in range(3):
        for j in range(3):
            if dna[i][j] == dna[i+1][j+1] and dna[i][j] == dna[i+2][j+2] and dna[i][j] == dna[i+3][j+3]:
                #Marca con parentesis en los lugares que se encontraron
                dna[i][j] = f"({dna[i][j]})"
                dna[i+1][j+1] = f"{dna[i][j]}"
                dna[i+2][j+2] = f"{dna[i][j]}"
                dna[i+3][j+3] = f"{dna[i][j]}"
                return True
    #Bucle para verificar la diagonal inversa
    for i in range(3):
        for j in range(-1,-4,-1):
            if dna[i][j] == dna[i+1][j-1] and dna[i][j] == dna[i+2][j-2] and dna[i][j] == dna[i+3][j-3]:
                #Marca con parentesis en los lugares que se encontraron
                dna[i][j] = f"({dna[i][j]})"
                dna[i+1][j-1] = f"{dna[i][j]}"
                dna[i+2][j-2] = f"{dna[i][j]}"
                dna[i+3][j-3] = f"{dna[i][j]}"
                return True
    return False

import random
#Llena ADN
def fill_dna(condition, dna):
    #Manera manual
    if condition == "1":
        for i in range(6):
            add_list = []
            for j in range(6):
                while True:
                    letter = input(f"Ingrese la letra de la fila {i}, Columna {j}: ")
                    if letter != "A" and letter != "T" and letter != "C" and letter != "G":
                        print("Error, ingresaste una base nitrogenada incorrecta. Recuerda estas deben ser ('A','C','T','G')")
                    else:
                        add_list.append(letter)
                        break
            dna.append(add_list)
    #Manera aleatoria
    else:
        posible_letter = ["A","T","C","G"]
        for i in range(6):
            add_list = []
            for j in range(6):
                while True:
                    letter = random.choice(posible_letter)
                    add_list.append(letter)
                    break
            dna.append(add_list)
    return dna