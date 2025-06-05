class Add:
    """
    Clase que representa una operación de suma entre dos operandos.

    Attributes:
        left: El operando izquierdo de la suma
        right: El operando derecho de la suma
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self) : return f"({self.left} + {self.right})"


class Mul:
    """
    Clase que representa una operación de multiplicación entre dos operandos.

    Attributes:
        left: El operando izquierdo de la multiplicación
        right: El operando derecho de la multiplicación
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self) : return f"({self.left} * {self.right})"


class Pow:
    """
    Clase que representa una operación de potenciación.

    Attributes:
        base: La base de la potencia
        exponent: El exponente al cual se eleva la base
    """
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def __repr__(self) : return f"({self.base}**{self.exponent})"