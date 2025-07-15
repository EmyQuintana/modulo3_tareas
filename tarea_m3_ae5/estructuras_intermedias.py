matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]


ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}


coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

# 1. Cambia el valor 3 en matriz por 6.

matriz[1][0] = 6

# 2. Cambia el nombre del primer cantante por "Enrique Martin Morales".

cantantes[0]["nombre"] = "Enrique Martin Morales"

# 3. En el diccionario ciudades, reemplaza "Cancún" por "Monterrey".

indice_cancun = ciudades["México"].index("Cancún")
ciudades["México"][indice_cancun] = "Monterrey"

# 4. En la lista coordenadas, cambia el valor de "latitud" por 9.9355431.
coordenadas[0]["latitud"] = 9.9355431

# Imprimiendo los cambios 
print("- Matriz actualizada -")
print(matriz)

print("\n-Cantantes actualizados-")
print(cantantes)

print("\n-Ciudades actualizadas-")
print(ciudades)

print("\n-Coordenadas actualizadas-")
print(coordenadas)


print("\nLista de Cantantes:")
# Recorremos cada diccionario en la lista 'cantantes'
for cantante in cantantes:
    # Accedemos al nombre y país de cada cantante
    nombre = cantante["nombre"]
    pais = cantante["pais"]
    
    # Imprimimos la información 
    print(f"nombre - {nombre}, pais - {pais}")


# ---
## Obteniendo todos los Nombres
print("\nNombres de los cantantes:")
for cantante in cantantes:
    print(cantante["nombre"])

# ---
## Obteniendo todos los Países
print("\nPaíses de origen de los cantantes:")
for cantante in cantantes:
    print(cantante["pais"])

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

print("\nInformación de Costa Rica:")

# Recorremos el diccionario usando .items() para obtener la clave y el valor
for clave, lista_valores in costa_rica.items():
    # Obtenemos la cantidad de elementos en la lista usando len()
    cantidad = len(lista_valores)
    
    # Convertimos la clave a mayúsculas usando .upper()
    clave_mayusculas = clave.upper()
    
    # Imprimimos el resultado con el formato solicitado
    print(f"La cantidad de elementos en {clave_mayusculas} es: {cantidad}")



#Cada elemento de la lista correspondiente, en líneas separadas.
# Recorremos el diccionario 
for clave, lista_valores in costa_rica.items():
    # Convertimos a mayúsculas 
    clave_mayusculas = clave.upper()
    print(f"\n--- {clave_mayusculas} ---") 

    # Recorremos cada elemento 
    for elemento in lista_valores:
        print(f"- {elemento}") # Imprimimos cada elemento con un guion para que se vea como una lista

