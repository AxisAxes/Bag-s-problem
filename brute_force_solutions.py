#!/usr/bin/env python
# coding: utf-8


import itertools

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))



def full_bag(bag, itens):
    if bag <= 15 and bag >=0:
        for x in itens:
            if bag <= 15 and bag >=0:
                if bag < 0:
                    print('this is not solution')
                else:
                    bag-=x
                    print('result : {} = {} - {}'.format(bag-x, bag, itens))
            else:
                break
                print('this is not solution')
    else:
        print('end')
   
full_bag(15, itens)

import itertools

itens = [1,1,2,4,12]

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def full_bag(bag, itens):
    p = list(powerset(itens))
    i = [sum(tup) for tup in p]
    for y in i:
        if bag <=15 and bag >= 0:
            result = bag-y
            if result < 0 :
                 print('this is not solution! final result : {}'.format(result))
            elif result == 0:
                 print('The best result: {} >> {} - {} '.format(result,bag,y))
            else:
                 print('result: {} >> {} - {}'.format(result,bag,y))
               
                
full_bag(15,itens)





