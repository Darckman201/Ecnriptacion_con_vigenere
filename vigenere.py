mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
minusculas = "abcdefghijklmnñopqrstuvw "

def cifrar(cadena, llave):
    texto_cifrado = ''
    i = 0
    for letra in cadena:
        if (letra.isupper()):
            s = mayusculas.find(letra) + mayusculas.find(llave[i % len(llave)])
            modulo = int(s) % len(mayusculas)
            texto_cifrado = texto_cifrado + str(mayusculas[modulo])
        else:
            s = minusculas.find(letra) + minusculas.find(llave[i % len(llave)])
            modulo = int(s) % len(minusculas)
            texto_cifrado = texto_cifrado + str(minusculas[modulo])
        i = i + 1
    return texto_cifrado

def descifrar(cadena, llave):
    texto_descifrado = ''
    i = 0
    for letra in cadena:
        if (letra.isupper()):
            s = mayusculas.find(letra) - mayusculas.find(llave[i % len(llave)])
            modulo = int(s) % len(mayusculas)
            texto_descifrado = texto_descifrado + str(mayusculas[modulo])
        else:
            s = minusculas.find(letra) - minusculas.find(llave[i % len(llave)])
            modulo = int(s) % len(minusculas)
            texto_descifrado = texto_descifrado + str(minusculas[modulo])
        i = i + 1
    return texto_descifrado

def main():
    cadena = input("El texto en plano a cifrar es: ")
    llave = input("La palabra clave a cifrar es :")
    print ("El texto cifrado resultante es: " + cifrar(cadena, llave))

    cadena = input("El texto cifrado a descifrar es: ")
    llave = input("La palabra clave para descifrar es: ")
    print ("El texto original es: " + descifrar(cadena, llave))

if __name__ == "__main__":
    main()