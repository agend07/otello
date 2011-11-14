#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import nottest, raises

from game import Game
from player import Player
from plansza import Plansza

def test_game_has_2_players():
    game = Game()
    assert len(game.players) == 2

def test_get_result_draw():
    game = Game()
    assert 'Draw' in game.get_result()

def test_is_finished_at_beging_no_moves():
    game = Game()
    assert game.is_finished() == False

def test_is_finished_later():
    game = Game()
    p1 = Player('W')
    p1.blocked = True
    p2 = Player('B')
    p2.blocked = True
    game.players = [p1, p2]
    assert game.is_finished()

def test_is_finished_full():
    tekst = ''' B B B B B B B B
                B B B B B B B B
                B B B W B B B B
                B B B B W B B B
                W W W W B W W W
                W W W W W W W W
                W W W W W W W W
                W W W W W W W W ''' 
    game = Game()
    p1 = Plansza()
    p1.load(tekst)
    game.plansza = p1
    assert game.is_finished() == True

def test_is_finished_not_full():
    tekst = ''' B B B B B B B B
                B B B B B B B B
                B B B * B B B B
                B B B B W B B B
                W W W W B W W W
                W W W W W W W W
                W W W W W W W W
                W W W W W W W W ''' 
    game = Game()
    p1 = Plansza()
    p1.load(tekst)
    game.plansza = p1
    assert game.is_finished() == False