from Partida import Partida
from cards import Baraja


class Jugador:
    def __init__(self, nombre: str, partida: Partida):
        self.nombre = nombre
        self.cardSum = 0
        self.partida = partida
        self.baraja = Baraja()

        self.cardSum = int(self.baraja)

    def hit(self):
        carta = self.partida.getCarta()
        self.baraja += carta
        self.cardSum = int(self.baraja)
        if self.cardSum > 21:
            self.partida.acabar()

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
        self.partida.acabar()
