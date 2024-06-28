#Funcion principal
def is_mutant(dna):
    #Almacena todos las veces que chequea
    count_all = 0
    count_horizontal = horizontal_check(dna)
    count_vertical = vertical_check(dna)
    count_diagonal = diagonal_check(dna)
    count_oblique = oblique_check(dna)
    #Llena el contador segun la verificacion de arriba
    if count_horizontal>=1:
        count_all +=1
        if count_horizontal>=2:
            count_all +=2
    if count_vertical>=1:
        count_all +=1
        if count_vertical>=2:
            count_all +=2
    if count_diagonal>=1:
        count_all +=1
        if count_diagonal>=2:
            count_all +=2
    if count_oblique>=1:
        count_all +=1
        if count_oblique>=2:
            count_all +=2
    #Retornamos el contador si es igual o mayor a dos con los correspondientes acertados
    if count_all >=2:
        if count_horizontal>=1:
            print("POR HORIZONTAL", end=", ")
        if count_vertical>=1:
            print("POR VERTICAL", end=", ")
        if count_diagonal>=1:
            print("POR DIAGONAL", end=", ")
        if count_oblique>=1:
            print("POR OBLICUA", end=", ")
        return True
    else:
        return False

#Funcion horizontal para verificar
def horizontal_check(dna):
    count = 0
    for i in dna:
        for j in range(3):
            if i[j] == i[j+1] and i[j] == i[j+2] and i[j] == i[j+3]:
                #Marca con parentesis en los lugares que se encontraron
                i[j] = "X"
                i[j+1] = "X"
                i[j+2] = "X"
                i[j+3] = "X"
                count+=1
    return count
#Funcion vertical para verificar
def vertical_check(dna):
    count = 0
    for i in range(3):
        for j in range(6):
            if dna[i][j] == dna[i+1][j] and dna[i][j] == dna[i+2][j] and dna[i][j] == dna[i+3][j]:
                #Marca con parentesis en los lugares que se encontraron
                dna[i][j] = "X"
                dna[i+1][j] = "X"
                dna[i+2][j] = "X"
                dna[i+3][j] = "X"
                count+=1
    return count
#Funcion diagonal para verificar
def diagonal_check(dna):
    count = 0    
    for i in range(3):
        for j in range(3):
            if dna[i][j] == dna[i+1][j+1] and dna[i][j] == dna[i+2][j+2] and dna[i][j] == dna[i+3][j+3]:
                #Marca con parentesis en los lugares que se encontraron
                dna[i][j] = "X"
                dna[i+1][j+1] = "X"
                dna[i+2][j+2] = "X"
                dna[i+3][j+3] = "X"
                count +=1
    #Bucle para verificar la diagonal inversa
    for i in range(3):
        for j in range(-1,-4,-1):
            if dna[i][j] == dna[i+1][j-1] and dna[i][j] == dna[i+2][j-2] and dna[i][j] == dna[i+3][j-3]:
                #Marca con parentesis en los lugares que se encontraron
                dna[i][j] = "X"
                dna[i+1][j-1] = "X"
                dna[i+2][j-2] = "X"
                dna[i+3][j-3] = "X"
                count +=1
    return count
#Funcion oblicua para verificar
def oblique_check(dna):
    count = 0    
    for i in range(3):
        for j in range(3):
            if dna[i][j] == dna[i+1][j+1] and dna[i][j] == dna[i+2][j+2] and dna[i][j] == dna[i+3][j+3]:
                #Marca con parentesis en los lugares que se encontraron
                #f"({dna[i][j]})"
                dna[i][j] = "X"
                dna[i+1][j+1] = "X"
                dna[i+2][j+2] = "X"
                dna[i+3][j+3] = "X"
                for i in range(3):
                    for j in range(-3,-1,1):
                        if dna[i][j] == dna[i+1][j-1] and dna[i][j] == dna[i+2][j-2] and dna[i][j] == dna[i+3][j-3]:
                            #Marca con parentesis en los lugares que se encontraron
                            dna[i][j] = "X"
                            dna[i+1][j-1] = "X"
                            dna[i+2][j-2] = "X"
                            dna[i+3][j-3] = "X"
                            count +=1
    return count
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
                    letter = letter.upper()
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