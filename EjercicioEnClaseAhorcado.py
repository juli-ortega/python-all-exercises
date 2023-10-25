import random
from functions import show_hidden_word
word_collections = [
    "programacion",
    "tecnologia",
    "Python",
    "algoritmo",
    "desarrollo",
    "informatica",
    "compilador",
    "codigo",
    "lenguaje",
    "web",
    "base de datos",
    "repositorio",
    "seguridad",
    "redes",
    "hardware",
    "software",
    "aplicacion",
    "API",
    "frontend",
    "backend",
]
selected_word = random.choice(word_collections) #se selecciona una palabra aleatoria
print("Bienvenido al juego del ahorcado!!\n")
empty_word = []
attempts = []
for i in selected_word:
    empty_word.append("_") #contrstruye la empty word
tries = 10
while tries > 0:
    print(f"Intentos restantes: {tries}\n")
    print("Estado actual de la palabra:\n")
    empty_word = show_hidden_word(selected_word, empty_word, attempts) #llama a la funcion para mostrar la palabra actualizada
    for i in empty_word:
        print(i, end= " ")
    print("\n")
    while True:
        guess = input("\nIngrese una letra: ")
        if len(guess)!= 1: #revisa que sea de len 1
            print("Ingresa solo una letra!!!\n")
            continue
        else:
            attempts.append(guess.lower())
            break
    if guess.lower() in selected_word.lower():
        print("\nHas acertado la letra!!!\n")
        empty_word = show_hidden_word(selected_word, empty_word, attempts) # lo llama de vuelta para hacer la condición de salida
        for i in empty_word:
            if i not in selected_word:
                break
        else:
            for i in empty_word: #muestra la palabra de vuelta para mostrarla completa
                print(i, end= " ")
            print("\n")
            print("Has ganado!!!\n")
            exit()
        continue
    else:
        tries -= 1
        print("\nNO has acertado la letra!!!\n")
        continue
print("\nTe ahorcaron!!!")

