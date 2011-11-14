#!/usr/bin/env python
#-*- coding:utf-8 -*-

import copy

from point import Point
from strategies import random_move, NoMoves

class Player(object):
    """docstring for Player"""

    DIRECTIONS = [Point(-1, 0), Point(-1, 1), Point(0, 1), Point(1, 1), Point(1, 0), Point(1, -1), Point(0, -1), Point(-1, -1)]
    
    def __init__(self, color, strategy=random_move):
        super(Player, self).__init__()

        assert color in ['B', 'W'], 'Black or White only (B, W)'
        self.color = color
        self.enemy = 'B' if color == 'W' else 'W'
        self.blocked = False
        self.strategy = strategy

    def __str__(self):
        return self.color

    def __eq__(self, other):
        assert isinstance(other, Player), 'muszę dostać obiekt klasy Player do porównania'
        return self.color == other.color

    def get_enemy_player(self):
        # todo: niepotrzebnie za każdym razem tworzy nowy obiekt - jak wolne to jest?
        return Player('W') if self.color=='B' else Player('B')

    def check_direction(self, x, y, direction, plansza):
        """sprawdza czy jest możliwy w kierunku direction"""
        x, y = x + direction.x, y + direction.y
        if plansza[x, y] != self.enemy:  # pierszy musi być przeciwnego koloru
            return False
        while 1:
            x, y = x + direction.x, y + direction.y
            pole = plansza[x, y]
            if pole == self.enemy:
                continue
            elif pole == self.color:
                return True
            else: 
                return False

    def find_moves(self, plansza):
        available_moves = []
        for x in range(8):
            for y in range(8):
                if plansza[x, y] == '*':
                    for direction in self.DIRECTIONS:
                        if self.check_direction(x, y, direction, plansza):
                            available_moves.append((x, y))
                            break
        return available_moves
    
    def show_moves(self, plansza):
        kopia = copy.copy(plansza)
        moves = self.find_moves(plansza)
        for x in range(8):
            for y in range(8):
                if (x, y) in moves:
                    kopia[x, y] = '+'
        return str(kopia)

    def make_move(self, x, y, plansza):
        """metoda nie zmienia oryginalnej planszy, robi kopię, modyfikuje 
        ją i zwraca"""

        # assert (x,y) in self.find_moves(plansza)
        kopia = copy.copy(plansza)

        for direction in self.DIRECTIONS:
            if self.check_direction(x, y, direction, kopia):
                _x, _y = x, y
                while 1:
                    _x, _y = _x + direction.x, _y + direction.y
                    if kopia[_x, _y] == self.color:
                        break
                    kopia[_x, _y] = self.color

        kopia[x, y] = self.color
        return kopia

    def think_and_move(self, plansza):
        try:
            x, y = self.strategy(self, plansza)
            self.blocked = False
            return self.make_move(x, y, plansza)

        except NoMoves:
            self.blocked = True
            return plansza