#!/usr/bin/env python
#-*- coding:utf-8 -*-

import itertools 
import collections

from plansza import Plansza

from game import Game

paths = []


def play_game(n):
	wyniki = collections.defaultdict(int)
	for _ in xrange(n):
		cnt = 0
		last_moved = True
		plansza = Plansza()

		for color in itertools.cycle(['B', 'W']):
			any_moves = plansza.find_moves(color)
			if not any_moves:	
				print "%s can't make any move\n" % color
				if not last_moved:	# oboje gracze zablokowani
					break
			else:	# czyli są możliwe ruchy
				cnt += 1
				if color == 'B':
					plansza.make_random_move(color)
				elif color == 'W':
					plansza.pick_best_move(color)

			
			print plansza
			print 

			if not plansza._plansza.count('*'):		# cała plansza wypełniona
				break

			last_moved = any_moves

			# s=raw_input('?')
		# plansza.print_score()

		result = plansza.get_result().split()[0]
		print cnt
		wyniki[result] += 1

	print wyniki.items()

def start():
	game = Game()
	game.play()
	



if __name__ == '__main__':
	start()
	
