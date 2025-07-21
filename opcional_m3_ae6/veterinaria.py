import datetime # Módulo para trabajar con fechas y horas

# --- 1. Estructuras de Datos Globales ---
# Estas variables globales almacenarán la información principal del sistema.
# Se pasarán como parámetros a las funciones para evitar el acceso directo y fomentar la modularidad.

# Diccionario para almacenar información de las mascotas.
# La clave será el ID de la mascota (generado secuencialmente) y el valor será un diccionario
# con sus detalles (nombre, especie, raza, etc.).
mascotas = {} # {id_mascota: {'nombre': '...', 'especie': '...', 'raza': '...'}}
id_mascota_counter = 1 # Contador para generar IDs únicos para las mascotas

# Diccionario para almacenar las citas.
# La clave será la fecha de la cita (como cadena 'YYYY-MM-DD') y el valor será una lista
# de diccionarios, donde cada diccionario representa una cita en esa fecha.
# Esto permite agrupar citas por día.
citas = {} # {'YYYY-MM-DD': [{'hora': 'HH:MM', 'id_mascota': ID, 'motivo': '...'}]}

# Diccionario para almacenar el historial de tratamientos de cada mascota.
# La clave será el ID de la mascota y el valor será una lista de diccionarios,
# donde cada diccionario representa un tratamiento.
historial_tratamientos = {} # {id_mascota: [{'fecha': 'YYYY-MM-DD', 'tratamiento': '...', 'notas': '...'}]}

# Horarios de atención disponibles por defecto (ej. cada hora, de 9:00 a 17:00)
# Se usa para calcular la disponibilidad.
HORARIOS_ATENCION_DIA = [
    "09:00", "10:00", "11:00", "12:00", "13:00",
    "14:00", "15:00", "16:00", "17:00"
]

# --- 2. Funciones de Gestión ---

def registrar_mascota(mascotas_dict, id_counter):
    """
    Define una función para registrar una nueva mascota.
    Recibe el diccionario de mascotas y el contador de IDs como parámetros.
    Retorna el ID de la nueva mascota y el contador actualizado.
    """
    print("\n--- Registrar Nueva Mascota ---")
    nombre = input("Nombre de la mascota: ").strip()
    especie = input("Especie (ej. Perro, Gato, Ave): ").strip()
    raza = input("Raza: ").strip()
    nombre_propietario = input("Nombre del propietario: ").strip()
    
    # --- INICIO CAMBIO: Validación de teléfono (9 dígitos, empieza con 9) ---
    telefono_propietario = ""
    while True:
        telefono_propietario = input("Teléfono del propietario (9 dígitos, debe empezar con 9): ").strip()
        if len(telefono_propietario) == 9 and telefono_propietario.isdigit() and telefono_propietario.startswith('9'):
            break
        else:
            print("❌ Formato de teléfono inválido. Debe ser un número de 9 dígitos y empezar con '9'.")
    # --- FIN CAMBIO ---

    # Generar un ID único para la mascota
    id_actual = id_counter
    id_counter += 1 # Incrementa el contador global (se retornará para actualizar)

    mascotas_dict[id_actual] = {
        'nombre': nombre,
        'especie': especie,
        'raza': raza,
        'propietario': nombre_propietario,
        'telefono': telefono_propietario
    }
    print(f"✅ Mascota '{nombre}' (ID: {id_actual}) registrada con éxito.")
    
    # Retorna el ID de la nueva mascota y el contador actualizado
    return id_actual, id_counter

def calcular_horarios_disponibles(fecha_str, citas_dict, horarios_base):
    """
    Usa funciones para calcular horarios disponibles para una fecha dada.
    Recibe la fecha (str), el diccionario de citas y los horarios base como parámetros.
    Retorna una lista de horarios que están disponibles.
    """
    horarios_ocupados = set() # Variable local para almacenar horarios ya tomados ese día

    # Si hay citas para esa fecha, recopila los horarios ocupados
    if fecha_str in citas_dict:
        for cita in citas_dict[fecha_str]:
            horarios_ocupados.add(cita['hora'])
    
    # Calcula los horarios disponibles restando los ocupados de los base
    horarios_disponibles = [
        horario for horario in horarios_base if horario not in horarios_ocupados
    ]
    
    # Retorna la lista de horarios disponibles
    return horarios_disponibles

def registrar_cita(citas_dict, mascotas_dict, horarios_base):
    """
    Define una función para registrar nuevas citas.
    Recibe el diccionario de citas, mascotas y los horarios base como parámetros.
    Utiliza funciones para calcular horarios disponibles y evita sobrecupos.
    """
    print("\n--- Agendar Nueva Cita ---")
    if not mascotas_dict:
        print("⚠️ No hay mascotas registradas. Por favor, registre una mascota primero.")
        return

    # 1. Seleccionar Mascota
    print("\nMascotas registradas:")
    for id_m, m_info in mascotas_dict.items():
        print(f"  ID: {id_m} - {m_info['nombre']} ({m_info['especie']})")
    
    id_mascota = None
    while id_mascota is None:
        try:
            id_input = input("Ingrese el ID de la mascota para la cita (o '0' para cancelar): ").strip()
            if id_input == '0':
                print("🚫 Cita cancelada.")
                return
            id_mascota = int(id_input)
            if id_mascota not in mascotas_dict:
                print("❌ ID de mascota no encontrado. Intente de nuevo.")
                id_mascota = None # Reinicia para que el bucle continúe
        except ValueError:
            print("❌ Entrada inválida. El ID de la mascota debe ser un número.")
    
    mascota_info = mascotas_dict[id_mascota]
    print(f"Mascota seleccionada: {mascota_info['nombre']}")

    # --- INICIO CAMBIO: Seleccionar fecha de una lista ---
    fechas_disponibles_obj = []
    print("\nFechas disponibles para agendar citas (próximos 7 días):")
    for i in range(7): # Genera fechas para los próximos 7 días
        fecha_actual = datetime.date.today() + datetime.timedelta(days=i)
        fechas_disponibles_obj.append(fecha_actual)
        print(f"  {i+1}. {fecha_actual.strftime('%d-%m-%Y')}")
    
    fecha_valida_seleccion = False
    fecha_cita_str = ""
    while not fecha_valida_seleccion:
        try:
            opcion_fecha = input("Seleccione el número de la fecha deseada: ").strip()
            idx_fecha = int(opcion_fecha) - 1 # Ajustar a índice 0-basado
            if 0 <= idx_fecha < len(fechas_disponibles_obj):
                fecha_cita_str = fechas_disponibles_obj[idx_fecha].strftime('%Y-%m-%d')
                fecha_valida_seleccion = True
            else:
                print("❌ Número de fecha no válido. Intente de nuevo.")
        except ValueError:
            print("❌ Entrada inválida. Debe ser un número.")
    # --- FIN CAMBIO ---
    
    # 3. Calcular y Mostrar Horarios Disponibles (usando la función)
    horarios_disponibles_hoy = calcular_horarios_disponibles(fecha_cita_str, citas_dict, horarios_base)

    if not horarios_disponibles_hoy:
        print(f"⚠️ No hay horarios disponibles para el {fecha_cita_str}.")
        return

    print(f"\nHorarios disponibles para el {fecha_cita_str}:")
    for i, hora in enumerate(horarios_disponibles_hoy):
        print(f"  {i+1}. {hora}")

    # 4. Seleccionar Horario
    hora_cita = None
    while hora_cita is None:
        try:
            opcion_hora = input("Seleccione el número del horario deseado: ").strip()
            idx_hora = int(opcion_hora) - 1 # Ajustar a índice 0-basado
            if 0 <= idx_hora < len(horarios_disponibles_hoy):
                hora_cita = horarios_disponibles_hoy[idx_hora]
            else:
                print("❌ Número de horario no válido. Intente de nuevo.")
        except ValueError:
            print("❌ Entrada inválida. Debe ser un número.")

    motivo_cita = input("Motivo de la cita: ").strip()

    # 5. Registrar la Cita
    # Si la fecha no existe como clave en 'citas_dict', la crea con una lista vacía
    if fecha_cita_str not in citas_dict:
        citas_dict[fecha_cita_str] = []
    
    # Agrega la nueva cita a la lista de citas de esa fecha
    citas_dict[fecha_cita_str].append({
        'hora': hora_cita,
        'id_mascota': id_mascota,
        'nombre_mascota': mascota_info['nombre'], # Para facilitar la visualización
        'motivo': motivo_cita
    })
    print(f"🎉 Cita agendada para {mascota_info['nombre']} el {fecha_cita_str} a las {hora_cita}.")

def registrar_tratamiento(historial_dict, mascotas_dict):
    """
    Define una función para registrar tratamientos para una mascota.
    Recibe el diccionario de historial de tratamientos y mascotas como parámetros.
    """
    print("\n--- Registrar Tratamiento ---")
    if not mascotas_dict:
        print("⚠️ No hay mascotas registradas para añadir tratamientos.")
        return

    # 1. Seleccionar Mascota
    print("\nMascotas registradas:")
    for id_m, m_info in mascotas_dict.items():
        print(f"  ID: {id_m} - {m_info['nombre']} ({m_info['especie']})")
    
    id_mascota = None
    while id_mascota is None:
        try:
            id_input = input("Ingrese el ID de la mascota para el tratamiento (o '0' para cancelar): ").strip()
            if id_input == '0':
                print("🚫 Registro de tratamiento cancelado.")
                return
            id_mascota = int(id_input)
            if id_mascota not in mascotas_dict:
                print("❌ ID de mascota no encontrado. Intente de nuevo.")
                id_mascota = None
        except ValueError:
            print("❌ Entrada inválida. El ID de la mascota debe ser un número.")
    
    mascota_info = mascotas_dict[id_mascota]
    print(f"Mascota seleccionada: {mascota_info['nombre']}")

    # 2. Detalles del Tratamiento
    fecha_tratamiento_str = datetime.date.today().strftime('%Y-%m-%d') # Fecha actual por defecto
    tratamiento_desc = input("Descripción del tratamiento: ").strip()
    notas_adic = input("Notas adicionales: ").strip()

    # Si la mascota no tiene historial, crea una lista vacía para ella
    if id_mascota not in historial_dict:
        historial_dict[id_mascota] = []
    
    # Agrega el nuevo tratamiento a la lista de historial de la mascota
    historial_dict[id_mascota].append({
        'fecha': fecha_tratamiento_str,
        'tratamiento': tratamiento_desc,
        'notas': notas_adic
    })
    print(f"🎉 Tratamiento registrado para {mascota_info['nombre']} el {fecha_tratamiento_str}.")

def mostrar_historial_mascota(mascotas_dict, historial_dict):
    """
    Muestra el historial de tratamientos de una mascota específica.
    Recibe los diccionarios de mascotas e historial como parámetros.
    """
    print("\n--- Historial de Mascota ---")
    if not mascotas_dict:
        print("⚠️ No hay mascotas registradas.")
        return
    
    print("\nMascotas registradas:")
    for id_m, m_info in mascotas_dict.items():
        print(f"  ID: {id_m} - {m_info['nombre']} ({m_info['especie']})")
    
    id_mascota = None
    while id_mascota is None:
        try:
            id_input = input("Ingrese el ID de la mascota para ver su historial (o '0' para cancelar): ").strip()
            if id_input == '0':
                print("🚫 Consulta de historial cancelada.")
                return
            id_mascota = int(id_input)
            if id_mascota not in mascotas_dict:
                print("❌ ID de mascota no encontrado. Intente de nuevo.")
                id_mascota = None
        except ValueError:
            print("❌ Entrada inválida. El ID de la mascota debe ser un número.")
    
    mascota_info = mascotas_dict[id_mascota]
    print(f"\n--- Historial de '{mascota_info['nombre']}' (ID: {id_mascota}) ---")
    
    if id_mascota not in historial_dict or not historial_dict[id_mascota]:
        print("No hay tratamientos registrados para esta mascota aún.")
        return
    
    for i, tratamiento in enumerate(historial_dict[id_mascota]):
        print(f"  Tratamiento {i+1}:")
        print(f"    Fecha: {tratamiento['fecha']}")
        print(f"    Descripción: {tratamiento['tratamiento']}")
        print(f"    Notas: {tratamiento['notas']}")
        print("    --------------------")

def mostrar_citas_dia(citas_dict, mascotas_dict):
    """
    Muestra todas las citas agendadas para un día específico.
    Recibe los diccionarios de citas y mascotas como parámetros.
    """
    print("\n--- Citas por Día ---")
    if not citas_dict:
        print("⚠️ No hay citas agendadas aún.")
        return

    # --- INICIO CAMBIO: Seleccionar fecha de una lista para consulta ---
    fechas_disponibles_obj = []
    print("\nFechas con citas agendadas:")
    # Recopila y muestra solo las fechas que ya tienen citas
    fechas_con_citas = sorted(citas_dict.keys())
    if not fechas_con_citas:
        print("No hay fechas con citas agendadas.")
        return

    for i, fecha_str_key in enumerate(fechas_con_citas):
        try:
            fecha_obj_display = datetime.datetime.strptime(fecha_str_key, '%Y-%m-%d').date()
            fechas_disponibles_obj.append(fecha_obj_display) # Almacena el objeto fecha para referencia
            print(f"  {i+1}. {fecha_obj_display.strftime('%d-%m-%Y')}")
        except ValueError:
            print(f"  {i+1}. {fecha_str_key} (Formato inválido)") # En caso de fecha mal guardada
    
    fecha_valida_seleccion = False
    fecha_consulta_str = ""
    while not fecha_valida_seleccion:
        try:
            opcion_fecha = input("Seleccione el número de la fecha a consultar (o '0' para cancelar): ").strip()
            if opcion_fecha == '0':
                print("🚫 Consulta de citas cancelada.")
                return

            idx_fecha = int(opcion_fecha) - 1 # Ajustar a índice 0-basado
            if 0 <= idx_fecha < len(fechas_disponibles_obj):
                fecha_consulta_str = fechas_disponibles_obj[idx_fecha].strftime('%Y-%m-%d')
                fecha_valida_seleccion = True
            else:
                print("❌ Número de fecha no válido. Intente de nuevo.")
        except ValueError:
            print("❌ Entrada inválida. Debe ser un número.")
    # --- FIN CAMBIO ---
    
    print(f"\n--- Citas para el {fecha_consulta_str} ---")
    if fecha_consulta_str not in citas_dict or not citas_dict[fecha_consulta_str]:
        print("No hay citas agendadas para esta fecha.")
        return
    
    # Ordenar citas por hora para una mejor visualización
    citas_del_dia = sorted(citas_dict[fecha_consulta_str], key=lambda c: c['hora'])

    for i, cita in enumerate(citas_del_dia):
        # Obtener información completa de la mascota si es necesario
        mascota_nombre = mascotas_dict.get(cita['id_mascota'], {}).get('nombre', 'Desconocida')
        propietario_nombre = mascotas_dict.get(cita['id_mascota'], {}).get('propietario', 'Desconocido')
        
        print(f"  Cita {i+1}:")
        print(f"    Hora: {cita['hora']}")
        print(f"    Mascota: {mascota_nombre} (ID: {cita['id_mascota']})")
        print(f"    Propietario: {propietario_nombre}")
        print(f"    Motivo: {cita['motivo']}")
        print("    --------------------")

# --- 3. Menú Principal y Ejecución ---

def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n=== Sistema de Gestión de Citas VetCare ===")
    print("1. Registrar nueva mascota")
    print("2. Agendar nueva cita")
    print("3. Registrar tratamiento")
    print("4. Ver historial de mascota")
    print("5. Ver citas de un día")
    print("0. Salir")
    print("------------------------------------------")

def main():
    """
    Función principal que ejecuta el programa.
    Maneja el bucle del menú y llama a las funciones de gestión,
    pasando las variables globales como parámetros.
    """
    # Se usan las variables globales definidas al inicio del script.
    # Es crucial pasarlas a las funciones para que estas operen sobre los mismos datos.
    global mascotas, citas, historial_tratamientos, id_mascota_counter, HORARIOS_ATENCION_DIA

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            # La función retorna el nuevo ID y el contador actualizado,
            # que luego se reasignan a las variables globales.
            _, id_mascota_counter = registrar_mascota(mascotas, id_mascota_counter)
        elif opcion == '2':
            # Se pasan las estructuras de datos que la función necesita modificar o consultar.
            registrar_cita(citas, mascotas, HORARIOS_ATENCION_DIA)
        elif opcion == '3':
            # Se pasan las estructuras de datos necesarias.
            registrar_tratamiento(historial_tratamientos, mascotas)
        elif opcion == '4':
            # Se pasan las estructuras de datos para consulta.
            mostrar_historial_mascota(mascotas, historial_tratamientos)
        elif opcion == '5':
            # Se pasan las estructuras de datos para consulta.
            mostrar_citas_dia(citas, mascotas)
        elif opcion == '0':
            print("👋 ¡Gracias por usar VetCare! ¡Hasta pronto!")
            break # Sale del bucle principal y finaliza el programa
        else:
            print("❌ Opción no válida. Por favor, intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
