
fecha=input("ingrese la fecha en formato dia, DD/MM: ")
dia_semana = fecha[0:fecha.find(",")]
fecha_dia = int(fecha[fecha.find(" ")+1:fecha.find("/")])
fecha_mes = int(fecha[fecha.find("/")+1:])
check_date = True #PARA CORROBORAR QUE LAS FECHAS SEAN CORRECTAS

if (fecha_dia>31) or (fecha_dia<=0):
    print("Dia inexistente")
    check_date = False
elif(fecha_mes>12) or (fecha_mes<=0):
    print("Mes inexistente")
    check_date = False
elif (dia_semana.lower()=="lunes")or(dia_semana.lower()=="martes") or(dia_semana.lower()=="miercoles")or(dia_semana.lower()=="jueves")or(dia_semana.lower()=="viernes"):
    check_date
else:
    print("Dia incorrecto")
    check_date = False

if check_date:
    print(f"{dia_semana}, {fecha_dia}/{fecha_mes}")
    if (dia_semana.lower()=="lunes")or(dia_semana.lower()=="martes") or(dia_semana.lower()=="miercoles"):
        #
        check_examen = input("Se tomaron exámenes? ")
        if(check_examen.lower() == "si"):
            cant_aprobados = int(input("Cantidad de aprobados: "))
            cant_desaprobados = int(input("Cantidad de desaprobados: "))
            cant_total = cant_aprobados+cant_desaprobados
            #MOSTRAR PORCENTAJE DE APROBADOS
            print(f"El porcentaje de aprobados es: {int((cant_aprobados/cant_total)*100)}%")
    elif dia_semana.lower() =="jueves": #DIA JUEVES
        cant_total = int(input("Cantidad de alumnos: "))
        cant_asistencia = int(input("Asistencia: "))
        #MOSTRAR ASISTENCIA
        asistencia_final = print("Asistió la mayoriía")if int((cant_asistencia/cant_total)*100)>=50 else print("No asistió la mayoria")
    else:
            #DIA VIERNES
        if(fecha_dia==1) and(fecha_mes==1 or fecha_mes==7):
            print("Comienzo de nuevo ciclo!")
            arancel = 1000
            cant_alumnos = int(input("Cantidad de alumnos: "))
            arancel_final = arancel*cant_alumnos
            print(f"Cada alumno paga: ${arancel}") #ARANCEL POR CADA ALUMNO
            print(f"Total: ${arancel_final}") #TOTAL DE ARANCEL