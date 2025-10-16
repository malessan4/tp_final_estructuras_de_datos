Un archivo .pkl es un archivo serializado generado por el módulo pickle de Python.

Aquí te lo explico detalladamente:

pickle (el módulo):
pickle es un módulo estándar de Python.
Su propósito principal es serializar y deserializar objetos de Python.
Serializar significa convertir un objeto Python (como una lista, un diccionario, una instancia de clase, etc.) en una secuencia de bytes que puede almacenarse en un archivo o transmitirse a través de una red.
Deserializar (o "cargar") significa tomar esa secuencia de bytes y reconstruir el objeto Python original en la memoria.
.pkl (la extensión):
La extensión .pkl (o a veces .pickle) es una convención común para indicar que el archivo contiene datos serializados por pickle.
No es obligatorio usar .pkl; podrías usar .data, .bin o cualquier otra extensión, pero .pkl ayuda a identificar rápidamente el tipo de archivo.
El contenido del archivo no es legible directamente por un humano como lo sería un archivo .txt. Está en formato binario.
Para qué sirve:
Es útil para guardar el estado exacto de un programa (variables, objetos, listas, etc.) y poder recuperarlo más tarde en otra ejecución del programa.
Es una forma rápida y directa de almacenar objetos Python complejos sin tener que convertirlos manualmente a texto o usar formatos como JSON o XML (que pueden no soportar todos los tipos de objetos de Python o requerir una conversión previa y posterior).