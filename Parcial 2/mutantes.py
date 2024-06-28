from functions import is_mutant, fill_dna
print("Bienvenido a el juego de mutantes")
'''dna = [
        ["T", "G", "A", "T", "C", "A"],
        ["T", "T", "T", "C", "G", "A"],
        ["G", "T", "T", "T", "G", "A"],
        ["T", "A", "G", "T", "A", "A"],
        ["G", "G", "A", "A", "A", "C"],
        ["A", "A", "G", "G", "G", "G"]]'''
#Bucle principal para cargar el ADN de los mutantes
while True:                       
    #Decision para cargar el ADN
    while True:
        dna = []
        condition = input("Deseas llenar el (1) ADN manualmente o (2) ADN de manera aleatoria: ")
        if condition == "1":
            dna = fill_dna(condition,dna)
            break
        elif condition =="":
            dna = fill_dna(condition,dna)
            break
        else:
            print("Error el numero es incorrecto. Intente de nuevo.")
    #Se muestra el ADN originado
    print("---------------\nADN ORIGINADO:")
    for i in range(6):
        for j in range(6):
            print(dna[i][j], end=", ")
        print("")
    print("---------------")
    #Llamada a la funcion para verificar si es mutante o no
    if is_mutant(dna):
        print("ES MUTANTE\n---------------")
        
        for i in range(6):
            for j in range(6):
                print(dna[i][j], end=", ")
            print("")
    else:
        print("ES HUMANO\n---------------")
    #Decision para cargar otro
    while True:
        upload_other = input("¿Deseas cargar otro? (1) Si o (2)No: ")
        if upload_other != "" and upload_other!="2":
            print("Error el numero es incorrecto. Intente de nuevo.")
        else:
            break
    
    if upload_other == "2":
        print("----------------------------------\nGracias por utilizar nuestro juego\n----------------------------------")
        break