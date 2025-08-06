import requests
from PIL import Image

class Obra:
    """
    Definición de Clase: Obra, sus atributos y métodos.
    Guarda todos los detalles de una obra
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
        print(f"   - ID: {self.id} / Título: {self.titulo} / Artista: {self.nombre_artista}")

    def show(self):
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



