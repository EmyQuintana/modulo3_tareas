#Crear un programa en Python que determine el descuento aplicado a una compra según los siguientes criterios:
#Si el cliente compra más de 10 productos, obtiene un descuento del 10%.
#Si el cliente es frecuente (más de 5 compras previas), se aplica un 5% adicional.
#Si la compra supera los 500 dólares, se otorga un descuento adicional del 7%.
#En días de promoción especial, se aplica un 15% adicional.
#Ningún cliente puede obtener un descuento mayor al 30% en total.

import datetime

# --- Lista de Productos Dermocosméticos con Precios ---
productos_dermocosmetica = [
    {"nombre": "Jabon rostro", "precio": 15.50},
    {"nombre": "Agua micelar", "precio": 12.00},
    {"nombre": "Tonico", "precio": 18.75},
    {"nombre": "Serum hidratante", "precio": 35.00},
    {"nombre": "Serum antiedad", "precio": 45.00},
    {"nombre": "Serum anti imperfecciones", "precio": 38.00},
    {"nombre": "Serum VitC", "precio": 40.00},
    {"nombre": "Serum antimanchas", "precio": 42.50},
    {"nombre": "Exfoliante fisico", "precio": 22.00},
    {"nombre": "Acido glicolico", "precio": 28.00},
    {"nombre": "Exfoliante quimico", "precio": 30.00},
    {"nombre": "Crema hidratante", "precio": 25.00},
    {"nombre": "Crema humectante", "precio": 27.00},
    {"nombre": "Crema antiedad", "precio": 48.00},
    {"nombre": "Protector solar", "precio": 32.00},
    {"nombre": "Contorno de ojos", "precio": 20.00},
]

# Los días de la semana se representan con números: Lunes=0, Martes=1, Miércoles=2, jueves=3, viernes=4, sabado=5, domingo=6
DIAS_DE_PROMOCION = [0, 2, 6] # Ejemplo: Lunes (0), Miercoles (4) y domingo () son días de promoción


print("\n¡Bienvenido/a a nuestra tienda de Dermocosmética Emy! ---")

# --- Inicio de la Compra: Solicitud de RUT y Cliente Frecuente ---
rut_cliente = input("\nPor favor, ingresa el RUT del cliente (ej. 12345678-9): ").strip()
print(f"RUT ingresado: {rut_cliente}")

es_cliente_frecuente = False #inciando en false, por principio de precaución 
while True:
    respuesta_frecuente = input("¿Es un cliente frecuente con más de 5 compras previas)? (sí/no): ").lower().strip()
    if respuesta_frecuente == 'si' or respuesta_frecuente == 'sí':
        es_cliente_frecuente = True
        break
    elif respuesta_frecuente == 'no':
        es_cliente_frecuente = False
        break
    else:
        print("Respuesta no válida. Por favor, responde 'sí' o 'no'.")

# Variables para acumular la compra
total_productos_seleccionados = 0
monto_total_compra = 0.0
carrito_compras = {} # Diccionario para almacenar productos y cantidades seleccionadas

# --- Selección de Productos ---

# Muestra la lista de productos SOLO UNA VEZ al principio
print("\n--- Lista de Productos Disponibles ---")
for i in range(len(productos_dermocosmetica)):
    producto = productos_dermocosmetica[i]
    print(f"{i + 1}. {producto['nombre']} - ${producto['precio']:.2f}")
print("------------------------------------------")
print("\nPara finalizar tu selección, ingresa '0'.")
print("También puedes ingresar el nombre del producto.")


while True:
    try: #protegerme el programa de errores inesperados y avisarle al usuario que lo vuelva a intentar
        opcion = input("Ingresa el número o nombre del producto a añadir (o 0 para finalizar): ").strip()

        if opcion == '0':
            break # Sale del bucle de selección de productos

        producto_elegido = None
        cantidad = 0

        # Intentar buscar por número
        if opcion.isdigit(): #para diferenets tipos de ingreso de datos, aqui pueden ser numeros o palabras (nombre del producto)
            num_producto = int(opcion)
            if 1 <= num_producto <= len(productos_dermocosmetica):
                producto_elegido = productos_dermocosmetica[num_producto - 1] #se resta 1 porque mi listado empieza en 1 y no en 0 como cuenta python
            else:
                print("⚠️ Número de producto no válido. Por favor, ingresa un número de la lista.")
                continue
        else: # Intentar buscar por nombre (ignorando mayúsculas/minúsculas)
            nombre_buscado = opcion.lower()
            for p in productos_dermocosmetica:
                if p['nombre'].lower() == nombre_buscado:
                    producto_elegido = p
                    break
            if producto_elegido is None:
                print(f"⚠️ El producto '{opcion}' no se encontró. Por favor, revisa el nombre o usa el número.")
                continue

        # Si se encontró un producto válido, pedir la cantidad
        if producto_elegido:
            cantidad_str = input(f"¿Cuántas unidades de '{producto_elegido['nombre']}' deseas añadir? ")
            cantidad = int(cantidad_str)

            if cantidad <= 0:
                print("La cantidad debe ser un número positivo. Por favor, intenta de nuevo.")
                continue

            # Añadir al carrito y actualizar totales
            if producto_elegido['nombre'] in carrito_compras:
                carrito_compras[producto_elegido['nombre']]['cantidad'] += cantidad
            else:
                carrito_compras[producto_elegido['nombre']] = {
                    'precio': producto_elegido['precio'],
                    'cantidad': cantidad
                }

            total_productos_seleccionados += cantidad
            monto_total_compra += producto_elegido['precio'] * cantidad
            
            print(f"✅ '{producto_elegido['nombre']}' (x{cantidad}) añadido/s a tu carrito.")
            print(f"🛒 **Total de productos en carrito: {total_productos_seleccionados}**")
            print(f"💰 **Monto provisional de la compra: ${monto_total_compra:.2f}**")

    except ValueError:
        print("❌ Entrada inválida. Por favor, ingresa un número entero para la selección/cantidad, o el nombre del producto.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- Fin de la Selección de Productos ---

if total_productos_seleccionados == 0:
    print("\nNo seleccionaste ningún producto. La compra ha finalizado sin descuento.")
else:
    # --- Resumen de Productos Añadidos ---
    print("\n--- Tu Carrito de Compras ---")
    if not carrito_compras:
        print("El carrito está vacío.") # Esto no debería ocurrir si total_productos_seleccionados > 0
    else:
        for nombre_prod, detalles in carrito_compras.items():
            print(f"- {nombre_prod} x {detalles['cantidad']} = ${detalles['precio'] * detalles['cantidad']:.2f}")
    print("----------------------------")

    # --- Obtener la fecha actual para el día de promoción ---
    fecha_actual_compra = datetime.date.today()
    # Mapeo de números de día a nombres de día
    nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    nombre_dia_actual = nombres_dias[fecha_actual_compra.weekday()]
    
    print(f"\nLa fecha actual de la compra es: {fecha_actual_compra} ({nombre_dia_actual})")

    # Determinar si es un día de promoción especial
    es_dia_promocion = (fecha_actual_compra.weekday() in DIAS_DE_PROMOCION)
    if es_dia_promocion:
        dias_promo_nombres = [nombres_dias[d] for d in DIAS_DE_PROMOCION]
        print(f"🎉 ¡Hoy es un día de promoción especial! ({', '.join(dias_promo_nombres)})")

    # --- Cálculo del Descuento (todas las condiciones aquí) ---
    descuento_base = 0.0

    # 1. Descuento por cantidad de productos
    if total_productos_seleccionados > 10:
        print("✅ Aplicando 10% de descuento por más de 10 productos.")
        descuento_base += 10

    # 2. Descuento adicional por cliente frecuente (se usa la variable definida al inicio)
    if es_cliente_frecuente:
        print("✅ Aplicando 5% de descuento adicional por cliente frecuente.")
        descuento_base += 5

    # 3. Descuento adicional por monto de compra
    if monto_total_compra > 500:
        print("✅ Aplicando 7% de descuento adicional por compra superior a $500.")
        descuento_base += 7

    # 4. Descuento adicional por día de promoción
    if es_dia_promocion:
        print("✅ Aplicando 15% de descuento adicional por día de promoción especial.")
        descuento_base += 15

    # 5. Límite máximo de descuento
    if descuento_base > 30:
        descuento_final = 30.0
        print(f"⚠️ El descuento total superó el 30%, se ha limitado al 30%.")
    else:
        descuento_final = descuento_base

    # --- Mostrar Resultados Finales ---
    print("\n--- Resumen Final de la Compra ---")
    print(f"RUT del cliente: {rut_cliente}") # Mostrar el RUT al final
    print(f"Cantidad total de productos: {total_productos_seleccionados}")
    print(f"Monto total de la compra: ${monto_total_compra:.2f}")
    print(f"¿Cliente frecuente?: {'Sí' if es_cliente_frecuente else 'No'}")
    print(f"¿Día de promoción especial?: {'Sí' if es_dia_promocion else 'No'}")
    print(f"\n**¡Felicitaciones! El descuento aplicado es del: {descuento_final:.2f}%**")
    
    monto_con_descuento = monto_total_compra * (1 - descuento_final / 100)
    print(f"**Monto final a pagar (con descuento): ${monto_con_descuento:.2f}**")

