from cards import Baraja, Carta
from jugador import Jugador, Crupier


class Partida:
    def __init__(self, name: str, baraja: Baraja = Baraja(generar=True)):
        self.jugador = Jugador(name, baraja)
        self.crupier = Crupier(baraja)
        self.otra = False
        self.jugando = True
        self.baraja = baraja

        self.jugador.baraja + self.baraja.getRandom()
        self.crupier.baraja + self.baraja.getRandom()
        self.jugador.baraja + self.baraja.getRandom()

    def Turnar(self):
        self.jugador.mostrarCartas()
        self.crupier.mostrarCartas()

        self.crupier.Turnar()
        self.jugador.Turnar()

        if self.jugador.acabar or self.crupier.acabar:
            if len(self.jugador.baraja) > len(self.crupier.baraja):
                self.crupier.Turnar()
            self.acabar()

    def getCarta(self) -> Carta:
        return self.baraja.getRandom()

    def acabar(self):
        j_sum = self.jugador.cardSum
        c_sum = self.crupier.cardSum

        j_dif = abs(j_sum - 21)
        c_dif = abs(c_sum - 21)

        self.jugador.mostrarCartas()
        self.crupier.mostrarCartas(mostrar=True)

        if (c_sum > 21 and j_sum <= 21) or \
                (((21 < j_sum < c_sum) or (21 > j_sum > c_sum)) and (c_sum > 21 or j_dif < c_dif)):
            print(f'¡%s ha ganado con %i puntos!' % (self.jugador.nombre, j_sum))
            print(f'Los %i puntos del Crupier no han sido suficientes para detenerte' % c_sum)
            print('¡Felicidades!')

        elif j_sum == c_sum:
            print('¡Uy! Es un empate')
            print('Esto no se queda así, esto se resolverá en otra ocasión')

        else:
            print(f'Los %i no han sido suficientes, %s' % (j_sum, self.jugador.nombre))
            print(f'¡El Crupier ha ganado magistralmente con %i puntos!' % c_sum)
            print('La próxima será')

        print()
        r = str(input('Dele a enter para jugar otra vez o coloque n y dele a enter para salir '))

        if r == 'n' or r == 'N':
            self.otra = False
        else:
            self.otra = True
        print()

        self.jugando = False

    def __bool__(self):
        return self.jugando
