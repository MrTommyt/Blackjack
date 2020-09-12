from cards import Baraja, Carta
from jugador import Jugador, Crupier


class Partida:
    def __init__(self, name: str, baraja: Baraja = Baraja(generar=True)):
        self.jugador = Jugador(name, baraja)
        self.crupier = Crupier(baraja)
        self.jugando = True
        self.baraja = baraja

        self.jugador.baraja + self.baraja.getRandom()
        self.crupier.baraja + self.baraja.getRandom()
        self.jugador.baraja + self.baraja.getRandom()

    def Turnar(self):
        self.jugador.mostrarCartas()
        self.crupier.mostrarCartas()

        print(str(self.jugador.baraja.cartas))
        print(str(self.crupier.baraja.cartas))

        self.crupier.Turnar()
        self.jugador.Turnar()

        if self.jugador.acabar or self.crupier.acabar:
            self.acabar()

    def getCarta(self) -> Carta:
        return self.baraja.getRandom()

    def acabar(self):
        j_sum = self.jugador.cardSum
        c_sum = self.crupier.cardSum

        if j_sum > c_sum or c_sum > 21:
            print(f'¡%s Ha ganado con %i puntos!' % (self.jugador.nombre, j_sum))
            print(f'Los %i puntos del Crupier no han sido suficientes para detenerte' % c_sum)
            print('¡Felicidades!')

        elif c_sum > j_sum or j_sum > 21:
            print(f'Los %i no han sido suficientes, %s' % (j_sum, self.jugador.nombre))
            print(f'¡El Crupier ha ganado magistralmente con %i puntos!' % c_sum)
            print('La próxima será')

        self.jugando = False

    def __bool__(self):
        return self.jugando
