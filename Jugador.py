from Cartas import Baraja
import os

Line = '---------------------------'


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Jugador:
    def __init__(self, nombre: str, mazo: Baraja):
        self.nombre = nombre
        self.cardSum = 0
        self.acabar = False
        self.mazo = mazo
        self.baraja = Baraja()

    def hit(self):
        carta = self.mazo.getRandom()

        self.baraja + carta
        self.cardSum = self.baraja.valor

        if self.cardSum > 21:
            self.acabar = True

    def Turnar(self):
        self.cardSum = self.baraja.valor
        while 1:
            try:
                print(f'Por medio del siguiente puede seleccionar las acciones que desea realizar')
                print('1. Hit')
                print('2. Stay')
                respuesta = int(input())

                if (not isinstance(respuesta, int)) or (not respuesta > 0 and not respuesta < 3):
                    raise TypeError

                if respuesta == 1:
                    self.hit()
                elif respuesta == 2:
                    self.stay()
                break
            except TypeError:
                print('El valor ingresado no es un número válido')

        clear()

    def stay(self):
        self.acabar = True

    def mostrarCartas(self):
        space = ' ' * (len(Line) - len(self.nombre) - 7)
        print(f'{Line}--')
        print(f'| [{self.baraja.valor}]\t{self.nombre}{space}|')
        print(f'{Line}--')
        print('|| ', end='')

        for i in range(len(self.baraja)):
            print(f'{str(self.baraja[i].valor)}{self.baraja[i].simbolo}', end='')

            if i < len(self.baraja) - 1:
                print(' | ', end='')

        print(f' ||')
        print(f'{Line}--')
        print()


class Crupier(Jugador):
    def __init__(self, mazo: Baraja):
        super().__init__('Crupier', mazo)

    def hit(self):
        carta = self.mazo.getRandom()

        if carta.figura == 'A':
            if carta.valor + self.cardSum < 21:
                self.cardSum = self.baraja.valor + 11
                self.baraja + carta
            else:
                self.baraja + carta
                self.cardSum = self.baraja.valor
        else:
            self.baraja + carta
            self.cardSum = self.baraja.valor

        if self.cardSum > 21:
            self.acabar = True

    def Turnar(self):
        if self.cardSum < 16:
            self.hit()

    def mostrarCartas(self, mostrar: bool = False):
        space = ' '
        space *= (len(Line) - len(self.nombre) - 7)
        print(f'{Line}--')

        if not mostrar:
            print(f'| [{self.baraja[0].valor}]\t{self.nombre}{space}|')
        else:
            print(f'| [{self.baraja.valor}]\t{self.nombre}{space}|')

        print(f'{Line}--')
        print('|| ', end='')

        for i in range(len(self.baraja)):
            if i > 0 and not mostrar:
                print(f'??', end='')
            else:
                print(f'{str(self.baraja[i].valor)}{self.baraja[i].simbolo}', end='')

            if i < len(self.baraja) - 1:
                print(' | ', end='')

        print(f' ||')
        print(f'{Line}--')
        print()
