#!/bin/python

from Partida import Partida

if __name__ == '__main__':
    partida = Partida(input('Me gustaría saber tu nombre: '))
    while partida.jugando:
        partida.Turnar()
