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
    
    def crear_agregar_alumno(self, nombre, apellido, legajo, telefono, email, direccion, fecha_nacimiento, sexo):
        nuevo_alumno = Alumno(nombre, apellido, legajo, telefono, email, direccion, fecha_nacimiento, sexo)
        self.alumnos.append(nuevo_alumno)
        print(f"Alumno {nombre} {apellido} con legajo {legajo} agregado a la escuela.")

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)
        print(f"Profesor {profesor.nombre} {profesor.apellido} agregado a la escuela.")


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
        print(f"Asignando nota {nota} en {materia} a {alumno.nombre} {alumno.apellido}")
        alumno._agregar_nota(materia, nota)