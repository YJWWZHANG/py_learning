#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_scores(**kw):
    print('      Name  Scores')
    print('------------------')
    for name, scores in kw.items():
        print('%10s  %d' % (name, scores))

print_scores(zqb1=1, zqb2=2, zqb3=3)

datas = {
    'zqb1':10,
    'zqb2':20,
    'zqb3':30,
}

print_scores(**datas)

def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('    Name:%s' % name)
    print('  Gender:%s' % gender)
    print('    City:%s' % city)
    print('     Age:%s' % age)
    print()

print_info('z1', gender='male', age=20)
print_info('z2', gender='haha', city='gz', age=15)