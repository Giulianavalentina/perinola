class Ronda:
    def __init__(self):
        """Constructor que inicializa una lista vacía de jugadores."""
        self.jugadores = []

    def __str__(self):
        """Devuelve una representación en cadena de la ronda con los jugadores en orden."""
        return "\n".join([str(jugador) for jugador in self.jugadores])

    def agregarJugador(self, jugador):
        """Agrega un jugador al final de la lista. Lanza un error si el jugador no tiene fichas."""
        if jugador.sinFichas():
            raise ValueError(f"No se puede agregar a {jugador.nombre}, ya que no tiene fichas.")
        self.jugadores.append(jugador)

    def sacarJugadoresSinFichas(self):
        """Elimina a todos los jugadores que no tienen fichas."""
        self.jugadores = [jugador for jugador in self.jugadores if not jugador.sinFichas()]

    def jugadorEnTurno(self):
        """Devuelve el jugador al que le toca el turno (el primero de la lista)."""
        if not self.jugadores:
            return None
        return self.jugadores[0]

    def pasarTurno(self):
        """Pasa el turno al siguiente jugador. El primero se mueve al final de la lista."""
        if self.jugadores:
            jugador = self.jugadores.pop(0)
            self.jugadores.append(jugador)

    def quedaUnSoloJugador(self):
        """Devuelve True si queda solamente un jugador en la ronda."""
        return len(self.jugadores) == 1
