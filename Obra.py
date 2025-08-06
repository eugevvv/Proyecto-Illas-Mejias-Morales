import requests
from PIL import Image

class Obra:
    """
    Definición de Clase: Obra, sus atributos y métodos.
    Guarda todos los detalles de una obra
    Args:
            datos_obra (dict): Variable que nos ayuda a guardar los diferentes datos que tiene un obra a través de la API con la función .get()
            nombre_departamento (str): Variable que guarda los nombres de cada departamento del Museo.
        """
    def __init__(self, datos_obra, nombre_departamento):
        self.id =datos_obra.get("objectID", "ID no disponible")
        self.titulo= datos_obra.get("title", "Obra sin título")
        self.nombre_artista= datos_obra.get("artistDisplayName", "Artista desconocido")
        self.nacionalidad_artista= datos_obra.get("artistNationality", "Nacionalidad desconocida")
        self.fecha_nacimiento_artista= datos_obra.get("artistBeginDate", "No disponible")
        self.fecha_muerte_artista= datos_obra.get("artistEndDate", "No disponible")
        self.tipo=datos_obra.get("classification", "Obra no clasificada")
        self.anio_creacion= datos_obra.get("objectDate", "Fecha desconocida")
        self.url_imagen= datos_obra.get("primaryImageSmall", "Imagen no disponible")
        self.departamento= nombre_departamento

    def show_summary(self):
        """Refleja un resumen de la obra (ID, Título, Artista).
        """
        print(f"   - ID: {self.id} / Título: {self.titulo} / Artista: {self.nombre_artista}")

    def show(self):
        """
        Muestra todos los detalles de una obra y trata de abrir la imagen
        usando las librerías externas: requests y Pillow.
        """
        print("\n-------- Detalles de la Obra Seleccionada ---------")
        print(f"ID: {self.id}")
        print(f"Título: {self.titulo}")
        print(f"Artista: {self.nombre_artista}") 
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento_artista}")
        print(f"Fecha de Fallecimiento: {self.fecha_muerte_artista}")
        print(f"Nacionalidad: {self.nacionalidad_artista}")
        print(f"Departamento: {self.departamento}")
        print(f"Tipo de Obra: {self.tipo}")
        print(f"Año: {self.anio_creacion}")
        print(f"URL de la imagen: {self.url_imagen}")
        print("---------------------------------------------------\n")

        if (self.url_imagen) and (self.url_imagen != 'No disponible'):
            #Si la variables self.url_imagen no está vacía y si dicha variable se encuentra disponible, intentar cargar imagen utilizando get()
            print("Cargando imagen...")
            try: #Para evitar detener el programa
                response = requests.get(self.url_imagen, stream=True) #Gracias al stream, la imagen se descarga en fragmentos pequeños, y no consume memoria.
                #Función del "stream: True"
                if response.status_code == 200:
                    imagen = Image.open(response.raw) #El raw hace que Pillow lea la imagen de forma binaria
                    imagen.show()
                else:
                    print("No se pudo descargar la imagen.")
            except Exception: #Clase utilizada para los errores
                print(f"Ocurrió un error al procesar la imagen...")
        else:
            print("(La obra no tiene una imagen disponible...)")



