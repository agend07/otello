#!/usr/bin/env python
#-*- coding:utf-8 -*-
from plansza import Plansza

def test_load_from_string():

		tekst = '''	* * * * * * * *
					* * * * * * * *
					* * * * W B * *
					* * * B B B * *
					* * * B W * * *
					* * * B W * * *
					* * * * * * * *
					* * * * * * * * '''

		plansza = Plansza()
		plansza.load(tekst)
		assert plansza[1,1]=='*', 'powinna być gwiazdka'
		assert plansza[3,3]=='B', 'powinno być B'

def test_clean_board():
	tekst = '''	* * * * * * * *
				* * * * * * * *
				* * * * * * * *
				* * * B W * * *
				* * * W B * * *
				* * * * * * * *
				* * * * * * * *
				* * * * * * * * '''	
	
	clean = Plansza()
	clean.load(tekst)
	nowa = Plansza()
	assert nowa==clean, 'powinny być takie same'

def test_count_pawnsBW_clean():
	plansza = Plansza()
	whites, blacks = plansza.count_pawnsWB()
	assert blacks==2 and whites==2, 'liczba pionów się nie zgadza'

def test_count_pawnsBW():
	tekst = '''	B B B * * * * *
				* * * * * * * *
				* * * * * * * *
				* * * B W * * *
				* * * W B * * *
				* * * * * * * *
				* * * * * * * *
				* * * * * W W W '''	
	plansza = Plansza()
	plansza.load(tekst)
	w, b = plansza.count_pawnsWB()
	assert w==5 and b==5


# class PlanszaTest(unittest.TestCase):

	# def test_znalezione_ruchy(self):
	# 	plansza = Plansza()
	# 	plansza.find_moves('B')
	# 	expected=set([(3, 5), (2, 4), (4, 2), (5, 3)])
	# 	actual = set(plansza.available_moves)
	# 	self.assertEqual(actual, expected)

	# def test_wykonal_ruch(self):
	# 	plansza = Plansza()
	# 	plansza.make_move(3, 5, 'B')

	# 	self.assertEqual(plansza[3,5], 'B')
	# 	self.assertEqual(plansza[3,4], 'B')

	# def test_wykonal_ruch2(self):
	# 	plansza = Plansza()
	# 	plansza.make_move(5, 4, 'W')

	# 	self.assertEqual(plansza[5,4], 'W')
	# 	self.assertEqual(plansza[4,4], 'W')

	# def test_wykonal_ruch3(self):
		
	# 	start = '''		* * * * * W * *
	# 					* * * * * B * *
	# 					* * * * W B * *
	# 					* * * B B B * *
	# 					* * * B W * W B
	# 					* * * B W B W *
	# 					* * * * * W * B
	# 					* * * * * * * * '''
		
	# 	expected = '''	* * * * * W * *
	# 					* * * * * B * *
	# 					* * * * W B * *
	# 					* * * B B B * *
	# 					* * * B B B B B
	# 					* * * B W B B *
	# 					* * * * * W * B
	# 					* * * * * * * *'''

		# plansza = Plansza()
		# plansza.load(start)
		# plansza.make_move(4,5,'B')

		# end=Plansza()
		# end.load(expected)

		# self.assertEqual(plansza, end)

	


#if __name__ == '__main__':
#	unittest.main()


		
		
		
		