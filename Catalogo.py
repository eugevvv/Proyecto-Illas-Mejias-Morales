from Departamento import Departamento
from Obra import Obra
import try_api

# Nombre del archivo que contiene las nacionalidades
Nacionalidades = 'CH_Nationality_List_20171130_v1.csv'

# Límite de obras a mostrar para que no se crashee.
Limite = 20

class Catalogo:
    """
    Docstring for Catalogo
    Clase principal para gestionar el catálogo
    Carga de departamentos, nacionalidades y la presentación de obras
    """
    def __init__(self):
        """
        Docstring for __init__
        
        :param self:Inicializa las listas de departamentos y nacionalidades
        """
        self.departamentos = []
        self.nacionalidades = []

    def cargar_nacionalidades_desde_csv(self): 
         """
         Docstring for cargar_nacionalidades_desde_csv
        
        :param self:Carga la lista de nacionalidades del csv
        Maneja el error por si el archivo no se encuentra
        """
         print("Cargando lista de nacionalidades de referencia...")

         try:
            with open(Nacionalidades, 'r') as archivo:
            
                archivo.readline()
                
                for linea in archivo:

                    linea_limpia = linea.strip()
                    partes = linea_limpia.split(',')
                    nacionalidad = partes[0]
                    self.nacionalidades.append(nacionalidad)
                    
            print(f"Se cargaron {len(self.nacionalidades)} nacionalidades de referencia...")
            
         except FileNotFoundError:
            print(f"\nOcurrió un error al cargar el archivo")

    def cargar_departamentos(self):
        """
        Docstring for cargar_departamentos
        
        :param self: Consulta la API del museo para cargar los departamentos
        En caso de que falle la carga de datos, se termina la ejecucion  
        """
        print("\nConsultando departamentos en el Museo Metropolitano de Arte...")
        datos_dptos = try_api.obtener_departamentos()
        if datos_dptos:
            for dpto_dict in datos_dptos:
                self.departamentos.append(Departamento(id_dpto=dpto_dict['departmentId'], nombre_dpto=dpto_dict['displayName']))
            print("Departamentos cargados en el sistema...")
        else:
            print("\nNo se pudieron cargar los departamentos.")
            exit()
    
    def presentar_obras(self, todos_los_ids, contexto_busqueda):
        """
             Docstring for presentar_obras
        
        :param self: Muestra las obras de arte en una lista 
        Permite al usuario explorar los detalles de una obra o cargar resultados adicionales
        :param todos_los_ids: Una lista con los IDs únicos de todas las obras
        :param contexto_busqueda: Criterio de busqueda descrito 
     
        """
        if not todos_los_ids:
            print("No se encontraron obras que coincidan con la búsqueda.")
            return

        contador = 0
        while True:
            if contador >= len(todos_los_ids):
                print("\nNo hay más obras que mostrar para esta búsqueda.")
                break

            print(f"\nCargando obras (mostrando de {contador + 1} en adelante)...")
            ids_pagina = todos_los_ids[contador : contador + Limite] #Comienza desde 0 hasta el Limite, que este caso sería 20 obras
            obras_pagina = []
            for id_obra in ids_pagina:
                detalle = try_api.obtener_detalle_obra(id_obra)
                if detalle:
                    obra = Obra(detalle, contexto_busqueda)
                    obras_pagina.append(obra)

            if not obras_pagina:
                print("No se pudieron cargar más detalles de obras.")
                break

            print(f"\n--- Obras Encontradas de {len(todos_los_ids)} totales ---")
            for obra in obras_pagina:
                obra.show_summary()

            print("\n--- ¿Qué deseas hacer? ---")
            print("FAVOR, lea con atención")
            print()
            print("1. Ver detalles de una obra")
            print(f"2. Cargar {Limite} obras más")
            print("3. Volver al menú principal")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                try:
                    id_elegido = int(input("Por favor, introduce el ID de la obra que quieres ver: "))
                    obra_seleccionada = None

                    for obra in obras_pagina:
                        if obra.id == id_elegido:
                            obra_seleccionada = obra
                            break
                
                    if obra_seleccionada:
                        obra_seleccionada.show()
                    else:
                        print("El ID no está disponible en la lista actual.")
                except ValueError:
                    print("Existe un error. Por favor, introduce un número de ID válido.")

            elif opcion == "2":
                contador += Limite
                continue

            elif opcion == "3":
                break

            else:
                print("Opción no válida. Por favor, elige una opción del 1 al 3.")

    def buscar_por_departamento(self):
        """
        Docstring for buscar_por_departamento
    
        :param self:  Se encarga de permitirle al usuario la busqueda en base al ID
        del departamento que requieran. 
        """
        print("\n--- Lista de Departamentos ---")
        for dpto in self.departamentos:
            dpto.show()
        try:
            id_elegido = int(input("\nPor favor, introduce el ID del departamento: "))
            dpto_elegido = None
            
            for dpto in self.departamentos:
                if dpto.id_dpto == id_elegido:
                    dpto_elegido = dpto
                    break
            
            if not dpto_elegido:
                print("ID de departamento no válido.")
                return

            ids_obras = try_api.obtener_ID_departamento(id_elegido)
            self.presentar_obras(ids_obras, dpto_elegido.nombre_dpto)
        except ValueError:
            print("\nError: Por favor, introduce un número válido.")

    def buscar_por_nacionalidad(self):
        """
        Docstring for buscar_por_nacionalidad
        
        :param self: Consulta a la API para permitir la búsqueda de nacionalidades del artista en específico.
        """
        print("\n--- Búsqueda por Nacionalidad del Artista ---")
        if self.nacionalidades:
            nacionalidad_elegida = input("Escribe la nacionalidad en inglés (ej: Italian): ")
        if not nacionalidad_elegida.strip():
            print("Favor, introduzca una nacionalidad correcta.")
            return
        
        ids_obras = try_api.buscar_ID_termino(nacionalidad_elegida)
        self.presentar_obras(ids_obras, f"Nacionalidad: {nacionalidad_elegida}")

    def buscar_por_nombre_autor(self):
        """
        Docstring for buscar_por_nombre_autor
        
        :param self: Busca las obras por medio del nombre facilitado por el usuario. 
        """
        print("\n--- Búsqueda por Nombre del Autor ---")
        nombre_autor = input("Escribe el nombre del autor (ej: Vincent van Gogh): ")
        if not nombre_autor.strip():
            print("Favor, introducir un nombre correcto.")
            return

        ids_obras = try_api.buscar_ID_termino(nombre_autor)
        self.presentar_obras(ids_obras, f"Autor: {nombre_autor}")

    def iniciar_sistema(self):
        """
        Docstring for iniciar_sistema
        
        :param self: Se encarga de almacenar la información de las nacionalidades y los departamentos 
        para darle inicio al sistema completo. Acá es donde el programa empieza.
        """
        print("----------------------------------------------")
        print("     ¡Bienvenido al Catálogo 'MetroArt'!      ")
        print("----------------------------------------------")
        self.cargar_nacionalidades_desde_csv()
        self.cargar_departamentos()

        while True:
            print("\n--- Menú Principal ---")
            print("1. Buscar obras por Departamento")
            print("2. Buscar obras por Nacionalidad del Artista")
            print("3. Buscar obras por Nombre del Autor")
            print("4. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1': 
                self.buscar_por_departamento()
            elif opcion == '2': 
                self.buscar_por_nacionalidad()
            elif opcion == '3': 
                self.buscar_por_nombre_autor()
            elif opcion == '4':
                print("\nGracias por visitar MetroArt...")
                break
            else:
                print("\nOpción no válida. Favor, elige una opción del 1 al 4.")
                      
            


                
















