class Jugador:
    def __init__(self, nombre, fichas=5):
        """Constructor que inicializa el nombre y la cantidad de fichas del jugador."""
        self.nombre = nombre
        self.fichas = fichas

    def __str__(self):
        return f"{self.nombre}, {self.fichas} fichas"

    def darFicha(self, cuantas=1):
        """Agrega la cantidad especificada de fichas al jugador."""
        self.fichas += cuantas

    def sacarFicha(self, cuantas=1):
        """Le quita la cantidad especificada de fichas al jugador.
        Lanza un error si se intenta sacar más fichas de las que el jugador tiene."""
        if cuantas > self.fichas:
            raise ValueError(f"No se pueden sacar {cuantas} fichas, solo tienes {self.fichas}.")
        self.fichas -= cuantas

    def tieneFicha(self, cuantas=1):
        """Devuelve True si el jugador tiene al menos la cantidad especificada de fichas."""
        return self.fichas >= cuantas

    def sinFichas(self):
        """Devuelve True si el jugador no tiene fichas."""
        return self.fichas == 0
