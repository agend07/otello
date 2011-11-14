#!/usr/bin/env python
#-*- coding:utf-8 -*-

def pawns_ratio(plansza, kolor):
    assert kolor in ['W', 'B']
    whites, blacks = plansza.count_pawnsWB()
    if kolor == 'W':
        return float(whites)/blacks
    else:
        return float(blacks)/whites

def pawns_difference(plansza, kolor):
    assert kolor in ['W', 'B']
    whites, blacks = plansza.count_pawnsWB()
    if kolor == 'W':
        return whites - blacks
    else:
        return blacks - whites

def pawns_count(plansza, kolor):
    assert kolor in ['W', 'B']
    whites, blacks = plansza.count_pawnsWB()
    if kolor == 'W':
        return whites
    else:
        return blacks