#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import random


def map_gen(x, y, density):
    print('{}.ox'.format(y))
    indexes = []
    t = []
    for i in range(int(y)):
        for j in range(int(x)):
            if (random.randint(0, int(y)) * 2) < int(density):
                print('o', end='')
            else:
                print('.', end='')
        print('', end='\n')


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Missing parameters.')
        exit()
    map_gen(*sys.argv[1:4])
