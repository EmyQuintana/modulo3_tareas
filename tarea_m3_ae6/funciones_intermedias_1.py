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

#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]

matriz [1][0] = [6]
print ("\nla nueva matriz es:")
print (matriz) 

#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”

cantantes [0][0] =["Enrique Martin Morales"]
print ("\nlista de cantantes corregida:")
for cantantes in cantantes : 
    print(f"nombre:{cantantes["nombre"]}")

#En ciudades, cambia “Cancún” por “Monterrey

ciudades["México"][2] = "Monterrey"
print("\nLista de ciudades corregida:")
for pais, ciudadescorregidas in ciudades.items():
    ciudadescorregidas=", ".join(ciudadescorregidas)
    print(f"{pais}: {ciudadescorregidas}")


#  En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"] = [9.9355431]
print("\nCoordenadas corregidas:")
print (coordenadas)