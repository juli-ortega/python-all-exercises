from functions import is_mutant, fill_dna, test_cases
print("Bienvenido a el juego de mutantes")
#Bucle principal para cargar el ADN de los mutantes
while True:                       
    #Decision para cargar el ADN
    while True:
        dna = []
        condition = input("Deseas llenar con:\n(1) ADN manualmente \n(2) ADN de manera aleatoria \n(3) Casos de Prueba\nEleccion: ")
        if condition == "1" or condition =="2":
            dna = fill_dna(condition,dna)
            break
        elif condition =="3":
            dna = test_cases(dna)
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
    else:
        print("ES HUMANO\n---------------")
    #Decision para cargar otro
    while True:
        upload_other = input("¿Deseas cargar otro? (1) Si o (2)No: ")
        if upload_other != "1" and upload_other!="2":
            print("Error el numero es incorrecto. Intente de nuevo.")
        else:
            break
    
    if upload_other == "2":
        print("----------------------------------\nGracias por utilizar nuestro juego\n----------------------------------")
        break
    