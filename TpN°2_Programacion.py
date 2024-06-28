'''1-	Crear un programa que reciba el número de años que tiene nuestra 
computadora y muestre en la consola que el computador es nuevo
 si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.'''

print("Ejercicio 1")
numbers_computer = int(input("Ingrese el numero de años de su PC: "))
if numbers_computer>2:
    print("El computador ya es viejo")
else:
    print("El conputador es nuevo")

'''2-	Hacer que el programa anterior muestre 
un mensaje de error si el usuario digita un número negativo.'''
print("------------")
print("Ejercicio 2")
numbers_computer = int(input("Ingrese el numero de años de su PC: "))
if numbers_computer>2:
    print("El computador ya es viejo")
elif numbers_computer<0:
    print("Error el año no puede ser negativo")
else:
    print("El conputador es nuevo")

'''3-	Solicitar al usuario que ingrese los nombres de dos personas,
los cuales se almacenarán en dos variables.
A continuación. Imprimir "coincidencia" si ambos nombres comienzan con la misma letra.
Si no es así, imprimir "no hay coincidencia".'''
print("------------")
print("Ejercicio 3")
name1 = input("Ingrese el nombre de la primer persona: ")
name2 = input("Ingrese el nombre de la segunda persona: ")
if name1.upper()[0] == name2.upper()[0]:
    print("Coincidencia")
else:
    print("No hay coincidencia")

'''
4-	Crear un programa que permita al usuario elegir un candidato por el cual votar.
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad,
candidato C por el partido azul.'''
print("------------")
print("Ejercicio 4")
print("Cadidatos a votar: (A) PARTIDO ROJO, (B) PARTIDO VERDE, (C) PARTIDO AZUL")
choice = input()
if choice.upper() == "A":
    print("Usted a elegido al PARTIDO ROJO")
elif choice.upper() == "B":
    print("Usted a elegido al PARTIDO VERDE")
elif choice.upper() == "C":
    print("Usted a elegido al PARTIDO VERDE")
else:
    print("Usted no ha elegido a ningun candidato")

'''5-	Escribir un programa que solicite al usuario una letra, si es una vocal,
 mostrar el mensaje "Es vocal".Se debe validar que el usuario ingrese sólo un carácter. 
 Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.'''
print("------------")
print("Ejercicio 5")
letter = input("Ingrese una letra: ")
if len(letter) > 1:
    print("No se puede procesar el dato")
elif letter.upper() == 'A':
    print("Es una vocal")
elif letter.upper() == 'E':
    print("Es una vocal")
elif letter.upper() == 'I':
    print("Es una vocal")
elif letter.upper() == 'O':
    print("Es una vocal")
elif letter.upper() == 'U':
    print("Es una vocal")
else:
    print("No es una vocal")

'''6-	Hacer un programa que permita saber si un año es bisiesto. 
Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100,
excepto que también sea divisible por 400.'''
print("------------")
print("Ejercicio 6")
year = int(input("Ingrese un año: "))
if year%4==0 and year%100 !=0:
    print("Es un año bisiesto")
elif year%4==0 and year%100 ==0 and year%400==0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")

'''7-	Escribí un programa para solicitar al usuario tres números
y mostrar en pantalla al menor de los tres.'''
print("------------")
print("Ejercicio 7")
num1= int(input("Ingrese el numero 1: "))
num_lesser = num1
num2= int(input("Ingrese el numero 2: "))
if num_lesser>num2:
    num_lesser = num2
num3= int(input("Ingrese el numero 3: "))
if num_lesser>num3:
    num_lesser=num3
print(f"El menor es: {num_lesser}")

'''8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. 
Si el nombre es “Gwenevere” y la contraseña es “excalibur”, 
mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. 
Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.'''
print("------------")
print("Ejercicio 8")
user = input("Ingrese el usuario: ")
password = input("Ingrese la contraseña: ")

if user == "Gwenevere" and password=="excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso Denegado")

'''9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y 
el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los 
hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el 
grupo que le corresponde.'''
print("------------")
print("Ejercicio 9")
user_name = input("Ingrese su nombre: ")
sex = input("Ingrese su sexo: (M) Masculino o (F) Femenino: ")
user_name = user_name.upper()
sex = sex.upper()

if (sex == "M" and user_name >"N") or (sex == "F" and user_name < "M"):
    print("Corresponde: Grupo A")
else:
    print("Corresponde: Grupo B")

'''10-	Escribir un programa para una empresa que tiene salas de juegos para todas las 
edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por 
entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la 
entrada. Si el cliente es menor de 4 años puede entrar gratis, 
si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.'''
print("------------")
print("Ejercicio 10")
age = int(input("Ingrese su edad: "))

if age<4 and age>=0:
    print("La entrada es gratis")
elif age>=4 and age<19:
    print("La entrada cuesta: $500")
elif age>=19:
    print("La entrad cuesta: $1.000")
else:
    print("Error, edad incorrecta")

'''11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.
•	Ingredientes vegetarianos: Pimiento y tofu.
•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en 
función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas 
la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y 
todos los ingredientes que lleva.'''
print("------------")
print("Ejercicio 11")

choice = input("Ingrese (1) Vegeteriano o (2) No vegetariano: ")
if choice == "1":
    choice_ingredients = input("Elige: (1) Pimiento, (2) Tofu : ")
    if choice_ingredients == "1":
        pizza = "La pizza es vegetariana con mozzarella, tomate y pimiento."
    elif choice_ingredients == "2":
        pizza = "La pizza es vegetariana con mozzarella, tomate y tofu."
    else:
        print("NUMERO INCORRECTO")
elif choice == "2":
    choice_ingredients = input("Elige: (1) Peperoni, (2) Jamon, (3) Salmon : ")
    if choice_ingredients == "1":
        pizza = "La pizza es no esvegetariana con mozzarella, tomate y peperoni."
    elif choice_ingredients == "2": 
        pizza = "La pizza es no es vegetariana con mozzarella, tomate y jamon."
    elif choice_ingredients == "3":
        pizza = "La pizza es no es vegetariana con mozzarella, tomate y salmon."
    else:
        print("NUMERO INCORRECTO")
else:
    print("NUMERO INCORRECTO")

print(pizza)

'''12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos
años han pasado desde ese año o cuántos años faltan para llegar a ese año.'''
print("------------")
print("Ejercicio 12")

year = int(input("Año actual: "))
year_2 = int(input("Cualquier año: "))

if year==year_2:
    print("Estas en el mismo año")
elif year>year_2:
    different = year - year_2
    print(f"Han pasado {different} años desde {year_2}")
elif year<year_2:
    different = year_2 - year
    print(f"Faltan {different} años para llegar a {year_2}")

'''13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es 
múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o 
nulos.'''
print("------------")
print("Ejercicio 13")
num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
if num1<=0 or num2<=0:
    print("Ha ingresado un numero nulo o un numero negativo. Por favor, vuelva a intentarlo.")
elif num1==num2:
    print("Los numero son iguales.")
elif num1>num2:
    if num1%num2==0:
        print(f"El numero {num1} es multiplo de {num2} ")
    else:
        print(f"El numero {num1} es no es multiplo de {num2} ")
elif num2>num1:
    if num2%num1==0:
        print(f"El numero {num2} es multiplo de {num1} ")
    else:
        print(f"El numero {num2} es no es multiplo de {num1} ")

'''14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado 
(ax + b = 0) y escriba la solución.Se recuerda que una ecuación de primer grado puede no 
tener solución, tener una solución única, o que todos los números sean solución. 
Se recuerda que la fórmula de las soluciones es x = -b / a '''
print("------------")
print("Ejercicio 14")
coefficient1 = float(input("Ingrese el coeficiente a = "))
coefficient2 = float(input("Ingrese el coeficiente b = "))

if coefficient1==0:
    if coefficient2 == 0:
        print("La ecuacion tiene soluciones infinitas")
    else:
        print("La ecuacion no tiene solucion")
else:
    x = -(coefficient2) / coefficient1
    print(f"La ecuacion tiene una unica solucion y es: x = {x}")

'''15-	Escriba un programa que pregunte primero si se quiere calcular el área de un 
triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo 
(escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el 
área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el 
programa tiene que pedir entonces el radio y escribir el área.'''
print("------------")
print("Ejercicio 15")
choice_t_or_c = input("Desea calcular el area de un (T) Triangulo o (C) Circulo: ")

choice_t_or_c = choice_t_or_c.upper()
import math
if choice_t_or_c == "T":
    base = float(input("Ingrese la base: "))
    high = float(input("Ingrese la altura: "))

    area = base * high /2

    print(f"El area del traingulo es: {area}")

elif choice_t_or_c =="C":
    radio = float(input("Ingrese el radio: "))

    area = math.pi * (radio ** 2)

    print(f"El area del circulo es: {area}")
else:
    print("LETRA INCORRECTA")

'''16-	Haz una calculadora básica pida al usuario dos valores, a y b.
Según la opción que desean, realizar la operación:
•	Si operación es 1 entonces debemos ver el resultado de a + b
•	Si operación es 2 entonces debemos ver el resultado de a * b
•	Si operación es 3 entonces debemos ver el resultado de a - b
•	Si operación es 4 entonces debemos ver el resultado de a / b'''
print("------------")
print("Ejercicio 16")
a = int(input("Ingrese el numero a: "))
b = int(input("Ingrese el numero b: "))

operation = input("Ingrese la operacion que desea realizar:\n(1) Suma\n(2) Multiplicacion\n(3) Resta\n(4) Division\nElige: ")

if operation == "1":
    print(f"{a} + {b} = {a+b}")
elif operation == "2":
    print(f"{a} x {b} = {a*b}") 
elif operation == "3":
    print(f"{a} - {b} = {a-b}") 
elif operation == "4":
    print(f"{a} / {b} = {a/b}") 
else:
    print("NUMERO INCORRECTO")

'''17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es 
lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. 
Si el día ingresado no es ninguno de esos, imprimir otro mensaje.'''
print("------------")
print("Ejercicio 17")
week_day = input("Ingrese un dia de la semana: ")

week_day = week_day.lower()

if week_day =="lunes":
    print("El dia ingresado es lunes")
elif week_day =="viernes":
    print("EL dia es viernes")
elif week_day =="sabado" or week_day =="domingo":
    print("Es fin de semana :)")
elif week_day == "martes" or week_day == "miercoles" or week_day == "jueves":
    print("Estamos entre semana, que aburrido.")
else:
    print("DIA INCORRECTO")

'''18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, 
si trabajó horas extras y mostrar esta cantidad. Mostrar su salario total, tomando en cuenta 
que las horas extras serán pagadas un 10% más que las horas laborales comunes.'''
print("------------")
print("Ejercicio 18")
month_hours = float(input("Ingrese la cantidad de horas trabajadas en el mes: "))
salary = float(input("Ingrese el salario por hora: "))

if month_hours > 48:
    print(f"Has trabajado {month_hours-48} horas extras")
    print(f"Tu salario es de ${salary * 48 + salary * (month_hours - 48) + month_hours*salary * 0.10}")
elif month_hours<=48:
    print(f"Tu salario es de ${month_hours*salary}")
elif month_hours<=0:
    print("HORAS INCORRECTAS")

'''19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 
1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de 
$60; de lo contrario no hay descuento.'''
print("------------")
print("Ejercicio 19")
pencils = int(input("Ingrese la cantidad de lapices: "))

if pencils>1000:
    discount = pencils * 60 * 0.07
    print(f"Descuento del 7% = {discount}")
    print(f"El total es: ${pencils*60 - discount}")
elif pencils<=1000:
    print(f"El total es: ${pencils*60}")
elif pencils <=0:
    print("CANTIDAD DE LAPICES INCORRECTO")

'''20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su 
promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.'''
print("------------")
print("Ejercicio 20")
note1 = int(input("Ingrese la nota 1: "))
note2 = int(input("Ingrese la nota 2: "))
note3 = int(input("Ingrese la nota 3: "))
note4 = int(input("Ingrese la nota 4: "))

average = (note1 + note2 + note3 + note4) / 4

if average >= 6:
    print("Aprobado")
elif average<6:
    print("Desaprobado")