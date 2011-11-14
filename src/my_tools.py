#!/usr/bin/env python
#-*- coding:utf-8 -*-

import itertools

def take(iterable, n):
    return list(itertools.islice(iterable, n))

