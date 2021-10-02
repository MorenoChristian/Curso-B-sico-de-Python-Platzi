def palindromo(palabra):
    palabra = palabra.replace(" ","") # reemplazo todos los espacios por nada, eliminamos los espacios de sobra
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1] #va a recorrer de atras hacia adelante, y lo guarda en la nueva variable
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

if __name__ == "__main__":
    run()