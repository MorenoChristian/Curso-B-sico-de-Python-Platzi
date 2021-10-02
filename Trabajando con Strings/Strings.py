nombre = input("Ingrese su nombre: ")

nombre = nombre.upper() #tranforma a mayuscula
print(nombre)

nombre = nombre.lower() #transforma a minuscula
print(nombre)

nombre = nombre.capitalize() #transforma solamente la primer letra a mayuscula
print(nombre)

nombre = nombre.strip() # borra los espacios de sobras despues del string
print(nombre)

nombre = nombre.replace("i","e") #recibe 2 parametros, reemplaza el primer string de 'nombre' por el segundo string
print(nombre)

letra = nombre[3]
print(letra)

longitud = len(nombre)
print(longitud)

corte = nombre[2:5]
print(corte)

corte2 = nombre[0:8:2] #realiza un corte de 0 a 8 pero de dos en dos
print(corte2)

corte3 = nombre[0::3] #de 0 hasta el final de 3 en 3
print(corte3)

recorrido_inverso = nombre[::-1] 
#Al no haber parámetro en los 2 primeros lugares, se interpreta que 
# se arranca desde el inicio hasta el final, pero en pasos de 1 en 1 
# con la palabra al revés, porque es -1.
print(recorrido_inverso)