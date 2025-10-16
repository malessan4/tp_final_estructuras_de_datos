# Esto es un ejemplo de la gestion de alumnos implementando 
# una "base de datos" muy sencilla

import pickle
import os

# Nombre del archivo para persistir los datos
ESCUELA_DATA_FILE = 'escuela_data.pkl'

# se crea la clase Escuela
class Escuela:
    def __init__(self, nombre, direccion, telefono, email):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.alumnos = [] # Lista para almacenar los alumnos de la escuela
        self.profesores = [] # Lista para almacenar los profesores de la escuela

    def mostar_informacion(self):
        return f"Escuela: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Email: {self.email}"

    def _guardar_datos(self):
        """Guarda el estado actual de la escuela (alumnos y profesores) en un archivo."""
        with open(ESCUELA_DATA_FILE, 'wb') as f:
            pickle.dump(self, f)
        print("Datos de la escuela guardados en disco.")

    # --- Nuevos métodos para crear y agregar directamente ---

    def crear_agregar_alumno(self, nombre, apellido, legajo, telefono, email, direccion, fecha_nacimiento, sexo):
        """Crea un nuevo alumno y lo agrega a la escuela."""
        nuevo_alumno = Alumno(nombre, apellido, legajo, telefono, email, direccion, fecha_nacimiento, sexo)
        self.alumnos.append(nuevo_alumno)
        print(f"Alumno {nuevo_alumno.nombre} {nuevo_alumno.apellido} agregado a la escuela.")
        self._guardar_datos() # Guardar despues de agregar
        return nuevo_alumno # Opcional: devolver el objeto creado para su uso posterior

    def crear_agregar_profesor(self, nombre, apellido, legajo, telefono, email, direccion, fecha_nacimiento):
        """Crea un nuevo profesor y lo agrega a la escuela."""
        nuevo_profesor = Profesor(nombre, apellido, legajo, telefono, email, direccion, fecha_nacimiento)
        self.profesores.append(nuevo_profesor)
        print(f"Profesor {nuevo_profesor.nombre} {nuevo_profesor.apellido} agregado a la escuela.")
        self._guardar_datos() # Guardar despues de agregar
        return nuevo_profesor # Opcional: devolver el objeto creado para su uso posterior

    # --- Métodos para agregar instancias ya creadas (opcional, puede mantenerse o eliminarse) ---
    # Si solo usas los nuevos métodos, puedes eliminar estos dos.
    def agregar_alumno(self, alumno):
        if isinstance(alumno, Alumno):
            self.alumnos.append(alumno)
            print(f"Alumno {alumno.nombre} {alumno.apellido} agregado a la escuela.")
            self._guardar_datos()
        else:
            print("Error: El objeto no es una instancia de la clase Alumno.")

    def agregar_profesor(self, profesor):
        if isinstance(profesor, Profesor):
            self.profesores.append(profesor)
            print(f"Profesor {profesor.nombre} {profesor.apellido} agregado a la escuela.")
            self._guardar_datos()
        else:
            print("Error: El objeto no es una instancia de la clase Profesor.")

    # --- Método para cargar datos desde el archivo ---
    @staticmethod
    def cargar_datos(nombre, direccion, telefono, email):
        """
        Intenta cargar una instancia de Escuela desde el archivo.
        Si no existe, crea una nueva con los datos dados.
        """
        if os.path.exists(ESCUELA_DATA_FILE):
            print("Cargando datos de la escuela desde archivo...")
            try:
                with open(ESCUELA_DATA_FILE, 'rb') as f:
                    escuela_cargada = pickle.load(f)
                    # Mantenemos los datos de identificación de la escuela original si es necesario
                    # o se puede verificar que coincidan. Aquí se actualizan con los pasados.
                    escuela_cargada.nombre = nombre
                    escuela_cargada.direccion = direccion
                    escuela_cargada.telefono = telefono
                    escuela_cargada.email = email
                return escuela_cargada
            except (EOFError, pickle.PickleError) as e:
                print(f"Error al cargar los datos: {e}. Se creará una nueva escuela.")
                # Si hay un error, creamos una nueva instancia
                return Escuela(nombre, direccion, telefono, email)
        else:
            print("No se encontraron datos previos. Se creará una nueva escuela.")
            return Escuela(nombre, direccion, telefono, email)


# se crea la clase Alumno

class Alumno:
    def __init__(self, nombre, apellido, legajo, telefono, email, direccion, fecha_nacimiento, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.notas = {} # Diccionario para almacenar las notas por materia

    def mostar_informacion(self):
            return f"Nombre: {self.nombre} {self.apellido}, Legajo: {self.legajo}, Teléfono: {self.telefono}, Email: {self.email}, Dirección: {self.direccion}, Fecha de Nacimiento: {self.fecha_nacimiento}"

    def mostrar_notas(self):
        print(f"Notas de {self.nombre} {self.apellido}:")
        if not self.notas:
            print("No hay notas registradas.")
        else:
            for materia, nota in self.notas.items():
                print(f"{materia}: {nota}")

    def _agregar_nota(self, materia, nota): # Es privado porque el que asigna las notas es el profesor
        self.notas[materia] = nota

# se crea la clase Profesor

class Profesor:
    def __init__(self, nombre, apellido, legajo, telefono, email, direccion, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.cursos = [] # Lista para almacenar los cursos que dicta el profesor

    def mostar_informacion(self):
        return f"Nombre: {self.nombre} {self.apellido}, Legajo: {self.legajo}, Teléfono: {self.telefono}, Email: {self.email}, Dirección: {self.direccion}, Fecha de Nacimiento: {self.fecha_nacimiento}"

    def mostrar_cursos(self):
        print(f"Cursos dictados por {self.nombre} {self.apellido}:")
        if not self.cursos:
            print("No hay cursos asignados.")
        else:
            for curso in self.cursos:
                print(curso)

    def asignar_nota(self, alumno, materia, nota):
        if isinstance(alumno, Alumno):
            print(f"Asignando nota {nota} en {materia} a {alumno.nombre} {alumno.apellido}")
            alumno._agregar_nota(materia, nota)
        else:
            print("Error: El objeto no es una instancia de la clase Alumno.")


# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Crear o cargar la escuela
    nombre_escuela = "Escuela Pythonica"
    direccion_escuela = "Calle Ficticia 123"
    telefono_escuela = "123456789"
    email_escuela = "info@escuelapythonica.edu"

    escuela = Escuela.cargar_datos(nombre_escuela, direccion_escuela, telefono_escuela, email_escuela)

    print("\n--- Información de la Escuela ---")
    print(escuela.mostar_informacion())
    print(f"Alumnos actuales: {len(escuela.alumnos)}")
    print(f"Profesores actuales: {len(escuela.profesores)}")

    # --- Agregar nuevos alumnos y profesores usando los nuevos métodos ---
    # Estas líneas crearán y agregarán automáticamente, guardando en el archivo.
    nuevo_alumno = escuela.crear_agregar_alumno("Ana", "García", "A001", "987654321", "ana@example.com", "Otra Calle 456", "2005-03-10", "F")
    nuevo_profesor = escuela.crear_agregar_profesor("Luis", "Martínez", "P001", "555111222", "luis@escuela.edu", "Calle Docente 789", "1980-07-21")

    print("\n--- Listado de Alumnos Cargados ---")
    for alumno in escuela.alumnos:
        print(alumno.mostar_informacion())

    print("\n--- Listado de Profesores Cargados ---")
    for profesor in escuela.profesores:
        print(profesor.mostar_informacion())

    # --- Ejemplo de uso de asignar nota ---
    if nuevo_alumno and nuevo_profesor:
        nuevo_profesor.asignar_nota(nuevo_alumno, "Matemáticas", 9)
        nuevo_profesor.asignar_nota(nuevo_alumno, "Historia", 8)
        nuevo_alumno.mostrar_notas()
