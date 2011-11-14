#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random

from estimators import pawns_ratio
#from estimators import  pawns_difference, pawns_count

class NoMoves(Exception):
    pass

"""strategia to metoda która bierze player'a i plansze, a zwraca x,y - 
współrzędne do położenia piona koloru gracza, jeśli nie ma ruchu do 
wykonania wyrzuca wyjątek"""

def random_move(player, plansza):
    moves = player.find_moves(plansza)

    if moves:
        return random.choice(moves)
    else:
        raise NoMoves()

def best_first_move(player, plansza, estimator=pawns_ratio):
    """najlepszy ruch z bieżących - czyli 1 level"""
    moves = player.find_moves(plansza)
    if not moves:
        raise NoMoves()
    # print moves

    method = lambda m: estimator(player.make_move(m[0], m[1], plansza), player.color)
    # m2 = [(method(m), m[0], m[1]) for m in moves]
    # print m2
    return max(moves, key=method)


def best_first_move2(player, plansza, estimator=pawns_ratio):
    """najlepszy ruch z bieżących - czyli 1 level"""
    # moves = player.find_moves(plansza)
    # if not moves:
    #     raise NoMoves()

    method = lambda m: estimator(player.make_move(m[0][0], m[0][1], plansza), player.color)
    # m2 = [(method(m), m[0], m[1]) for m in moves]
    # print m2
    return max(get_paths(player, plansza, how_deep=1), key=method)[0]


def get_paths(player, plansza, how_deep, so_far=[]):
    moves = player.find_moves(plansza)

    if not moves and so_far:
        yield so_far

    for move in moves:
        my_so_far = so_far[:]
        my_so_far.append(move)

        if len(my_so_far) == how_deep:
            yield my_so_far
        else:
            new_plansza = player.make_move(move[0], move[1], plansza)
            enemy = player.get_enemy_player()
            for next_move in get_paths(enemy, new_plansza, how_deep, my_so_far):
                yield next_move

def find_move(player, plansza, how_deep):
    """Oceniam każdą ścieżkę i wybieram max'a"""
    pass

    # return max(
    #     get_paths(player, plansza, how_deep=how_deep),
    #     key = 
    # )


if __name__ == '__main__':
    
    from plansza import Plansza
    from player import Player

    plansza = Plansza()
    player = Player('W')

    for path in get_paths(player, plansza, how_deep=3):
        print path

    print list(get_paths(player, plansza, how_deep=2))
    # todo
    # print best_first_move2(player, plansza)



#     tekst = """ * * * * * * * *
#                 * * * * * * * *
#                 * * * * * * * *
#                 * * * B W * * *
#                 * * * W B * * *
#                 * * * * * * * *
#                 * * * * * * * *
#                 * * * * * * * * """