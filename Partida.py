from cards import Baraja, Carta

Line = '---------------------------'


class Jugador:
    def __init__(self, nombre: str, mazo: Baraja):
        self.nombre = nombre
        self.cardSum = 0
        self.acabar = False
        self.mazo = mazo
        self.baraja = Baraja()

        self.cardSum = int(self.baraja)

    def hit(self):
        carta = self.mazo.getRandom()
        self.baraja += carta
        self.cardSum = int(self.baraja)
        if self.cardSum > 21:
            self.acabar = True

    def Turnar(self):
        while 1:
            try:
                print(f'Por medio del siguiente puede seleccionar las acciones que desea realizar, tiene %i'
                      % self.cardSum)
                print('1. Hit')
                print('2. Stay')
                respuesta = input()

                if (not isinstance(respuesta, int)) or (not respuesta > 0 and not respuesta < 3):
                    raise TypeError

                if respuesta == 1:
                    self.hit()
                if respuesta == 2:
                    self.stay()

            except TypeError:
                print('El valor ingresado no es un número válido')

    def stay(self):
        self.acabar = True


def mostrarCartas(jugador: Jugador):
    c_baraja = jugador.baraja

    print(f'<{Line}>')
    print(f'{jugador.nombre}')
    print(f'<{Line}>')
    print('|| ', end='')
    for i in range(len(jugador.nombre)):
        print(f'{c_baraja[i].valor}{c_baraja[i].simbolo}')
        print(' | ', end='')
    print(' ||', end='')


class Partida:
    def __init__(self, name: str, baraja: Baraja = Baraja(generar=True)):
        self.jugador = Jugador(name, baraja)
        self.crupier = Crupier(baraja)
        self.jugando = True
        self.baraja = baraja

        self.jugador.Turnar()
        self.crupier.Turnar()

    def Turnar(self):
        self.jugador.Turnar()

        mostrarCartas(self.jugador)
        mostrarCartas(self.crupier)

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
    def __init__(self, mazo: Baraja):
        super().__init__('Crupier', mazo)

    def hit(self):
        carta = self.mazo.getRandom()

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
            self.acabar = True

    def Turnar(self):
        if self.cardSum > 16:
            self.stay()
        else:
            self.hit()
