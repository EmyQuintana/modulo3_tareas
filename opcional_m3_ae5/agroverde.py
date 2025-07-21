# Módulo para generar IDs únicos (simple contador secuencial)
import itertools

# --- Estructuras de Datos Globales ---

# Lista de diccionarios para almacenar los productos disponibles en el inventario.
# Cada diccionario representa un producto con su ID, nombre, precio, stock y categoría.
productos_disponibles = [
    {"id": 101, "nombre": "Tomates Orgánicos", "precio": 2.50, "stock": 50, "categoria": "Verduras"},
    {"id": 102, "nombre": "Lechuga Fresca", "precio": 1.80, "stock": 30, "categoria": "Verduras"},
    {"id": 103, "nombre": "Manzanas Rojas", "precio": 3.00, "stock": 40, "categoria": "Frutas"},
    {"id": 104, "nombre": "Huevos de Campo (docena)", "precio": 4.50, "stock": 20, "categoria": "Lácteos y Huevos"},
    {"id": 105, "nombre": "Pan Integral Artesanal", "precio": 3.20, "stock": 15, "categoria": "Panadería"}
]

# Set para almacenar las categorías únicas de productos.
# Los sets evitan automáticamente los elementos duplicados.
categorias_productos = {producto["categoria"] for producto in productos_disponibles}

# Diccionario para registrar los pedidos de los clientes.
# La clave es un ID de pedido único y el valor es un diccionario con los detalles del pedido:
# - 'cliente_info': Tupla con (nombre_cliente, telefono_cliente, email_cliente)
# - 'productos_pedido': Lista de diccionarios, cada uno con {'id_producto': ID, 'cantidad': Cantidad}
# - 'estado': Estado actual del pedido (ej. 'Pendiente', 'En Proceso', 'Completado', 'Cancelado')
pedidos_registrados = {}

# Generador de IDs para los pedidos (secuencial)
# itertools.count() crea un iterador que devuelve números consecutivos a partir de 1.
id_pedido_generador = itertools.count(1)

# --- Funciones de Gestión ---

def mostrar_productos_disponibles():
    """
    Muestra la lista actual de productos en el inventario con su stock.
    Itera sobre la lista de productos disponibles.
    """
    print("\n--- Productos Disponibles en AgroVerde ---")
    if not productos_disponibles:
        print("Actualmente no hay productos en el inventario.")
        return
    print(f"{'ID':<5} | {'Nombre':<25} | {'Precio':<10} | {'Stock':<7} | {'Categoría':<15}")
    print("-" * 70)
    for producto in productos_disponibles:
        print(f"{producto['id']:<5} | {producto['nombre']:<25} | ${producto['precio']:.2f}{'':<7} | {producto['stock']:<7} | {producto['categoria']:<15}")
    # Módulo para generar IDs únicos (simple contador secuencial)
import itertools

# --- Estructuras de Datos Globales ---

# Lista de diccionarios para almacenar los productos disponibles en el inventario.
# Cada diccionario representa un producto con su ID, nombre, precio, stock y categoría.
productos_disponibles = [
    {"id": 101, "nombre": "Tomates Orgánicos", "precio": 2.50, "stock": 50, "categoria": "Verduras"},
    {"id": 102, "nombre": "Lechuga Fresca", "precio": 1.80, "stock": 30, "categoria": "Verduras"},
    {"id": 103, "nombre": "Manzanas Rojas", "precio": 3.00, "stock": 40, "categoria": "Frutas"},
    {"id": 104, "nombre": "Huevos de Campo (docena)", "precio": 4.50, "stock": 20, "categoria": "Lácteos y Huevos"},
    {"id": 105, "nombre": "Pan Integral Artesanal", "precio": 3.20, "stock": 15, "categoria": "Panadería"}
]

# Set para almacenar las categorías únicas de productos.
# Los sets evitan automáticamente los elementos duplicados.
categorias_productos = {producto["categoria"] for producto in productos_disponibles}

# Diccionario para registrar los pedidos de los clientes.
# La clave es un ID de pedido único y el valor es un diccionario con los detalles del pedido:
# - 'cliente_info': Tupla con (nombre_cliente, telefono_cliente, email_cliente)
# - 'productos_pedido': Lista de diccionarios, cada uno con {'id_producto': ID, 'cantidad': Cantidad}
# - 'estado': Estado actual del pedido (ej. 'Pendiente', 'En Proceso', 'Completado', 'Cancelado')
pedidos_registrados = {}

# Generador de IDs para los pedidos (secuencial)
# itertools.count() crea un iterador que devuelve números consecutivos a partir de 1.
id_pedido_generador = itertools.count(1)

# --- Funciones de Gestión ---

def mostrar_productos_disponibles():
    """
    Muestra la lista actual de productos en el inventario con su stock.
    Itera sobre la lista de productos disponibles.
    """
    print("\n--- Productos Disponibles en AgroVerde ---")
    if not productos_disponibles:
        print("Actualmente no hay productos en el inventario.")
        return

    print(f"{'ID':<5} | {'Nombre':<25} | {'Precio':<10} | {'Stock':<7} | {'Categoría':<15}")
    print("-" * 70)
    for producto in productos_disponibles:
        print(f"{producto['id']:<5} | {producto['nombre']:<25} | ${producto['precio']:.2f}{'':<7} | {producto['stock']:<7} | {producto['categoria']:<15}")
    print("-" * 70)
    print("\nCategorías existentes: ", ", ".join(categorias_productos) if categorias_productos else "Ninguna")

def agregar_producto():
    """
    Permite agregar un nuevo producto al inventario.
    Solicita los detalles del producto y actualiza las estructuras de datos.
    """
    print("\n--- Agregar Nuevo Producto ---")
    while True:
        try:
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("❌ El nombre del producto no puede estar vacío.")
                continue

            precio = float(input("Precio del producto: "))
            if precio <= 0:
                print("❌ El precio debe ser un número positivo.")
                continue

            stock = int(input("Stock inicial: "))
            if stock < 0:
                print("❌ El stock no puede ser negativo.")
                continue

            categoria = input("Categoría del producto: ").strip().capitalize()
            if not categoria:
                print("❌ La categoría no puede estar vacía.")
                continue

            # Generar un ID simple para el nuevo producto (podría ser más sofisticado si se necesita)
            # Para este ejemplo, usaremos un ID basado en el último ID + 1
            nuevo_id = max([p['id'] for p in productos_disponibles]) + 1 if productos_disponibles else 101

            nuevo_producto = {
                "id": nuevo_id,
                "nombre": nombre,
                "precio": precio,
                "stock": stock,
                "categoria": categoria
            }
            productos_disponibles.append(nuevo_producto)
            categorias_productos.add(categoria) # Añade la categoría al set (evita duplicados)
            print(f"✅ Producto '{nombre}' agregado con éxito. ID: {nuevo_id}")
            break
        except ValueError:
            print("❌ Entrada inválida. Asegúrate de ingresar números para precio y stock.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

def eliminar_producto():
    """
    Permite eliminar un producto del inventario por su ID.
    Verifica si el producto existe antes de eliminarlo.
    """
    print("\n--- Eliminar Producto ---")
    if not productos_disponibles:
        print("⚠️ No hay productos en el inventario para eliminar.")
        return

    mostrar_productos_disponibles()
    while True:
        try:
            id_a_eliminar_str = input("Ingrese el ID del producto a eliminar (o '0' para cancelar): ").strip()
            if id_a_eliminar_str == '0':
                print("🚫 Eliminación cancelada.")
                return

            id_a_eliminar = int(id_a_eliminar_str)
            
            producto_encontrado = False
            for producto in productos_disponibles:
                if producto['id'] == id_a_eliminar:
                    productos_disponibles.remove(producto)
                    print(f"✅ Producto '{producto['nombre']}' (ID: {id_a_eliminar}) eliminado con éxito.")
                    producto_encontrado = True
                    # Reconstruir el set de categorías por si la categoría del producto eliminado era única
                    global categorias_productos
                    categorias_productos = {p["categoria"] for p in productos_disponibles}
                    break # Sale del bucle for
            
            if not producto_encontrado:
                print(f"❌ Producto con ID {id_a_eliminar} no encontrado.")
            break # Sale del bucle while
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número para el ID.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            break

def realizar_pedido():
    """
    Permite a un cliente realizar un nuevo pedido.
    Verifica la disponibilidad de stock y registra el pedido.
    """
    print("\n--- Realizar Nuevo Pedido ---")
    if not productos_disponibles:
        print("⚠️ No hay productos disponibles para realizar un pedido en este momento.")
        return

    # Usar tupla para almacenar información inmutable del cliente
    nombre_cliente = input("Nombre del cliente: ").strip()
    telefono_cliente = input("Teléfono del cliente: ").strip()
    email_cliente = input("Email del cliente: ").strip()
    cliente_info = (nombre_cliente, telefono_cliente, email_cliente) # Tupla inmutable

    productos_en_pedido = []
    subtotal_pedido = 0.0

    while True:
        mostrar_productos_disponibles()
        id_producto_str = input("Ingrese el ID del producto a añadir al pedido (o '0' para finalizar): ").strip()

        if id_producto_str == '0':
            if not productos_en_pedido:
                print("🚫 Pedido cancelado: No se añadió ningún producto.")
                return # Sale de la función si no hay productos en el pedido
            break # Sale del bucle de selección de productos

        try:
            id_producto = int(id_producto_str)
            producto_obj = None
            for p in productos_disponibles:
                if p['id'] == id_producto:
                    producto_obj = p
                    break

            if producto_obj is None:
                print(f"❌ Producto con ID {id_producto} no encontrado.")
                continue # Vuelve a pedir otro producto

            while True:
                try:
                    cantidad = int(input(f"¿Cuántas unidades de '{producto_obj['nombre']}' deseas pedir? (Stock: {producto_obj['stock']}): "))
                    if cantidad <= 0:
                        print("❌ La cantidad debe ser un número positivo.")
                        continue # Vuelve a pedir la cantidad
                    if cantidad > producto_obj['stock']:
                        print(f"⚠️ No hay suficiente stock. Solo quedan {producto_obj['stock']} unidades.")
                        continue # Vuelve a pedir la cantidad
                    break # Cantidad válida, sale del bucle interno
                except ValueError:
                    print("❌ Entrada inválida para la cantidad. Por favor, ingresa un número entero.")
                    continue

            # Añadir producto al pedido y actualizar stock
            productos_en_pedido.append({'id_producto': id_producto, 'nombre': producto_obj['nombre'], 'cantidad': cantidad, 'precio_unitario': producto_obj['precio']})
            producto_obj['stock'] -= cantidad # Reduce el stock disponible
            subtotal_pedido += (producto_obj['precio'] * cantidad)
            print(f"✅ '{producto_obj['nombre']}' (x{cantidad}) añadido al pedido.")
            # No usamos 'break' aquí, para permitir añadir más productos.
            # El bucle externo 'while True' se encarga de seguir pidiendo productos.

        except ValueError:
            print("❌ ID de producto inválido. Por favor, ingresa un número entero.")
            continue # Vuelve a pedir otro producto
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            break # En caso de un error grave, salir del bucle

    # Generar un ID de pedido único
    id_pedido = next(id_pedido_generador)
    
    # Registrar el pedido en el diccionario global
    pedidos_registrados[id_pedido] = {
        'cliente_info': cliente_info,
        'productos_pedido': productos_en_pedido,
        'subtotal': subtotal_pedido,
        'estado': 'Pendiente' # Estado inicial del pedido
    }
    print(f"\n🎉 Pedido {id_pedido} de {nombre_cliente} registrado con éxito. Estado: Pendiente.")
    print(f"Total del pedido: ${subtotal_pedido:.2f}")

def actualizar_estado_pedido():
    """
    Permite cambiar el estado de un pedido existente.
    """
    print("\n--- Actualizar Estado de Pedido ---")
    if not pedidos_registrados:
        print("⚠️ No hay pedidos registrados para actualizar.")
        return

    mostrar_pedidos() # Muestra los pedidos actuales para que el usuario elija

    while True:
        try:
            id_pedido_str = input("Ingrese el ID del pedido a actualizar (o '0' para cancelar): ").strip()
            if id_pedido_str == '0':
                print("🚫 Actualización de estado cancelada.")
                return

            id_pedido = int(id_pedido_str)
            pedido = pedidos_registrados.get(id_pedido)

            if pedido is None:
                print(f"❌ Pedido con ID {id_pedido} no encontrado.")
                continue # Vuelve a pedir el ID del pedido

            print(f"Pedido {id_pedido} actual: Cliente '{pedido['cliente_info'][0]}', Estado '{pedido['estado']}'")
            
            nuevos_estados_validos = ['Pendiente', 'En Proceso', 'Completado', 'Cancelado']
            while True:
                nuevo_estado = input(f"Ingrese el nuevo estado ({', '.join(nuevos_estados_validos)}): ").strip().capitalize()
                if nuevo_estado in nuevos_estados_validos:
                    pedido['estado'] = nuevo_estado
                    print(f"✅ Estado del pedido {id_pedido} actualizado a '{nuevo_estado}'.")
                    break # Sale del bucle de selección de estado
                else:
                    print("❌ Estado inválido. Por favor, elija uno de los estados sugeridos.")
                    continue # Vuelve a pedir el estado

            break # Sale del bucle de solicitud de ID de pedido
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número para el ID del pedido.")
            continue
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            break

def mostrar_pedidos():
    """
    Muestra todos los pedidos registrados con sus detalles y estado.
    Itera sobre el diccionario de pedidos.
    """
    print("\n--- Pedidos Registrados ---")
    if not pedidos_registrados:
        print("No hay pedidos registrados aún.")
        return

    for id_pedido, detalles_pedido in pedidos_registrados.items():
        cliente_nombre = detalles_pedido['cliente_info'][0]
        cliente_telefono = detalles_pedido['cliente_info'][1]
        cliente_email = detalles_pedido['cliente_info'][2]
        productos_lista = ", ".join([f"{p['nombre']} (x{p['cantidad']})" for p in detalles_pedido['productos_pedido']])
        
        print(f"ID Pedido: {id_pedido}")
        print(f"  Cliente: {cliente_nombre} (Tel: {cliente_telefono}, Email: {cliente_email})")
        print(f"  Productos: {productos_lista}")
        print(f"  Subtotal: ${detalles_pedido['subtotal']:.2f}")
        print(f"  Estado: {detalles_pedido['estado']}")
        print("---------------------------")

def contar_totales():
    """
    Cuenta y muestra el número total de productos únicos disponibles y pedidos registrados.
    """
    print("\n--- Resumen de Totales ---")
    total_productos_unicos = len(productos_disponibles)
    total_pedidos_registrados = len(pedidos_registrados)

    print(f"Total de productos únicos en inventario: {total_productos_unicos}")
    print(f"Total de pedidos registrados: {total_pedidos_registrados}")
    print("--------------------------")

# --- Menú Principal ---

def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n=== Sistema de Gestión de Pedidos AgroVerde ===")
    print("1. Mostrar productos disponibles")
    print("2. Agregar nuevo producto")
    print("3. Eliminar producto")
    print("4. Realizar un pedido")
    print("5. Actualizar estado de pedido")
    print("6. Mostrar todos los pedidos")
    print("7. Contar totales (productos y pedidos)")
    print("0. Salir")
    print("---------------------------------------------")

def main():
    """Función principal que ejecuta el programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            mostrar_productos_disponibles()
        elif opcion == '2':
            agregar_producto()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            realizar_pedido()
        elif opcion == '5':
            actualizar_estado_pedido()
        elif opcion == '6':
            mostrar_pedidos()
        elif opcion == '7':
            contar_totales()
        elif opcion == '0':
            print("👋 ¡Gracias por usar AgroVerde! ¡Hasta pronto!")
            break # Sale del bucle principal y finaliza el programa
        else:
            print("❌ Opción no válida. Por favor, intente de nuevo.")
            # El bucle while se repite automáticamente

if __name__ == "__main__":
    main()
    print("\nCategorías existentes: ", ", ".join(categorias_productos) if categorias_productos else "Ninguna")

def agregar_producto():
    """
    Permite agregar un nuevo producto al inventario.
    Solicita los detalles del producto y actualiza las estructuras de datos.
    """
    print("\n--- Agregar Nuevo Producto ---")
    while True:
        try:
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("❌ El nombre del producto no puede estar vacío.")
                continue

            precio = float(input("Precio del producto: "))
            if precio <= 0:
                print("❌ El precio debe ser un número positivo.")
                continue

            stock = int(input("Stock inicial: "))
            if stock < 0:
                print("❌ El stock no puede ser negativo.")
                continue

            categoria = input("Categoría del producto: ").strip().capitalize()
            if not categoria:
                print("❌ La categoría no puede estar vacía.")
                continue

            # Generar un ID simple para el nuevo producto (podría ser más sofisticado si se necesita)
            # Para este ejemplo, usaremos un ID basado en el último ID + 1
            nuevo_id = max([p['id'] for p in productos_disponibles]) + 1 if productos_disponibles else 101

            nuevo_producto = {
                "id": nuevo_id,
                "nombre": nombre,
                "precio": precio,
                "stock": stock,
                "categoria": categoria
            }
            productos_disponibles.append(nuevo_producto)
            categorias_productos.add(categoria) # Añade la categoría al set (evita duplicados)
            print(f"✅ Producto '{nombre}' agregado con éxito. ID: {nuevo_id}")
            break
        except ValueError:
            print("❌ Entrada inválida. Asegúrate de ingresar números para precio y stock.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

def eliminar_producto():
    """
    Permite eliminar un producto del inventario por su ID.
    Verifica si el producto existe antes de eliminarlo.
    """
    print("\n--- Eliminar Producto ---")
    if not productos_disponibles:
        print("⚠️ No hay productos en el inventario para eliminar.")
        return

    mostrar_productos_disponibles()
    while True:
        try:
            id_a_eliminar_str = input("Ingrese el ID del producto a eliminar (o '0' para cancelar): ").strip()
            if id_a_eliminar_str == '0':
                print("🚫 Eliminación cancelada.")
                return

            id_a_eliminar = int(id_a_eliminar_str)
            
            producto_encontrado = False
            for producto in productos_disponibles:
                if producto['id'] == id_a_eliminar:
                    productos_disponibles.remove(producto)
                    print(f"✅ Producto '{producto['nombre']}' (ID: {id_a_eliminar}) eliminado con éxito.")
                    producto_encontrado = True
                    # Reconstruir el set de categorías por si la categoría del producto eliminado era única
                    global categorias_productos
                    categorias_productos = {p["categoria"] for p in productos_disponibles}
                    break # Sale del bucle for
            
            if not producto_encontrado:
                print(f"❌ Producto con ID {id_a_eliminar} no encontrado.")
            break # Sale del bucle while
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número para el ID.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            break

def realizar_pedido():
    """
    Permite a un cliente realizar un nuevo pedido.
    Verifica la disponibilidad de stock y registra el pedido.
    """
    print("\n--- Realizar Nuevo Pedido ---")
    if not productos_disponibles:
        print("⚠️ No hay productos disponibles para realizar un pedido en este momento.")
        return

    # Usar tupla para almacenar información inmutable del cliente
    nombre_cliente = input("Nombre del cliente: ").strip()
    telefono_cliente = input("Teléfono del cliente: ").strip()
    email_cliente = input("Email del cliente: ").strip()
    cliente_info = (nombre_cliente, telefono_cliente, email_cliente) # Tupla inmutable

    productos_en_pedido = []
    subtotal_pedido = 0.0

    while True:
        mostrar_productos_disponibles()
        id_producto_str = input("Ingrese el ID del producto a añadir al pedido (o '0' para finalizar): ").strip()

        if id_producto_str == '0':
            if not productos_en_pedido:
                print("🚫 Pedido cancelado: No se añadió ningún producto.")
                return # Sale de la función si no hay productos en el pedido
            break # Sale del bucle de selección de productos

        try:
            id_producto = int(id_producto_str)
            producto_obj = None
            for p in productos_disponibles:
                if p['id'] == id_producto:
                    producto_obj = p
                    break

            if producto_obj is None:
                print(f"❌ Producto con ID {id_producto} no encontrado.")
                continue # Vuelve a pedir otro producto

            while True:
                try:
                    cantidad = int(input(f"¿Cuántas unidades de '{producto_obj['nombre']}' deseas pedir? (Stock: {producto_obj['stock']}): "))
                    if cantidad <= 0:
                        print("❌ La cantidad debe ser un número positivo.")
                        continue # Vuelve a pedir la cantidad
                    if cantidad > producto_obj['stock']:
                        print(f"⚠️ No hay suficiente stock. Solo quedan {producto_obj['stock']} unidades.")
                        continue # Vuelve a pedir la cantidad
                    break # Cantidad válida, sale del bucle interno
                except ValueError:
                    print("❌ Entrada inválida para la cantidad. Por favor, ingresa un número entero.")
                    continue

            # Añadir producto al pedido y actualizar stock
            productos_en_pedido.append({'id_producto': id_producto, 'nombre': producto_obj['nombre'], 'cantidad': cantidad, 'precio_unitario': producto_obj['precio']})
            producto_obj['stock'] -= cantidad # Reduce el stock disponible
            subtotal_pedido += (producto_obj['precio'] * cantidad)
            print(f"✅ '{producto_obj['nombre']}' (x{cantidad}) añadido al pedido.")
            # No usamos 'break' aquí, para permitir añadir más productos.
            # El bucle externo 'while True' se encarga de seguir pidiendo productos.

        except ValueError:
            print("❌ ID de producto inválido. Por favor, ingresa un número entero.")
            continue # Vuelve a pedir otro producto
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            break # En caso de un error grave, salir del bucle

    # Generar un ID de pedido único
    id_pedido = next(id_pedido_generador)
    
    # Registrar el pedido en el diccionario global
    pedidos_registrados[id_pedido] = {
        'cliente_info': cliente_info,
        'productos_pedido': productos_en_pedido,
        'subtotal': subtotal_pedido,
        'estado': 'Pendiente' # Estado inicial del pedido
    }
    print(f"\n🎉 Pedido {id_pedido} de {nombre_cliente} registrado con éxito. Estado: Pendiente.")
    print(f"Total del pedido: ${subtotal_pedido:.2f}")

def actualizar_estado_pedido():
    """
    Permite cambiar el estado de un pedido existente.
    """
    print("\n--- Actualizar Estado de Pedido ---")
    if not pedidos_registrados:
        print("⚠️ No hay pedidos registrados para actualizar.")
        return

    mostrar_pedidos() # Muestra los pedidos actuales para que el usuario elija

    while True:
        try:
            id_pedido_str = input("Ingrese el ID del pedido a actualizar (o '0' para cancelar): ").strip()
            if id_pedido_str == '0':
                print("🚫 Actualización de estado cancelada.")
                return

            id_pedido = int(id_pedido_str)
            pedido = pedidos_registrados.get(id_pedido)

            if pedido is None:
                print(f"❌ Pedido con ID {id_pedido} no encontrado.")
                continue # Vuelve a pedir el ID del pedido

            print(f"Pedido {id_pedido} actual: Cliente '{pedido['cliente_info'][0]}', Estado '{pedido['estado']}'")
            
            nuevos_estados_validos = ['Pendiente', 'En Proceso', 'Completado', 'Cancelado']
            while True:
                nuevo_estado = input(f"Ingrese el nuevo estado ({', '.join(nuevos_estados_validos)}): ").strip().capitalize()
                if nuevo_estado in nuevos_estados_validos:
                    pedido['estado'] = nuevo_estado
                    print(f"✅ Estado del pedido {id_pedido} actualizado a '{nuevo_estado}'.")
                    break # Sale del bucle de selección de estado
                else:
                    print("❌ Estado inválido. Por favor, elija uno de los estados sugeridos.")
                    continue # Vuelve a pedir el estado

            break # Sale del bucle de solicitud de ID de pedido
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número para el ID del pedido.")
            continue
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            break

def mostrar_pedidos():
    """
    Muestra todos los pedidos registrados con sus detalles y estado.
    Itera sobre el diccionario de pedidos.
    """
    print("\n--- Pedidos Registrados ---")
    if not pedidos_registrados:
        print("No hay pedidos registrados aún.")
        return

    for id_pedido, detalles_pedido in pedidos_registrados.items():
        cliente_nombre = detalles_pedido['cliente_info'][0]
        cliente_telefono = detalles_pedido['cliente_info'][1]
        cliente_email = detalles_pedido['cliente_info'][2]
        productos_lista = ", ".join([f"{p['nombre']} (x{p['cantidad']})" for p in detalles_pedido['productos_pedido']])
        
        print(f"ID Pedido: {id_pedido}")
        print(f"  Cliente: {cliente_nombre} (Tel: {cliente_telefono}, Email: {cliente_email})")
        print(f"  Productos: {productos_lista}")
        print(f"  Subtotal: ${detalles_pedido['subtotal']:.2f}")
        print(f"  Estado: {detalles_pedido['estado']}")
        print("---------------------------")

def contar_totales():
    """
    Cuenta y muestra el número total de productos únicos disponibles y pedidos registrados.
    """
    print("\n--- Resumen de Totales ---")
    total_productos_unicos = len(productos_disponibles)
    total_pedidos_registrados = len(pedidos_registrados)

    print(f"Total de productos únicos en inventario: {total_productos_unicos}")
    print(f"Total de pedidos registrados: {total_pedidos_registrados}")
    print("--------------------------")

# --- Menú Principal ---

def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n=== Sistema de Gestión de Pedidos AgroVerde ===")
    print("1. Mostrar productos disponibles")
    print("2. Agregar nuevo producto")
    print("3. Eliminar producto")
    print("4. Realizar un pedido")
    print("5. Actualizar estado de pedido")
    print("6. Mostrar todos los pedidos")
    print("7. Contar totales (productos y pedidos)")
    print("0. Salir")
    print("---------------------------------------------")

def main():
    """Función principal que ejecuta el programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            mostrar_productos_disponibles()
        elif opcion == '2':
            agregar_producto()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            realizar_pedido()
        elif opcion == '5':
            actualizar_estado_pedido()
        elif opcion == '6':
            mostrar_pedidos()
        elif opcion == '7':
            contar_totales()
        elif opcion == '0':
            print("👋 ¡Gracias por usar AgroVerde! ¡Hasta pronto!")
            break # Sale del bucle principal y finaliza el programa
        else:
            print("❌ Opción no válida. Por favor, intente de nuevo.")
            # El bucle while se repite automáticamente

if __name__ == "__main__":
    main()