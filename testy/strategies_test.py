#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import nottest, raises, with_setup

from player import Player
from plansza import Plansza
from strategies import NoMoves
from strategies import random_move, best_first_move, get_paths


player = None
plansza = None

def setup():
    global player, plansza
    player = Player('W')
    plansza = Plansza()


@raises(NoMoves)
@with_setup(setup)
def test_random_move_wyrzuca_wyjatek():
    tekst = ''' * * * * * * * *
                * * * * * * * *
                * * * * * * * *
                * * * W W * * *
                * * * W W * * *
                * * * * * * * *
                * * * * * * * *
                * * * * * * * * ''' 
    plansza.load(tekst)
    random_move(player, plansza)

@with_setup(setup)
def test_random_move_zwraca_ruch():
    x, y = random_move(player, plansza)
    assert 0<= x <8
    assert 0<= y <8

@with_setup(setup)
def test_best_first_move_W():
    tekst = ''' * * * * * * * *
                * * * * * * * *
                * * * * W B * *
                * * * W W * * *
                * B B W W * * *
                * * * * * * * *
                * * * * * * * *
                * * * * * * * * ''' 
    plansza.load(tekst)
    move = best_first_move(player, plansza)
    assert move==(4,0)

@with_setup(setup)
def test_best_first_move_B():
    tekst = ''' * * * * * * * *
                * * * * * * * *
                * * * * W B * *
                * * * W W W * *
                * B B W W * * *
                * * * * * * * *
                * * * * * * * *
                * * * * * * * * ''' 
    plansza.load(tekst)
    player = Player('B')
    move = best_first_move(player, plansza)
    assert move==(4,5)

@with_setup(setup)
def test_get_paths_count():
    assert len(list(get_paths(player, plansza, how_deep=3)))==56


@with_setup(setup)
def test_get_paths_count2():
    tekst = """ * * * W B * * *
                W * * * B * * *
                * B * * B * * B
                * * B B B * B *
                * * * B B B * *
                B B B B B B B B
                * * * B B B * *
                * * B * B * B * """

    plansza.load(tekst)
    assert len(list(get_paths(player, plansza, how_deep=3)))==8

@with_setup(setup)
def test_get_paths_count2():
    tekst = """ * * * W B * * *
                W * * * B * * *
                * B * * B * * B
                * * B B B * B *
                * * * B B B * *
                B B B B B B B B
                * * * B B B * *
                * * B * B * B * """

    plansza.load(tekst)
    assert len(list(get_paths(player, plansza, how_deep=3)))==8


@with_setup(setup)
def test_get_paths_count3():
    tekst = """ * * * * W * * *
                * * * * W * * *
                * * * * W * * *
                * * * * B * * *
                * * * B B * * *
                * * * B B * * *
                * * * * B * * *
                * * * * B * * * """
    plansza.load(tekst)
    assert len(list(get_paths(player, plansza, how_deep=3)))==0

@with_setup(setup)
def test_get_paths_count4():
    tekst = ''' B B B B B B B B
                B B B B B B B B
                B B B W B B B B
                B B B B W B B B
                W * W W * W * W
                W W W W W W W W
                W W W W W W W W
                W W W W W W W W ''' 
    plansza.load(tekst)

    # for path in get_paths(player, plansza, how_deep=3):
    #     print path
    assert len(list(get_paths(player, plansza, how_deep=3)))==1
    assert len(list(get_paths(player, plansza, how_deep=3))[0])==2

@with_setup(setup)
def test_get_paths_count5():
    tekst = ''' B B B B B B B B
                B B B B B B B B
                B B B W B B B B
                B B B B W B B B
                W * W W * W * W
                W W W W W W W W
                W W W W W W W W
                W W W W W W W W ''' 
    plansza.load(tekst)
    player = Player('B')

    # for path in get_paths(player, plansza, how_deep=10):
    #     print path
    # assert len(list(get_paths(player, plansza, how_deep=3)))==1
    # assert len(list(get_paths(player, plansza, how_deep=3))[0])==2
