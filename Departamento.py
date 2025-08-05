class Departamento:
    """
    Definición de Clase: Departamento, sus atributos y métodos.
    Representa un departamento y guarda información básica del mismo.
    """
    def __init__(self, id_dpto, nombre_dpto):
        """
        Atributo principal de la clase Departamento

        Args:
            id_dpto (int): ID numérico del departamento.
            nombre_dpto (str): Nombre del departamento.
        """
        self.id_dpto= id_dpto
        self.nombre_dpto= nombre_dpto

    def show(self):
        """
        Muestra la información básica del departamento
        """
        print(f"{self.id.dpto} - {self.nombre_dpto})

