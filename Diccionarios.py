def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    poblacion_paises = {
        "Argentina" : 40234658,
        "Brasil" : 70548621,
        "Chile" : 526351485,
    }
    # print(poblacion_paises["Chile"])

    print("Imprimo las llaves")
    for pais in poblacion_paises.keys():
        print(pais)

    print("Imprimo los valosres de las llaves")
    for pais in poblacion_paises.values():
        print(pais)

    print("Imprimimos las llaves y valores")
    for pais, poblacion in poblacion_paises.items(): #lleva dos variables para almacenar las llaves y los valores
        print(pais + " tiene " + str(poblacion)+ " habitantes")

    longitud = len(mi_diccionario)
    print(longitud)

if __name__ == "__main__":
    run()