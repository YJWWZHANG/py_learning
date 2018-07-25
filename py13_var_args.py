#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hello(greeting, *args):
    if(len(args) == 0):
        print('%s!' % greeting)
    else:
        print('%s, %s!', (greeting, ','.join(args)))

hello('Hi')
hello('Hi', 'Sarah')
hello('hello', 'z1', 'z2', 'z3')

name = ('zqb1', 'zqb2')
hello('hello', *name)