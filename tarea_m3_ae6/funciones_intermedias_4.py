costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}


ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}


def imprimirInformacion(diccionario):
    for clave, lista_valores in diccionario.items():
        print(f"{clave}: {len(lista_valores)}")
        for valor in lista_valores:
         print(valor)


imprimirInformacion(costa_rica)

#ejemplo 2
imprimirInformacion(ciudades)




