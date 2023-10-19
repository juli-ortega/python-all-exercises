def sumar_digitos(num):
    if num%10==num:
        return num
    else:
        return num%10 + sumar_digitos(num//10)

            

