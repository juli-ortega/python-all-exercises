#Creacion de listas para almacenar los planes
list_plan =[]
plan = {"1":"[Plan A] Este plan contiene 3GB , durante 6 meses +2GB de regalo!! ( $3.500 )" ,
        "2":"[Plan B] Este plan contiene 6GB , durante 12 meses +4GB de regalo!! ( $4.200 )" , 
        "3":"[Plan C] Este plan contiene 10GB , durante 18 meses +6GB de regalo!! ( $5.500 )", "4": "[Plan propio]"}
print("--------------------------")
print("¡Bienvenido a CeluMania!")
print("--------------------------")
tries = 2
select_user = {}
#Ingreso a la app con validacion de usuario
while True:
    option = int(input("Si sos nuevo usuario ingrese (1) , cliente resgistrado (2): "))
    if option==1:
        print("Registrase: ")
        email = input("Ingrese su usuario: ")
        if list_plan.__contains__(email):
            print("Usuario ya existe")
        else:
            password = input("Ingrese su contraseña: ")
            print("-------------------------------------")
            print("USUARIO REGISTRADO EXITOSAMENTE...")
            print("-------------------------------------")
            list_plan.append(email)
            list_plan.append(password)
    elif option==2:
        while True or tries!=0:
            print("Iniciar sesion: ")
            email_register = input("Ingrese su usuario: ")
            password_register = input("Ingrese su contraseña: ")
            #Busqueda de usuario en la lista de datos ya almacenados
            if list_plan.__contains__(email_register) and list_plan.__contains__(password_register):
                break
            else:
                print(f"Usuario y/o contraseña incorrecta. Le queda {tries} intentos.")
                tries -=1
                if tries ==0:
                    print("---------------------")
                    print("Te quedaste sin intentos")
                    exit()
        break
    else:
        print("Error, el numero ingresado es incorrecto")
select=0

#Ingreso para usuarios ya registrados.
print("---------------------")
print(f"Bienvenido {email_register}")
while select!=4:
    #Menu de opciones
    print("--------------------")
    print("¿Que desea hacer?")
    print("1-Ver tu Plan")
    print("2-Elegir un nuevo Plan")
    print("3-Dar de baja a tu Plan")
    print("4-Finalizar programa")
    select = int(input("Elija una opcion: "))
    #Condicional para la eleccion de opciones del menu
    if select==1:
        #Ver Plan
        if select_user.__contains__(email_register):
            print("-----------------------")
            print("Tu plan es: ", select_user[email_register])
        else:
            print("-----------------------")
            print("Usted no tiene un plan seleccionado")
    elif select==2:
        #Eleccion de plan
        if select_user.__contains__(email_register):
            print("--------------")
            print("Usted ya tiene un plan seleccionado. Vaya a la seccion 'Ver tu plan' para visualizarlo")
        else:    
            plan1 = int(input("Ingrese (1) para plan basico o (2) para plan a tu propio estilo: "))
            if plan1 == 1:
                print("[--PLAN MOVIL--]")
                print(plan["1"])
                print(plan["2"])
                print(plan["3"])
                plan_option = input("Ingrese 1 : PLAN A , 2 : PLAN B , 3 : PLAN C: ")
                if plan_option=="1":
                    select_user[email_register]= plan["1"]
                    print("------------------------")
                    print("Ha elegido el plan", plan["1"])
                elif plan_option=="2":
                    select_user[email_register]= plan["2"]
                    print("------------------------")
                    print("Ha elegido el plan", plan["2"])
                elif plan_option=="3":
                    select_user[email_register]= plan["3"]
                    print("------------------------")
                    print("Ha elegido el plan", plan["3"])
                else:
                    print("------------------------")
                    print("El plan no se ha elegido")
            elif plan1 == 2:
                plan_option="4"
                gb = int(input("¿Cuántas gigas queres en tu plan?: "))
                time = int(input( "¿Cuántos meses vas a querer tu plan?: "))
                money = gb*500 + time*200
                if gb >=5:
                    print("--------[TU PLAN]--------")
                    plan_own = f"Este plan contiene {gb}GB, durante {time} meses +4GB de regalo!!( ${money} )"
                    print(plan_own)
                    select_user[email_register]=plan_own
                    
                else:
                    print("--------[TU PLAN]--------")
                    plan_own = f"Este plan contiene{gb}GB, durante{time}meses +2GB de regalo!!( {money} )"
                    print(plan_own)
                    select_user[email_register]=plan_own
    elif select==3:
        #Dar de baja al plan
        while True:
            if select_user.__contains__(email_register):
                print("¿Estas seguro que queres dar de baja?(S/N)")
                select_down = input("Elija una opcion: ")
                if select_down.upper()=="S":
                    select_user.pop(email_register)
                    print("---------------------")
                    print("Tu plan se ha dado de baja")
                    break
                elif select_down.upper()=="N":
                    print("---------------------")
                    print("Tu plan no se ha dado de baja. Gracias por seguir en nuestra compañia")
                    break
                else:
                    print("Opcion incorrecta")
    elif select==4:
        #Cerrar programa
        print("---------------------")
        print("Cerrando programa")
        print("---------------------")
    else:
        print("---------------------")
        print("Incorrecto, ingrese un numero correspondiente")