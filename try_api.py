#Este apartado cumple con importar sus funciones al Catalogo
import requests
api = "https://collectionapi.metmuseum.org/public/collection/v1/"

def obtener_departamentos():
    """Obtiene la información necesaria de los departamentos de la API del Museo

    Returns:
        list[dict]: Lista de diccionarios, donde cada diccionario representa un departamento del museo. 
        Devuelve una lista vacía si encuentra un error, el cual puede ser por la conexión o por no haber encontrado los departamentos.
    """
    url = f"{api}/ departments"
    try
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            return datos.get("departments", []) #Devolver lista vacía si no se encuentran los departamentos.
        else:
            print(f"Error al contactar la API de departamentos. Código: {response.status_code}")
            return [] #lista vacia
    except Exception:
        print(f"Error de conexión con la API: {Exception}")
        return []
def obtener_ID_departamento(id_dpto):
    """Obtiene los IDs de todas las obras para un departamento específico.

    Args:
        id_dpto (int): El ID del departamento del museo

    Returns:
        list[int]: Lista de ID's de las obras de arte (Convertidas en Objetos). Retorna lista vacía si existe un error.
    """
    url = f"{api}/objects?departmentIds={id_dpto}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            return datos.get('objectIDs', [])
        else:
            print(f"Error al obtener obras del departamento. Código: {response.status_code}")
            return []
    except Exception:
        print(f"Error de conexión con la API: {Exception}") 
        return []
def buscar_ID_termino(termino_busqueda):
    """Busca obras que coincidan con un término que el usuario solicite.

    Args:
        termino_busqueda (str): El concepto de búsqueda que se usará para encontrar las obras que pida el usuario de determinadas opciones.
        La finalidad es que se utilice para las dos opciones que no son alfabéticas al inicio: Nacionalidad y Nombre de Autor.

    Returns:
        list[int]: Lista de ID's de objetos que deben coincidir con el térmico que se está buscando.
        Retorna lista vacía si existe un error o si no se encuentran coincidencias.
    """
    url = f"{api}/search?q={termino_busqueda}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            return datos.get('objectIDs', [])
        else:
            print(f"Error en la búsqueda por término. Código: {response.status_code}")
            return []
    except Exception:
        print(f"Error de conexión con la API: {Exception}")
        return []
def obtener_detalle_obra(id_obra): 
    """Obtiene los detalles completos de una única obra de arte por su ID.

    Args:
        id_obra (int): Está variable guarda el ID de la obra de la cual se quieren obtener detalles.

    Returns:
        dict: Retorna diccionarios con los detalles completos de la obra seleccionada mediante el ID.
        Retorna None si hay un error.
    """
    url = f"{api}/objects/{id_obra}"
    try: 
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception:
        print(f"Error de conexión al buscar obra {id_obra}: {Exception}")
        return None


