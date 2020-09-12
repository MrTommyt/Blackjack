import enum
import random


class Palo(enum.Enum):
    CLUB = ("Club", '♣')
    SPADES = ("Spades", '♠')
    HEARTS = ("Hearts", '♥')
    DIAMONDS = ("Diamonds", '♦')

    def __init__(self, name: str, symbol: str):
        self.symbol = symbol

    @staticmethod
    def getValues() -> list:
        values = []
        for value in Palo:
            values.append(value)

        return values

    @staticmethod
    def getRandomPalo():
        return random.choice(Palo.getValues())


class Valor:
    def __init__(self, value: int, sign):
        self.value = value

        if isinstance(sign, int):
            self.sign = sign
        if isinstance(sign, str):
            self.sign = sign

    @staticmethod
    def getValues() -> list:
        values = []
        for value in Palo:
            values.append(value)

        return values

    @staticmethod
    def getRandomValue() -> Palo:
        return random.choice(Palo.getValues())


class Carta:
    def __init__(self, valor: Valor, palo: Palo = Palo.getRandomPalo()):
        self.valor = valor.value
        self.figura = valor
        self.palo = palo
        self.simbolo = palo.symbol


class Baraja:
    def __init__(self, generar: bool = False, *args):
        self.cartas = []

        if generar:
            for palo in Palo.getValues():
                for valor in getValores():
                    carta = Carta(valor, palo)
                    self.cartas.append(carta)

        else:
            for arg in args:
                if not isinstance(arg, Carta):
                    raise TypeError(arg)

                self.cartas.append(arg)

    def __len__(self):
        return len(self.cartas)

    def __add__(self, other):
        if isinstance(other, Carta):
            self.cartas.append(other)
        elif isinstance(other, Baraja):
            self.cartas.extend(other.cartas)
        elif isinstance(other, list):
            self.cartas += other

    def __iter__(self):
        return self.cartas

    def __int__(self):
        suma = 0
        for carta in self.cartas:
            suma += carta.valor

        return suma

    def getRandom(self) -> Carta:
        index = random.randint(0, len(self.cartas))
        carta = self.cartas[index]
        self.cartas.remove(carta)
        return carta

    def __getitem__(self, item):
        return self.cartas[item]


ACE = Valor(1, 'A')
TWO = Valor(2, '2')
THREE = Valor(3, '3')
FOUR = Valor(4, '4')
FIVE = Valor(5, '5')
SIX = Valor(6, '6')
SEVEN = Valor(7, '7')
EIGHT = Valor(8, '8')
NINE = Valor(9, '9')
TEN = Valor(10, '10')
JACK = Valor(10, 'J')
KING = Valor(10, 'K')
QUEEN = Valor(10, 'Q')

__valores = [ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, KING, QUEEN]


def getValores() -> list:
    return __valores
