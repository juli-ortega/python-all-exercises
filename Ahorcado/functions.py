def sumar_digitos(num):
    if num%10==num:
        return num
    else:
        return num%10 + sumar_digitos(num//10)
def show_hidden_word(word, empty_word, attempts):
    """_summary_

    Args:
        word (str): palabra completa
        empty_word (list): lista de "_" a completar
        attempts (list): lista de intentos

    Returns:
        list: empty_word actualizado, si se actualizó 
    """
    for i in attempts: 
        if i in word.lower():
            for j in range(len(word)):
                if i == word[j].lower():
                    empty_word[j] = i
    return empty_word