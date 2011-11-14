#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Plansza(object):
    """plansza do Otello o rozmiarze 8x8"""

    TEMPLATE = '%s %s %s %s %s %s %s %s\n' * 7 + '%s %s %s %s %s %s %s %s'

    def __init__(self):
        super(Plansza, self).__init__()

        self._plansza = ['*']*64
        self[3, 3] = self[4, 4] = 'B'
        self[3, 4] = self[4, 3] = 'W'

    def __getitem__(self, key):
        x, y = key
        if 0 <= x < 8 and 0 <= y < 8:
            return self._plansza[x * 8 + y]
        else:
            return None

    def __setitem__(self, key, value):
        x, y = key
        self._plansza[x * 8 + y] = value

    def __eq__(self, other):
        assert isinstance(other, Plansza), 'muszę dostać obiekt klasy Plansza do porównania'
        return ''.join(self._plansza) == ''.join(other._plansza)

    def __copy__(self):
        kopia = Plansza()
        kopia._plansza = self._plansza[:]
        return kopia

    def __str__(self):
        return self.TEMPLATE % tuple(self._plansza)

    def load(self, tekst):
        tekst = [letter for letter in list(tekst) if letter in ['B', 'W', '*']]
        assert len(tekst) == 64, 'konieczne 64 znaki' 
        self._plansza = tekst

    def count_pawnsWB(self):
        return self._plansza.count('W'), self._plansza.count('B')
