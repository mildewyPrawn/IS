class A(object):
    """Clase que hereda de object"""

    def __init__(self, first, second, third):
        """Constructor de clase A"""
        self.first = first
        self.second = second
        self.third = third

    def __str__(self):
        """metodo toString de la clase A"""
        return "A:%s, %s, %s." % (str(self.first), self.second, self.third)
