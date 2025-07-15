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
#Obtener valores de una lista de diccionarios Crea la función iterarDiccionario2(llave, lista) 
# que reciba una cadena con el nombre de una llave y una lista de diccionarios. 
# La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista.

def iterarDiccionario2(llave, lista_de_diccionarios):
    for diccionario_actual in lista_de_diccionarios:
        
        if llave in diccionario_actual:
            
            print(diccionario_actual[llave])
        else:
            # Si no la tiene, te aviso
            print(f"\nLa etiqueta '{llave}' no existe en una de las cajas.")

iterarDiccionario2("nombre", cantantes)  
iterarDiccionario2("pais", cantantes)
iterarDiccionario2("latitud",coordenadas)