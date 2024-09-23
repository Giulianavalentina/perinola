class Apuesta:
    def __init__(self):
        self.fichas = 0 

    def __str__(self):
        return f"Apuesta: {self.fichas} fichas"

    def ponerFicha(self, cuantas=1):
        """Agrega la cantidad especificada de fichas a la apuesta."""
        self.fichas += cuantas
 
    def tomarFicha(self, cuantas=1):
        """Quita la cantidad especificada de fichas de la apuesta. 
        Lanza un error si se intenta sacar más fichas de las que hay."""
        if cuantas > self.fichas:
            raise ValueError(f"No se pueden tomar {cuantas} fichas, solo hay {self.fichas} disponibles.")
        self.fichas -= cuantas

    def tomarTodas(self):
        """Saca todas las fichas de la mesa y devuelve el número de fichas retiradas."""
        todas = self.fichas
        self.fichas = 0
        return todas

    def tieneFicha(self, cuantas=1):
        """Devuelve True si hay al menos la cantidad especificada de fichas."""
        return self.fichas >= cuantas

    def estaVacia(self):
        """Devuelve True si no hay fichas en la mesa."""
        return self.fichas == 0
