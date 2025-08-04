import requests

def datos_departamentos():
    response = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/departments')
    return response.json()

