#!/usr/bin/env python
#-*- coding:utf-8 -*-

from nose.tools import raises

from point import Point

def test_punkt():
    p=Point(0,0)
    assert p.x==0, 'co jest?'

@raises(TypeError)
def test_exception_zero_args():
    p=Point()

@raises(TypeError)
def test_exception_one_arg():
    p=Point(3)

@raises(TypeError)
def test_exception_too_many_args():
    p=Point(3,3,4)