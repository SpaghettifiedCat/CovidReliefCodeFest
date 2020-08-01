#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:22:22 2020

@author: spaghettifiedcat
"""

def triangle_num_generator():
    n = 1
    s = 0
    while 1:
        s += n
        n += 1
        yield s


def triangle_num_naive(n):
    tgen = triangle_num_generator()
    ret = 0
    for i in range(n):
        ret = next(tgen)
    return ret
def divisor_gen(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            if i is not n / i:
                divisors.insert(0, n / i)
    for div in divisors:
        yield div
def divisors(n):
    return [d for d in divisor_gen(n)]
num_divs = 0
i = 1
while num_divs < 200:
    i += 1
    tnum = triangle_num_naive(i)
    divs = divisors(tnum)
    num_divs = len(divs)

print(tnum) 