def primo(numero):
    cont = 0

    for i in range(1, numero+1):
        if numero % i == 0:
            cont = cont + 1
        
    if cont == 2:
        es_primo = True
        return es_primo
    else:
        es_primo = False
        return es_primo

num = int(input("Ingrese el numero: "))

resu = primo(num)

if resu == True:
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num} no es primo")