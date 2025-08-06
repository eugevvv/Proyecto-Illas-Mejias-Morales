#Este apartado cumple con importar sus funciones al Catalogo
import requests
api = "https://collectionapi.metmuseum.org/public/collection/v1/"

def obtener_departamentos():
    url = f"{api}/ departments"
    try
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            return datos.get("departments", []) #Devolver lista vacía si no se encuentran los departamentos.
        else:
            print(f"Error al contactar la API de departamentos...")
            return [] #lista vacia
    except Exception:
        print(f"Error de conexión con la API: {Exception}")
        return []
def obtener_ID_departamento(id_dpto):
    """
    Obtiene los IDs de todas las obras para un departamento específico.
    """
    url = f"{api}/objects?departmentIds={id_dpto}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            return datos.get('objectIDs', [])
        else:
            print(f"Error al obtener obras del departamento...")
            return []
    except Exception:
        print(f"Error de conexión con la API: {Exception}") 
        return []
def buscar_ID_termino(termino_busqueda):
    """
    Busca obras que coincidan con un término de forma general y efectiva.
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
    """
    Obtiene los detalles completos de una única obra de arte por su ID.
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
