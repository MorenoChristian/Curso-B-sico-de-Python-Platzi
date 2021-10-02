# ''' en las listas se puede poner cualquier tipo de variable, podemos agregar y eliminar datos dentro de la misma
#     con append y pop respectivamente
# '''

# lista = [1, 5, "Hola", 4.5, "Mundo", True]
# print(lista)

# lista.append(99)
# print(lista)

# lista.pop(1) #en este caso se coloca el indice del elemento a borrar
# print(lista)

# print(lista[1]+" "+lista[3]) #juego a concatenar los dos strings de la lista

# print("Aca recorremos toda la lista")
# for elementos in (lista):
#     print(elementos, end = " ")
# print("\n")


# print("Aca recorremos toda la lista AL REVEZ")
# for elementos in reversed(lista):
#     print(elementos, end = " ")
# print("\n")

# ## Concatenar dos o mas lista
# print("Concatenamiento de lista")
# a = [1,2]
# b = [3,4]
# print(a+b)

# ##Multiplicacion * Repite la misma lista
# print("Multiplicacion de lista")
# print(a*2)

# ## Ordenar lista de menor a mayor, esto modifica la lista inicial
# print("Ordenamiento de lista")
# c = ["b","t","p","a"]
# c.sort()
# print(c)

# ## Ordenar lista de mayor a menor, esto modifica la lista inicial
# print("Ordenamiento de lista")
# c = ["b","t","p","a"]
# c.reverse()
# print(c)

# ## Tamaño de la lista
# print("Tamaño de la lista")
# print(len(c))


# frutas = ["naranja", "manzana", "pera", "coco", "limon", "frutilla"]

# famosos = {"Mirtha Legrand", "Marcelo Tinelli", "Viviana Canosa"}
# edades = [18,20,15,65,34,21]
# sexos = ["mujer","hombre","mujer"]

# for i,fruta in enumerate(frutas): #nos permite recorrer la lista e ir enumerandola
#     print(f"En la posicion {i}, esa la fruta: {fruta}")

# for famoso,edad,sexo in zip(famosos,edades,sexos): #zip nos permite recorrer las lista que le pongamos a la vez
#     print(f"El {famoso} tiene {edad} años de edad y de sexo {sexo}")


colores = ["azul", "rojo", "verde", "amarillo"]
print("Lista colores antes de agregar: ",colores)
mono = ["Blanco","negro"]
#colores.insert(2,"blanco") #utilizamos insert para insertar un elemento en cierta posicion
colores.extend(mono) #agregamos varios elementos a la lista con extend
del colores[0:2] #eliminamos los elementos desde un inicio a un final
print("Lista despues de agregar: ",colores)

vocales = ["a","e","i","o","u"]
contar_vocales = vocales.count("i")
print("Cantidad de veces que aparece i: ",contar_vocales)

palabra = "Hola, que tal estas mi estimado?"
print("cantidad de i: ",palabra.count("e"))