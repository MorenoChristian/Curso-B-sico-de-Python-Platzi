import random #necesario para poder utilizar la funcion random()

numero_adivinar = random.randint(1, 100)

numero = int(input("Adivine el numero que estoy pensando: "))

while numero_adivinar != numero:
    if numero_adivinar > numero:
        numero = int(input("Incorrecto, ingrese un numero mayor: "))
        continue
    
    elif numero_adivinar < numero:
        numero = int(input("Incorrecto, ingrese un numero menor: "))
        continue

else:
    print("Acertaste!!")