from cards import Baraja, Carta
from jugador import Jugador

Line = '---------------------------'


class Partida:
    def __init__(self, jugador: Jugador, baraja: Baraja = Baraja(generar=True)):
        self.jugador = jugador
        self.crupier = Crupier(self)
        self.jugando = True
        self.baraja = baraja

        self.jugador.Turnar()
        self.crupier.Turnar()

    def Turnar(self):
        self.jugador.Turnar()
        c_baraja = self.crupier.baraja
        j_baraja = self.jugador.baraja

        print(f'<{Line}>')
        print(f'|%s|%s' % (self.crupier.nombre, self.jugador.nombre))
        print(f'<{Line}>')
        for i in range(len(self.jugador.nombre)):
            print(f'|%i%s|%i%s|' %
                  (c_baraja[i].valor, c_baraja[i].simbolo, j_baraja[i].valor, j_baraja[i].simbolo)
                  )
            print(f'<{Line}>')

        self.crupier.Turnar()

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


class Crupier(Jugador):
    def __init__(self, partida: Partida):
        super().__init__('Crupier', partida)

    def hit(self):
        carta = self.partida.getCarta()

        if carta.figura == 'A':
            if carta.valor + self.cardSum < 21:
                self.cardSum = int(self.baraja) + 11
                self.baraja += carta
            else:
                self.baraja += carta
                self.cardSum = int(self.baraja)
        else:
            self.baraja += carta
            self.cardSum = int(self.baraja)
        if self.cardSum > 21:
            self.partida.acabar()

    def Turnar(self):
        if self.cardSum > 16:
            self.stay()
        else:
            self.hit()
