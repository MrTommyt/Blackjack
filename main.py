#!/bin/python

from Partida import Partida
from getpass import getuser
import os


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == '__main__':
    while 1:
        clear()
        partida = Partida(getuser())
        while partida.jugando:
            partida.Turnar()

        if not partida.otra:
            break

    print('Gracias por jugar <3')
