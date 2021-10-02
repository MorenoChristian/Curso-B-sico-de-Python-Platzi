


menu = """
Bienvenido al conversor de monedas

1- Pesos Colombianos ❤
2- Pesos Argentinos 💋
3- Pesos Mexicanos 😊

Elige una opcion: """

opcion = int(input(menu))

def conversion_dolar(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos+ " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

if(opcion == 1):
    conversion_dolar("Colombianos", 3874)
elif opcion == 2:
    conversion_dolar("Argentinos", 180)
elif opcion == 3:
    conversion_dolar("Mexicanos", 24)
else:
    print("Ingresa una opcion conrrecta porfavor")