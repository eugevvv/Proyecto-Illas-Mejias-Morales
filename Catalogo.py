from Departamento import Departamento
from Obra import Obra 
import try_api

Nacionalidades = 'CH_Nationality_List_20171130_v1.csv'
Limite = 10 

class Catalogo

    def __init__(self):
       self.departamentos = []
       self.nacionalidades = []
        
    def cargar_nacionalidades_desde_csv(self):
        print("Cargando lista de nacionalidades de referencia...")
        
        try:
            with open(Nacionalidades, 'r', encoding='utf-8) as archivo:

                 contador_linea = 0 
            
                 for linea in archivo:
                    contador_linea += 1
                     
                     if contador_linea == 1:
                         continue
                     linea_limpia = linea.strip()
                     partes = linea_limpia.split(',')
                     nacionalidad = partes[0]
                     self.nacionalidades.append(nacionalidad)
                     print(f"Se cargaron {len(self.nacionalidades)} nacionalidades de referencia...")
              except:
                     print(f"Ocurrio un error al cargar el archivo")



                       





                      
            


                




