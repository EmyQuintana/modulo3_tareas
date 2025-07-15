matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

coordenadas= [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]

#Iterar a través de una lista de diccionarios Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y 
# recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente


def iterarDiccionario(lista):
     for cantante in lista:
        nombre_cantante = cantante["nombre"]
        pais_cantante = cantante["pais"]
        print(f"\nnombre - {nombre_cantante}, pais - {pais_cantante}")
iterarDiccionario(cantantes)


def iterarDiccionario(lista):
     for coordenadas in lista:
        valor_latitud = coordenadas ["latitud"]
        valor_longitud = coordenadas["longitud"]
        print(f"\nlatitud - {valor_latitud}, longitud - {valor_longitud}")
iterarDiccionario(coordenadas)
