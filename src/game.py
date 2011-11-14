#!/usr/bin/env python
#-*- coding:utf-8 -*-

import itertools
import collections

from player import Player
from plansza import Plansza

class Game(object):

    def __init__(self, first='W'):
        super(Game, self).__init__()
        self.white, self.black = Player('W'), Player('B')
        self.players = [self.white, self.black] if first == 'W' else [self.black, self.white]
        self.plansza = Plansza()

    def is_finished(self):
        if sum(self.plansza.count_pawnsWB()) == 64:
            return True
        elif self.players[0].blocked and self.players[1].blocked:
            return True
        else:
            return False

    def get_result(self):
        whites, blacks = self.plansza.count_pawnsWB()
        if whites > blacks:
            return "White won: %d to %d" % (whites, blacks)
        elif blacks > whites:
            return "Blacks won: %d to %d" % (blacks, whites)
        else:
            return "Draw %d to %d" % (blacks, whites)

    def play(self):
#        print self.plansza
        for player in itertools.cycle(self.players):
            self.plansza = player.think_and_move(self.plansza)           
#            if player.blocked:
#                print "\n%s can't move" % player.color
#            else:
#                print '\n' + str(self.plansza)
            if self.is_finished():
                break
#        print self.get_result()
        
def play_n_games(n):
    """Play n games and show result: Whites won a time, Blacks won b times,
    Draw c times"""
    
    wyniki = collections.defaultdict(int)
    
    for _ in xrange(n):
        game = Game(first='W')
        game.play()
        result = game.get_result().split()[0]
        wyniki[result] += 1
        
    print wyniki

      
if __name__ == '__main__':
#    game = Game(first='W')
#    game.play()
    play_n_games(10)