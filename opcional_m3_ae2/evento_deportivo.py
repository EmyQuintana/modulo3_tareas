import random #para mezclar aleatoriamente la lista de participantes antes de asignarlos a equipos, para una distribucion equitativa
import datetime # Importamos el módulo datetime

# Clase para generar IDs simplificados y únicos.
class IdGenerator:
    def __init__(self):
        # Diccionario para llevar la cuenta de los correlativos por prefijo
        self._counters = {} 

    def generate_id(self, prefix):
        """Genera un ID único con un prefijo dado y un contador correlativo."""
        if prefix not in self._counters:
            self._counters[prefix] = 0
        self._counters[prefix] += 1
        # :03d para padding con ceros (ej. 001, 002)
        return f"{prefix}{self._counters[prefix]:03d}" 

# Instancia global del generador de IDs
id_gen = IdGenerator()

class EventoDeportivo:
    def __init__(self, nombre, fecha, tipo_evento, estado="En proceso"):
        self.nombre = nombre
        self.fecha = fecha # La fecha se almacena como string (YYYY-MM-DD)
        self.tipo_evento = tipo_evento
        self.estado = estado
        self.participantes_inscritos = [] # Lista de objetos Participante
        self.equipos = {}                # Diccionario: {nombre_equipo: [participante1, participante2, ...]}
        
        # Generar ID basado en el nombre del evento
        prefix_parts = [word[0].upper() for word in nombre.split() if word]
        prefix = "".join(prefix_parts)
        
        if not prefix or len(prefix) < 2:
            prefix = "EV"
        elif len(prefix) > 3:
            prefix = prefix[:3] 
            
        self.id = id_gen.generate_id(prefix) 

    def __str__(self):
        # Convertir la fecha de string a objeto datetime para formatearla
        try:
            fecha_obj = datetime.datetime.strptime(self.fecha, '%Y-%m-%d')
            # Formatear a "día de Mes de Año"
            fecha_formateada = fecha_obj.strftime('%d de %B de %Y')
        except ValueError:
            fecha_formateada = self.fecha + " (Formato de fecha inválido)" # En caso de que la fecha no cumpla el formato esperado

        return (f"ID: {self.id} | Nombre: {self.nombre} | Fecha: {fecha_formateada} | "
                f"Tipo: {self.tipo_evento} | Estado: {self.estado} | "
                f"Participantes: {len(self.participantes_inscritos)}")

    def agregar_participante(self, participante):
        """Agrega un participante al evento si no está ya inscrito."""
        if participante not in self.participantes_inscritos:
            self.participantes_inscritos.append(participante)
            print(f"✅ {participante.nombre} inscrito en {self.nombre}.")
            return True
        else:
            print(f"⚠️ {participante.nombre} ya está inscrito en {self.nombre}.")
            return False

    def confirmar_asistencia(self, participante):
        """Confirma la asistencia de un participante para el evento."""
        if participante in self.participantes_inscritos:
            print(f"✅ Asistencia de {participante.nombre} confirmada para {self.nombre}.")
            return True
        else:
            print(f"❌ {participante.nombre} no está inscrito en {self.nombre}.")
            return False

    def asignar_equipo_automatico(self, num_equipos=2):
        """
        Asigna participantes a equipos de forma automática y equitativa.
        Reinicia los equipos existentes.
        """
        if len(self.participantes_inscritos) < num_equipos:
            print(f"⚠️ No hay suficientes participantes ({len(self.participantes_inscritos)}) para crear {num_equipos} equipos.")
            return

        self.equipos = {f"Equipo {i+1}": [] for i in range(num_equipos)}
        
        participantes_shuffled = self.participantes_inscritos[:] # Copia para no modificar la original
        random.shuffle(participantes_shuffled)

        # Asignar participantes a equipos de forma circular
        for i, participante in enumerate(participantes_shuffled):
            nombre_equipo = f"Equipo {(i % num_equipos) + 1}"
            self.equipos[nombre_equipo].append(participante)

        print(f"✅ Equipos asignados automáticamente para el evento {self.nombre}.")
        for nombre_equipo, miembros in self.equipos.items():
            print(f"  {nombre_equipo}: {[p.nombre for p in miembros]}")


class Participante:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.eventos_inscritos = [] # Lista de objetos EventoDeportivo
        
        # Generar ID basado en nombre y apellido
        nombre_partes = nombre.split()
        if len(nombre_partes) >= 2:
            prefix = f"{nombre_partes[0][0].upper()}{nombre_partes[-1][0].upper()}"
        elif nombre_partes:
            prefix = nombre_partes[0][0].upper() 
        else:
            prefix = "PA" 
        self.id = id_gen.generate_id(prefix) 

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Email: {self.email}"

    def inscribirse_evento(self, evento):
        """Inscribe al participante en un evento."""
        if evento.agregar_participante(self): 
            self.eventos_inscritos.append(evento)
            print(f"✅ {self.nombre} ahora está registrado en el evento: {evento.nombre}.")
        else:
            print(f"⚠️ {self.nombre} ya estaba registrado en el evento: {evento.nombre}.")


# Inicialización de las estructuras de almacenamiento globales
eventos = {}        # {evento_id: EventoDeportivo_objeto}
participantes = {}  # {participante_id: Participante_objeto}

def registrar_evento():
    """Permite al usuario registrar un nuevo evento deportivo."""
    print("\n--- Registrar Nuevo Evento Deportivo ---")
    nombre = input("Nombre del evento: ")
    
    # --- CAMBIO: Solicitar día, mes y año por separado y validar ---
    fecha_valida = False
    while not fecha_valida:
        try:
            dia = int(input("Día del evento (DD): "))
            mes = int(input("Mes del evento (MM): "))
            anio = int(input("Año del evento (YYYY): "))
            
            # Intentar crear un objeto datetime.date para validar la fecha
            # Esto lanzará un ValueError si la fecha es inválida (ej. 30 de febrero)
            fecha_obj_temp = datetime.date(anio, mes, dia)
            fecha = fecha_obj_temp.strftime('%Y-%m-%d') # Formatear a YYYY-MM-DD para almacenar
            fecha_valida = True
        except ValueError:
            print("❌ Fecha inválida. Por favor, ingrese números válidos para día, mes y año.")
            print("Asegúrese de que la fecha sea una fecha real (ej. 31 de Febrero no es válido).")
    # --- FIN CAMBIO ---

    tipo = input("Tipo de evento (ej. Futbol, Baloncesto, Carrera): ")

    nuevo_evento = EventoDeportivo(nombre, fecha, tipo)
    eventos[nuevo_evento.id] = nuevo_evento 
    
    # Mostrar la fecha formateada al registrar
    try:
        fecha_obj = datetime.datetime.strptime(nuevo_evento.fecha, '%Y-%m-%d')
        fecha_formateada_reg = fecha_obj.strftime('%d de %B de %Y')
    except ValueError:
        fecha_formateada_reg = nuevo_evento.fecha + " (Formato de fecha inválido)"

    print(f"🎉 Evento '{nuevo_evento.nombre}' registrado con éxito. ID: {nuevo_evento.id} | Fecha: {fecha_formateada_reg}")
    return nuevo_evento.id

def registrar_participante():
    """Permite al usuario registrar un nuevo participante."""
    print("\n--- Registrar Nuevo Participante ---")
    nombre = input("Nombre del participante: ")
    email = input("Email del participante: ")

    nuevo_participante = Participante(nombre, email)
    participantes[nuevo_participante.id] = nuevo_participante 
    print(f"👤 Participante '{nuevo_participante.nombre}' registrado con éxito. ID: {nuevo_participante.id}")
    return nuevo_participante.id

def inscribir_participante_en_evento():
    """Permite inscribir un participante existente en un evento existente."""
    print("\n--- Inscribir Participante en Evento ---")
    if not participantes or not eventos:
        print("⚠️ No hay participantes o eventos registrados para realizar inscripciones.")
        return

    print("\nParticipantes disponibles:")
    for p_id, p in participantes.items():
        print(f"  {p_id}: {p.nombre} ({p.email})")

    p_id_input = input("Ingrese el ID del participante a inscribir: ").strip().upper() # Limpiar y convertir a mayúsculas
    # --- CAMBIO CLAVE: NO SE USA int() AQUÍ ---
    participante_obj = participantes.get(p_id_input)
    if not participante_obj:
        print(f"❌ Participante con ID '{p_id_input}' no encontrado.")
        return

    print("\nEventos disponibles:")
    for e_id, e in eventos.items():
        print(e) # Esto usará el __str__ modificado con la fecha formateada

    e_id_input = input("Ingrese el ID del evento en el que desea inscribir al participante: ").strip().upper() # Limpiar y convertir a mayúsculas
    # --- CAMBIO CLAVE: NO SE USA int() AQUÍ ---
    evento_obj = eventos.get(e_id_input)
    if not evento_obj:
        print(f"❌ Evento con ID '{e_id_input}' no encontrado.")
        return

    participante_obj.inscribirse_evento(evento_obj)

def consultar_eventos_por_estado():
    """Permite consultar eventos filtrados por su estado."""
    print("\n--- Consultar Eventos por Estado ---")
    if not eventos:
        print("⚠️ No hay eventos registrados.")
        return

    estado_buscado = input("Ingrese el estado a buscar (En proceso, Confirmado, Cancelado, o 'todos' para ver todos): ").capitalize()
    
    encontrado = False
    for evento in eventos.values():
        if estado_buscado == "Todos" or evento.estado == estado_buscado:
            print(evento) # Esto usará el __str__ modificado con la fecha formateada
            encontrado = True
            continue 
    
    if not encontrado:
        print(f"❌ No se encontraron eventos con el estado '{estado_buscado}'.")

def asignar_equipos_a_evento():
    """Permite asignar equipos automáticamente para un evento."""
    print("\n--- Asignar Equipos a Evento ---")
    if not eventos:
        print("⚠️ No hay eventos registrados para asignar equipos.")
        return

    print("\nEventos disponibles para asignación de equipos:")
    for e_id, e in eventos.items():
        print(e) # Esto usará el __str__ modificado con la fecha formateada

    e_id_input = input("Ingrese el ID del evento para asignar equipos: ").strip().upper() # Limpiar y convertir a mayúsculas
    # --- CAMBIO CLAVE: NO SE USA int() AQUÍ ---
    evento_obj = eventos.get(e_id_input)
    if not evento_obj:
        print(f"❌ Evento con ID '{e_id_input}' no encontrado.")
        return

    if len(evento_obj.participantes_inscritos) == 0:
        print(f"⚠️ El evento '{evento_obj.nombre}' no tiene participantes inscritos para formar equipos.")
        return

    while True: # Bucle para asegurar una entrada válida para el número de equipos
        num_equipos_input = input(f"¿Cuántos equipos desea crear para '{evento_obj.nombre}'? (Min 2, Max {len(evento_obj.participantes_inscritos)}): ")
        try:
            # --- CAMBIO CLAVE: Se usa int() aquí para el NÚMERO de equipos ---
            num_equipos = int(num_equipos_input) 
            if num_equipos < 2:
                print("⚠️ Debe crear al menos 2 equipos.")
                continue 
            if num_equipos > len(evento_obj.participantes_inscritos):
                print(f"⚠️ No puede crear más equipos que participantes ({len(evento_obj.participantes_inscritos)}).")
                continue 
            break 
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingrese un número entero.")

    evento_obj.asignar_equipo_automatico(num_equipos)

def gestionar_estado_evento():
    """Permite cambiar el estado de un evento (En proceso, Confirmado, Cancelado)."""
    print("\n--- Gestionar Estado de Evento ---")
    if not eventos:
        print("⚠️ No hay eventos registrados.")
        return

    print("\nEventos disponibles:")
    for e_id, e in eventos.items():
        print(e) # Esto usará el __str__ modificado con la fecha formateada

    e_id_input = input("Ingrese el ID del evento cuyo estado desea cambiar: ").strip().upper() 
    # --- CAMBIO CLAVE: NO SE USA int() AQUÍ ---
    evento_obj = eventos.get(e_id_input)
    if not evento_obj:
        print(f"❌ Evento con ID '{e_id_input}' no encontrado.")
        return

    while True:
        nuevo_estado = input("Ingrese el nuevo estado (En proceso, Confirmado, Cancelado): ").capitalize()
        if nuevo_estado in ["En proceso", "Confirmado", "Cancelado"]:
            evento_obj.estado = nuevo_estado
            print(f"✅ El estado del evento '{evento_obj.nombre}' se ha actualizado a '{nuevo_estado}'.")
            break 
        else:
            print("❌ Estado inválido. Por favor, ingrese 'En proceso', 'Confirmado' o 'Cancelado'.")

def confirmar_asistencia_participante():
    """Permite al organizador confirmar la asistencia de un participante."""
    print("\n--- Confirmar Asistencia de Participante ---")
    if not participantes or not eventos:
        print("⚠️ No hay participantes o eventos registrados.")
        return

    print("\nEventos disponibles:")
    for e_id, e in eventos.items():
        print(e) # Esto usará el __str__ modificado con la fecha formateada

    e_id_input = input("Ingrese el ID del evento para confirmar asistencia: ").strip().upper() 
    # --- CAMBIO CLAVE: NO SE USA int() AQUÍ ---
    evento_obj = eventos.get(e_id_input)
    if not evento_obj:
        print(f"❌ Evento con ID '{e_id_input}' no encontrado.")
        return

    if not evento_obj.participantes_inscritos:
        print(f"⚠️ El evento '{evento_obj.nombre}' no tiene participantes inscritos.")
        return

    print(f"\nParticipantes inscritos en '{evento_obj.nombre}':")
    for i, p in enumerate(evento_obj.participantes_inscritos):
        print(f"  {i+1}. {p.nombre} (ID: {p.id})") 

    p_index_input = input(f"Ingrese el NÚMERO del participante a confirmar asistencia (1-{len(evento_obj.participantes_inscritos)}): ")
    try:
        # --- CAMBIO CLAVE: Se usa int() aquí para el NÚMERO de la lista ---
        p_index_seleccionado = int(p_index_input) - 1 # Ajustar a índice 0-basado
        if 0 <= p_index_seleccionado < len(evento_obj.participantes_inscritos):
            participante_obj = evento_obj.participantes_inscritos[p_index_seleccionado]
            evento_obj.confirmar_asistencia(participante_obj)
        else:
            print("❌ Número de participante inválido.")
    except ValueError:
        print("❌ Entrada inválida. Debe ser un número.")


def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n--- Menú Principal de Gestión de Eventos Deportivos ---")
    print("1. Registrar nuevo evento")
    print("2. Registrar nuevo participante")
    print("3. Inscribir participante en un evento")
    print("4. Asignar equipos a un evento")
    print("5. Consultar eventos por estado")
    print("6. Gestionar estado de un evento")
    print("7. Confirmar asistencia de participante (Organizador)")
    print("0. Salir")
    print("-----------------------------------------------------")

def main():
    """Función principal que ejecuta el programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_evento()
        elif opcion == '2':
            registrar_participante()
        elif opcion == '3':
            inscribir_participante_en_evento()
        elif opcion == '4':
            asignar_equipos_a_evento()
        elif opcion == '5':
            consultar_eventos_por_estado()
        elif opcion == '6':
            gestionar_estado_evento()
        elif opcion == '7':
            confirmar_asistencia_participante()
        elif opcion == '0':
            print("¡Gracias por usar la plataforma! Saliendo del programa.")
            break 
        else:
            print("❌ Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
