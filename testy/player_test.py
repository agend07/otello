#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import raises

from plansza import Plansza
from player import Player
from point import Point

def test_make_player_B():
    player = Player('B')
    assert player.color=='B'
    assert player.enemy=='W'

def test_make_player_W():
    player = Player('W')
    assert player.color=='W'
    assert player.enemy=='B'


@raises(TypeError)
def test_make_player_exception_no_args():
    player = Player()

def test_check_direction_ok_W():
    plansza = Plansza()
    x,y = 3,2
    dir = Point(0,1)
    player = Player('W')
    result = player.check_direction(x, y, dir, plansza)
    assert result==True, 'ruch w tym kierunku powinien być możliwy'

def test_check_direction_wrong_W():
    plansza = Plansza()
    x,y = 3,2
    dir = Point(1,1)
    player = Player('W')
    result = player.check_direction(x, y, dir, plansza)
    assert result==False, 'ruch nieprawidłowy'

def test_check_direction_ok_B():
    plansza = Plansza()
    x,y = 5,3
    dir = Point(-1,0)
    player = Player('B')
    result = player.check_direction(x, y, dir, plansza)
    assert result==True, 'ruch w tym kierunku powinien być możliwy'

def test_check_direction_wrong_B():
    plansza = Plansza()
    x,y = 3,2
    dir = Point(0,1)
    player = Player('B')
    result = player.check_direction(x, y, dir, plansza)
    assert result==False, 'ruch w tym kierunku powinien być możliwy'


def test_find_moves_B():
    plansza = Plansza()
    player = Player('B')

    expected=set([(3, 5), (2, 4), (4, 2), (5, 3)])
    actual = set(player.find_moves(plansza))

    assert (3,5) in actual, 'nie ma mojego ruchu w znalezionych'
    assert (1,1) not in actual, 'tego ruchu ma nie być  znalezionych'
    assert actual==expected

def test_find_moves_W():
    plansza = Plansza()
    player = Player('W')
    expected=set([(2, 3), (3, 2), (4, 5), (5, 4)])
    actual = set(player.find_moves(plansza))

    assert actual==expected

def test_show_moves_W():
    tekst = """ * * * * * * * *
                * * * * * * * *
                * * * + * * * *
                * * + B W * * *
                * * * W B + * *
                * * * * + * * *
                * * * * * * * *
                * * * * * * * * """
    plansza = Plansza()
    player = Player('W')
    result = ''.join(list(player.show_moves(plansza).split()))
    tekst = ''.join(list(tekst.split()))
    assert result==tekst

def test_show_moves_B():
    tekst = """ * * * * * * * *
                * * * * * * * *
                * * * * + * * *
                * * * B W + * *
                * * + W B * * *
                * * * + * * * *
                * * * * * * * *
                * * * * * * * * """
    plansza = Plansza()
    player = Player('B')
    result = ''.join(list(player.show_moves(plansza).split()))
    tekst = ''.join(list(tekst.split()))
    assert result==tekst

def test_make_move_W_2_3():
    player = Player('W')
    plansza = Plansza()
    expected = Plansza()
    tekst = """ * * * * * * * *
                * * * * * * * *
                * * * W * * * *
                * * * W W * * *
                * * * W B * * *
                * * * * * * * *
                * * * * * * * *
                * * * * * * * * """
    expected.load(tekst)
    assert player.make_move(2, 3, plansza) == expected

def test_make_move_W_4_5():
    player = Player('W')
    plansza = Plansza()
    expected = Plansza()
    tekst = """ * * * * * * * *
                * * * * * * * *
                * * * * * * * *
                * * * B W * * *
                * * * W W W * *
                * * * * * * * *
                * * * * * * * *
                * * * * * * * * """
    expected.load(tekst)
    assert player.make_move(4, 5, plansza) == expected

def test_make_move_B_5_3():
    player = Player('B')
    plansza = Plansza()
    expected = Plansza()
    tekst = """ * * * * * * * *
                * * * * * * * *
                * * * * * * * *
                * * * B W * * *
                * * * B B * * *
                * * * B * * * *
                * * * * * * * *
                * * * * * * * * """
    expected.load(tekst)
    assert player.make_move(5, 3, plansza) == expected

def test_make_move_B_5_4():
    player = Player('B')

    plansza = Plansza()
    expected = Plansza()

    start = """ * * * * B * * *
                W * * * W * * *
                * B * * W * * B
                * * B B W * W *
                * * * B W W * *
                B W W W * W W B
                * * * W W W * *
                * * B * B * B * """

    end =   """ * * * * B * * *
                W * * * B * * *
                * B * * B * * B
                * * B B B * B *
                * * * B B B * *
                B B B B B B B B
                * * * B B B * *
                * * B * B * B * """
    plansza.load(start)
    expected.load(end)
    assert player.make_move(5, 4, plansza) == expected

# @raises(AssertionError)
# def test_make_move_not_possible():
#     player=Player('B')
#     plansza = Plansza()
#     player.make_move(1, 1, plansza)

def test_is_player_blocked_B():
    player = Player('B')
    plansza = Plansza()
    player.think_and_move(plansza)
    assert not player.blocked 

def test_is_player_blocked_W():
    player = Player('W')
    plansza = Plansza()
    player.think_and_move(plansza)
    assert not player.blocked 

def test_is_player_blocked_B_True():
    player = Player('B')
    plansza = Plansza()
    tekst = """ * * * * W * * *
                * * * * W * * *
                * * * * W * * *
                * * * * B * * *
                * * * B B * * *
                * * * B * * * *
                * * * * * * * *
                * * * * * * * * """
    plansza.load(tekst)
    player.think_and_move(plansza)
    assert player.blocked

def test_is_player_blocked_W_True():
    player = Player('W')
    plansza = Plansza()
    tekst = """ * * * * W * * *
                * * * * W * * *
                * * * * W * * *
                * * * * B * * *
                * * * B B * * *
                * * * B B * * *
                * * * * B * * *
                * * * * B * * * """
    plansza.load(tekst)
    player.think_and_move(plansza)
    assert player.blocked

def test_player_eq_True():
    p1 = Player('B')
    p2 = Player('B')
    assert p1==p2

def test_player_eq_False():
    p1 = Player('B')
    p2 = Player('W')
    assert p1!=p2