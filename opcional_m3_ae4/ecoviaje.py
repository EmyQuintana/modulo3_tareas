# --- Configuración Inicial de Excursiones ---
# Lista de diccionarios para almacenar la información de cada excursión.
# Cada diccionario representa una excursión con su nombre, cupo total,
# cupo disponible (que se irá actualizando) y una lista de las reservas.
excursiones = [
    {
        "numero": 1,
        "nombre": "Sendero del Bosque Encantado",
        "cupo_total": 10,
        "cupo_disponible": 10,
        "reservas": [] # Lista para guardar los nombres de los participantes
    },
    {
        "numero": 2,
        "nombre": "Ascenso al Volcán Dormido",
        "cupo_total": 5,
        "cupo_disponible": 5,
        "reservas": []
    },
    {
        "numero": 3,
        "nombre": "Rafting en el Río Salvaje",
        "cupo_total": 8,
        "cupo_disponible": 8,
        "reservas": []
    },
    {
        "numero": 4,
        "nombre": "Observación de Aves en el Humedal",
        "cupo_total": 12,
        "cupo_disponible": 12,
        "reservas": []
    }
]

# --- Funciones del Programa ---

def mostrar_excursiones():
    """
    Muestra la lista de excursiones disponibles con sus detalles.
    Utiliza un ciclo 'for' para iterar sobre la lista de excursiones.
    """
    print("\n--- Excursiones Disponibles EcoViaje ---")
    print("---------------------------------------")
    for excursion in excursiones:
        # Imprime los detalles de cada excursión
        print(f"Número: {excursion['numero']}")
        print(f"  Nombre: {excursion['nombre']}")
        print(f"  Cupos Disponibles: {excursion['cupo_disponible']}/{excursion['cupo_total']}")
        # Muestra los participantes si ya hay reservas
        if excursion['reservas']:
            print(f"  Participantes: {', '.join(excursion['reservas'])}")
        else:
            print("  Participantes: Ninguno aún.")
        print("---------------------------------------")

def realizar_reserva():
    """
    Permite a un usuario reservar un cupo en una excursión.
    Utiliza ciclos 'while' para validación de entrada y 'if' para condiciones.
    """
    print("\n--- Realizar Nueva Reserva ---")
    nombre_usuario = input("Por favor, ingresa tu nombre para la reserva: ").strip()

    # Bucle 'while True' para solicitar el número de excursión hasta que sea válido.
    while True:
        try:
            num_excursion_str = input("Ingresa el número de la excursión que deseas reservar (o '0' para cancelar): ").strip()
            
            if num_excursion_str == '0':
                print("🚫 Reserva cancelada por el usuario.")
                return # Sale de la función

            num_excursion = int(num_excursion_str)
            
            # Buscar la excursión por su número
            excursion_encontrada = None
            # Ciclo 'for' para buscar la excursión en la lista
            for excursion in excursiones:
                if excursion['numero'] == num_excursion:
                    excursion_encontrada = excursion
                    break # 'break' para salir del ciclo 'for' una vez que se encuentra la excursión
            
            if excursion_encontrada is None:
                print("❌ Número de excursión no válido. Por favor, intenta de nuevo.")
                continue # 'continue' para saltar al inicio del ciclo 'while' y pedir de nuevo
            
            # Verificar cupos disponibles
            if excursion_encontrada['cupo_disponible'] > 0:
                excursion_encontrada['cupo_disponible'] -= 1 # Reduce el cupo disponible
                excursion_encontrada['reservas'].append(nombre_usuario) # Agrega el nombre a la lista de reservas
                print(f"🎉 ¡Reserva exitosa! {nombre_usuario} ha reservado un cupo en '{excursion_encontrada['nombre']}'.")
                print(f"Cupos restantes para '{excursion_encontrada['nombre']}': {excursion_encontrada['cupo_disponible']}/{excursion_encontrada['cupo_total']}")
                break # 'break' para salir del ciclo 'while' una vez que la reserva es exitosa
            else:
                print(f"⚠️ ¡Lo sentimos! La excursión '{excursion_encontrada['nombre']}' ya no tiene cupos disponibles.")
                break # 'break' para salir del ciclo 'while' si la excursión está llena
        
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingresa un número válido para la excursión.")
            continue # 'continue' para saltar al inicio del ciclo 'while' y pedir de nuevo
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            break # En caso de un error grave, salir del bucle

# --- Menú Principal del Programa ---

def main():
    """
    Función principal que ejecuta el programa y el menú de interacción.
    Utiliza un ciclo 'while True' para mantener el programa en ejecución.
    """
    print("\n=== ¡Bienvenido a EcoViaje! ===")
    
    # Bucle principal del programa
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ver excursiones disponibles")
        print("2. Realizar una reserva")
        print("0. Salir del programa")
        print("----------------------")
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == '1':
            mostrar_excursiones()
        elif opcion == '2':
            realizar_reserva()
        elif opcion == '0':
            print("👋 ¡Gracias por usar EcoViaje! ¡Que tengas un gran día!")
            break # 'break' para salir del ciclo 'while True' y finalizar el programa
        else:
            print("❌ Opción no válida. Por favor, ingresa 1, 2 o 0.")
            # No se necesita 'continue' aquí, el ciclo 'while' simplemente se repetirá

# Punto de entrada del programa
if __name__ == "__main__":
    main()