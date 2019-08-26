# Te falta importar la clase A
# Lo que hay en el from es el nombre del archivo y lo que hay en
# import es el nombre de la clase
from A import A

class B(A):
    """Clase B que hereda a la clase A"""

    def __init__(self, first, second, third, other):
        """Constructor de clase B"""

        # Invoca al constructor de clase A
        A.__init__(self, first, second, third)

        # Nuevos atributos
        self.other = other

    def __str__(self):
        """metodo toString de la clase B"""
        return "B: %s, %s, %s." % (self.first, self.second, self.other)
