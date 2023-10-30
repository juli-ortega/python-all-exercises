def return_dni(dni):
    if len(dni)==7 or len(dni)==8:
        return True
    else:
        return False
    
def end_word(phrase):
    words_in_phrase = phrase.split()

    if words_in_phrase:
        end_word_in_phrase = words_in_phrase[-1]
        print(f"La longitud de la ultima palabra es: {len(end_word_in_phrase)}")
    else:
        print("No hay palabras en la frase")


def first_word(name):
    words_in_phrase = name.split()

    if words_in_phrase:
        first_word_in_phrase = words_in_phrase[0]
        return first_word_in_phrase
    else:
        print("No hay palabras en la frase")

def get_num_mult(num1,num2):
    if num2>num1:
        if num2%num1==0:
            return True
        else:
            return False
    elif num1>num2:
        if num1%num2 == 0:
            return True
        else:
            return False

def temp_max_min(max,min):
    medium = (max + min) /2
    return medium
    
def split_letters(phrase):
    new_phrase=""
    for i in range(len(phrase)):
        if phrase[i] == " ":
            continue
        new_phrase += phrase[i]+" "

    return new_phrase

def get_max_min (list_num):
    maxim = max(list_num)
    mini = min(list_num)
    return maxim, mini

import math

def calculate(radio):
    area = math.pi * radio**2
    perimeter =  2 * math.pi * radio

    return area, perimeter

def login(user,password,attemps):
    if user == "Usuario1" and password == "asdasd":
        return True
    else:
        attemps[0] +=1
        return False

def discount_prices(prices_discounts):
    discounts = 0
    for i in prices_discounts:
        discounts = i * (prices_discounts[i]/100)
        prices_discounts[i] = i-discounts
    
    return prices_discounts

def mult_elements(list_add):
    new_list = []
    for i in list_add:
        new_list.append(mult_list(i))
    
    return new_list

def mult_list(element):
    return element * 2

def new_dict_for_phrase(phrase):
    new_dictio_with_words = {}
    words_in_phrase = phrase.split()
    for i in range(len(words_in_phrase)):
        new_dictio_with_words[words_in_phrase[i]] = len(words_in_phrase[i])

    return new_dictio_with_words 

def module_of_vec(amount):
    add = 0
    for i in range(amount):
        poten = 0
        elements = float(input(f"Ingrese el vector {i+1}: "))
        poten = elements**2 
        add+=poten
    
    vector = math.sqrt(add)

    return vector

def is_cousin(number):
    if number == 0:
        return False
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    condition = True
    for i in range(5, int(number**0.5) + 1, 6):
        if number % i == 0 or number % (i + 2) == 0:
            condition = False
            break
    if condition == True:
        return True
    
def factorial(i):
    multiplication = 1
    if i == 0:
        return 1
    for j in range(1,i+1):
        multiplication *= j
    if i ==0:
        return 0
    return multiplication

def search_digit(num,digit):
    count = 0
    for i in str(num):
        if i == digit:
            count +=1
    return count

def add_digits(numbers):
    add = 0
    while numbers > 0:
        digit = numbers % 10  
        add += digit  
        numbers //= 10
    return add
    
#Trabajo Practico Numero 6

def count_of_names_repeat(list_for_repeat):
    count = {}

    for i in list_for_repeat:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    
    return count

def lower_list ( list_receive):
    k = 0
    for i in list_receive:
        list_receive[k] = i.lower()
        k+=1
    return list_receive
    
#Trabajo Practico Numero 7

def order_library(list_of_dictio):
    return sorted(list_of_dictio, key=lambda x: x.get("Año de Publicación"))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(key) < len(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def insertion_sort_ints(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def order_strings_for_alpha(list_to_order):
    return sorted(list_to_order)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambia los elementos
                swapped = True
        if not swapped:
            break

    return arr
        
