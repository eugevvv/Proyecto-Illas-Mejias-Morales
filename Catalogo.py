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
            with open(Nacionalidades, 'r') as archivo:

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

     def cargar_departamentos(self):
         print("Consultando departamentos en el Museo Metropolitano de Arte...")
         datos_dptos = try_api.obtener_departamentos()
         if datos_dptos:
             for dpto_dict in datos_dptos:
                 self.departamentos.append(Departamento(id_dpto=dpto_dict['departamentId'], nombre_dpto=dpto_dict[display_name]))
             print("Departamentos cargados en el sistema...")
         else:
             print("No se pudieron cargar los departamentos")
             exit()





                      
            


                






