#Funcion principal
def is_mutant(dna):
    count_all = 0
    #Almacena todos las veces que chequea
    count_horizontal = horizontal_check(dna)
    count_vertical = vertical_check(dna)
    count_diagonal = diagonal_check(dna)
    count_oblique = oblique_check(dna)
    #Verificacion de contador horizontal si es uno suma solo uno y si son dos suma dos
    if count_horizontal>=1:
        count_all +=1
        if count_horizontal>=2:
            count_all +=2
    #Verificacion de contador vertical si es uno suma solo uno y si son dos suma dos
    if count_vertical>=1:
        count_all +=1
        if count_vertical>=2:
            count_all +=2
    #Verificacion de contador oblicua si es uno suma solo uno y si son dos suma dos
    if count_oblique>=1:
        count_all +=1
        if count_oblique>=2:
            count_all +=2
    #Verificacion de contador diagonal si es uno suma solo uno y si son dos suma dos
    if count_diagonal>=1:
        count_all +=1
        if count_diagonal>=2:
            count_all +=2
    #Retornamos el contador si aunque sea hay uno retorna el print de cada uno
    if count_all >=2:
        if count_horizontal>=1:
            print("POR HORIZONTAL", end=", ")
        if count_vertical>=1:
            print("POR VERTICAL", end=", ")
        if count_oblique>=1:
            print("POR OBLICUA", end=", ")
        elif count_diagonal>=1:
            print("POR DIAGONAL", end=", ")
        return True
    else:
        return False

#Funcion horizontal para verificar
def horizontal_check(dna):
    count = 0
    row = -1
    for i in range(6):
        for j in range(3):
            #Aca salteamos la horizontal que ya fue hallada
            if row == i:
                continue
            elif dna[i][j] == dna[i][j+1] and dna[i][j] == dna[i][j+2] and dna[i][j] == dna[i][j+3]:
                    #Si detecta que ya encontro en una fila no la vuelve a la misma fila
                    row = i
                    count+=1
    return count
#Funcion vertical para verificar
def vertical_check(dna):
    count = 0
    column = -1
    for i in range(3):
        for j in range(6):
            #Aca salteamos la columna que ya fue hallada
            if column == j:
                continue
            elif dna[i][j] == dna[i+1][j] and dna[i][j] == dna[i+2][j] and dna[i][j] == dna[i+3][j]:
                    #Si detecta que ya encontro en una columna no la vuelve a la misma columna
                    column = j
                    count+=1
    return count
#Funcion diagonal para verificar
def diagonal_check(dna):
    count = 0
    row = -1    
    for i in range(3):
        for j in range(3):
            #Aca salteamos el valor que ya fue hallado
            if row == i and colum == j:
                continue
            elif dna[i][j] == dna[i+1][j+1] and dna[i][j] == dna[i+2][j+2] and dna[i][j] == dna[i+3][j+3]:
                #Almacenamos el segundo elemento y no lo volvemos a tomar mas para que no siga tomando esa misma diagonal
                row = i+1
                colum = j+1
                count +=1
    #Bucle para verificar la diagonal inversa
    row = -1
    for i in range(3):
        for j in range(-1,-4,-1):
            #Aca salteamos el valor que ya fue hallado
            if row == i:
                continue
            elif dna[i][j] == dna[i+1][j-1] and dna[i][j] == dna[i+2][j-2] and dna[i][j] == dna[i+3][j-3]:
                #Almacenamos el segundo elemento y no lo volvemos a tomar mas para que no siga tomando esa misma diagonal
                row = i+1
                count +=1
    return count
#Funcion oblicua para verificar
def oblique_check(dna):
    count = 0    
    for i in range(3):
        for j in range(3):
            if dna[i][j] == dna[i+1][j+1] and dna[i][j] == dna[i+2][j+2] and dna[i][j] == dna[i+3][j+3]:
                for i in range(3):
                    for j in range(-3,-1,1):
                        if dna[i][j] == dna[i+1][j-1] and dna[i][j] == dna[i+2][j-2] and dna[i][j] == dna[i+3][j-3]:
                            count +=1
    return count
import random
#Llena ADN
def fill_dna(condition, dna):
    #Manera manual
    if condition == "1":
        for j in range(6):
            while True:
                state = True
                row = input(f"Ingrese la fila {j+1}: ")
                if len(row)!=6:
                    print("Error, la lista debe tener 6 caracteres de longitud")
                    continue
                row = row.upper()
                for i in row:
                    if i !="A" and i != "T" and i !="C" and i !="G":
                        state = False
                        print("Error, uno de los caracteres no es una base nitrogenada de ADN")
                        break
                if state == True:
                    dna.append(row)
                    break
    #Manera aleatoria
    else:
        posible_letter = ["A","T","C","G"]
        for i in range(6):
            add_letter =""
            for j in range(6):
                letter = random.choice(posible_letter)
                add_letter += letter
            dna.append(add_letter)
    return dna
#Casos de pruebas
def test_cases(dna):
    while True:
        print("-------------")
        print("Elige:")
        election = input("(1) Horizontal\n(2) Vertical\n(3) Diagonal\n(4) Oblicua\nEleccion: ")
        #Caso de prueba Horizontal
        if election == "1":
            dna = ["ATCGTC",
                   "ACTTTT",
                   "TCGATT",
                   "GCTAGC",
                   "GTGGGG",
                   "ATCGAT"]
            return dna
        #Caso de prueba vertical
        elif election == "2":
            dna = ["ATCGTC",
                   "ACGAGC",
                   "TCGATC",
                   "GCGAGC",
                   "GTGGGA",
                   "ATCGAT"]
            return dna
        #Caso de prueba diagonal
        elif election == "3":
            dna = ["ATCGTT",
                   "ACTAGT",
                   "TCGTTG",
                   "GACCTC",
                   "ATGCCC",
                   "ATCGCT"]
            return dna
        #Caso de prueba oblicua
        elif election == "4":
            dna = ["ATCGTT",
                   "ACTAAT",
                   "TCCACG",
                   "GAACGC",
                   "AACGCC",
                   "ACCGAT"]
            return dna