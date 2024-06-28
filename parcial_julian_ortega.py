"""PARCIAL DE PROGRAMACION"""
#Mensaje de bienvenida e ingreso de nombre de usuario
print("¡Bienvenido!")
user_name = input("Ingrese su numbre: ")
#Ciclo general del programa
while True:
    print(f"{user_name}, por favor elige un juego:\n"
        "(1) Juego de numeros\n"
        "(2) Juego de palabras\n"
        "(0) Para cerrar programa")
    #Eleccion del juego
    choice = input("Su eleccion: ")
    #Condicionales para validar la eleccion
    if choice=="1":
        #Deficion de variables necesarias para el juego de numeros
        list_num_odd = []
        num_greater = 0
        adittion_odd = 0
        average = 0
        print(f"{user_name}, ingrese numeros enteros (finalizar ingrese 0): ")
        #Ciclo para Juego
        while True:
            user_numbers = int(input("Numero: "))
            if user_numbers == 0:
                print("El numero par mayor es: ", num_greater)
                print("El promedio de la suma de los numero impares es: ", average)
                break
            elif user_numbers % 2 == 0:
                if user_numbers>num_greater:
                    num_greater=user_numbers
            elif user_numbers % 2 != 0:
                adittion_odd += user_numbers
                list_num_odd.append(user_numbers)
                average = adittion_odd /len(list_num_odd) 
        #Vuelta al menu
        print("-------------------------")
        print("Volviendo al Menu...")
        print("-------------------------")
    #Eleccion de juego de palabras
    elif choice =="2":
        #Deficion de variables necesarias para el juego de palabras
        count_a = 0 
        count_e = 0
        count_i = 0
        count_o = 0
        count_u = 0
        phrase = input(f"{user_name}, por favor ingresa una frase: ")
        #Ciclo para la contabilizacion de vocales
        for i in range(len(phrase)):
            if phrase[i].upper() == "A":
                count_a += 1
            elif phrase[i].upper() == "E":
                count_e += 1
            elif phrase[i].upper() == "I":
                count_i += 1
            elif phrase[i].upper() == "O":
                count_o += 1
            elif phrase[i].upper() == "U":
                count_u += 1
        print("Cantidad de vocales encontradas para: \n"
            f"A = {count_a}\n"
            f"E = {count_e}\n"
            f"I = {count_i}\n"
            f"O = {count_o}\n"
            f"U = {count_u}")   
        #Vuelta al menu
        print("-------------------------")
        print("Volviendo al Menu...")     
        print("-------------------------")
    elif choice == "0":
        #Finalizacion del programa
        print("-------------------------")
        print("Cerrando programa...")    
        print("-------------------------")
        break
    else:
        print("¡Error, ingrese un numero valido!")