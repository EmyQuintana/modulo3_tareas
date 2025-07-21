tareas= [
    {
        "numero": 1,
        "nombre": "revisar y responder emails",
        "prioridad": "alta"
    },
     {
        "numero": 2,
        "nombre": "enviar a contabilidad los vouchers para validar",
        "prioridad": "media"
    
    },
    {
        "numero": 3,
        "nombre": "armar carpeta para generar OT",
        "prioridad": "alta"
        
    },
    {
        "numero": 4,
        "nombre": "hacer informes de hallazgos", 
        "prioridad": "alta"
    },
     {
        "numero": 5,
        "nombre": "hacer cotizaciones y enviarlas a clientes",
        "prioridad": "alta"
    }
]

def mostrar_tareas_disponibles():
    
    print("\n📋listado de tareas")
    print("---------------------------------------")
    for tarea in tareas:
        print(f"Número: {tarea['numero']}")
        print(f"  Nombre: {tarea['nombre']}")
        print(f"  Prioridad: {tarea["prioridad"]}")
        print("---------------------------------------")

def agregar_tarea():
    print("\n--- Agregar Nueva tarea---")
    while True:
            nombre = input("Nombre de la tarea: ").strip().capitalize()
            if not nombre:
                print("❌ El nombre del producto no puede estar vacío.")
                continue
            break
    while True:
            prioridad_input = input("Prioridad de la tarea (Alta, Media, Baja): ").strip().capitalize()
            if prioridad_input in ["Alta", "Media", "Baja"]:
                 break
            else:
                print("❌ La prioridada no puede estar vacía.")
                continue
    nuevo_numero =1
    if tareas: 
        nuevo_numero = max(tarea["numero"] for tarea in tareas) + 1
    nueva_tarea = {
            "numero":nuevo_numero,
            "nombre": nombre,
            "prioridad": prioridad_input
            }
    tareas.append(nueva_tarea)
    print(f"📝tarea '{nombre}' agregada con éxito (numero: {nuevo_numero}).")
def eliminar_tarea():
    print("\n--- Eliminar Tarea ---")
    if not mostrar_tareas_disponibles:
        print("⚠️ No hay tareas en el listado para eliminar.")
        return

    mostrar_tareas_disponibles()
    while True:
        try:
            num_a_eliminar = int(input("Ingrese el número de la tarea a eliminar (0 para cancelar): ").strip())
            if num_a_eliminar == 0:
                print("Operación cancelada.")
                return

            tarea_encontrada = False
            for i, tarea in enumerate(tareas):
                if tarea['numero'] == num_a_eliminar:
                    tarea_eliminada = tareas.pop(i) # Elimina la tarea por su índice
                    print(f" Tarea '{tarea_eliminada['nombre']}' (Número: {tarea_eliminada['numero']}) eliminada con éxito.")
                    tarea_encontrada = True
                    break
            
            if not tarea_encontrada:
                print("❌ Número de tarea no encontrado. Por favor, intente de nuevo.")

            else: 
                for j, tarea_restante in enumerate(tareas):
                    tarea_restante['numero'] = j + 1
                print("✅ Los números de las tareas han sido actualizados.")
                break # Salir del bucle si se eliminó con éxito
        except ValueError:
            print("❌ Entrada no válida. Por favor, ingrese un número.")
def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n=== Sistema de Gestión de Tareas ===")
    print("1. Mostrar listado de tareas actuales")
    print("2. Agregar nueva tarea")
    print("3. Eliminar tarea")
    print("0. Salir")
    print("---------------------------------------------")

def main():
    """Función principal que ejecuta el programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            mostrar_tareas_disponibles()
        elif opcion == '2':
            agregar_tarea()
        elif opcion == '3':
            eliminar_tarea()
        elif opcion == '0':
            print("👋¡Hasta pronto!")
            break # Sale del bucle principal y finaliza el programa
        else:
            print("❌ Opción no válida. Por favor, intente de nuevo.")
            # El bucle while se repite automáticamente

if __name__ == "__main__":
    main()