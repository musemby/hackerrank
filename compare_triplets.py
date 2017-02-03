#!/bin/python

import sys


a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]


la=[a0,a1,a2]
lb=[b0,b1,b2]

def compare(la, lb):
    alice=0
    bob=0
    for i in range(0,3):
        if la[i] > lb[i]:
            alice = alice + 1
        elif la[i] < lb[i]:
            bob = bob + 1
    print alice,bob

if __name__ == '__main__':
    compare(la, lb)
   