# opcion = input("Ingrese la opcion (1,2,3): ")

# if(opcion == "1"):
#     print("Hola!!!")
#     print("Como te encuentras?")
#     print("Elegiste la opcion 1")
#     print("Adios")
# elif(opcion == "2"):
#     print("Hola!!!")
#     print("Como te encuentras?")
#     print("Elegiste la opcion 2")
#     print("Adios")
# elif(opcion == "3"):
#     print("Hola!!!")
#     print("Como te encuentras?")
#     print("Elegiste la opcion 3")
#     print("Adios")

def conversacion(mensaje):
    print("Hola!!")
    print("Come te encuentras?")
    print(mensaje)
    print("Adios")

opcion = input("Ingrese la opcion (1,2,3): ")

if(opcion == "1"):
    conversacion("Elegiste la opcion 1")
elif(opcion == "2"):
    conversacion("Elegiste la opcion 2")
elif(opcion == "3"):
    conversacion("Elegiste la opcion 3")

def suma(a,b):
    resultado = a + b
    return resultado

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

sumatoria = suma(numero1,numero2)

print(sumatoria)