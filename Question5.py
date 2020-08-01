#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:22:22 2020

@author: spaghettifiedcat
"""
def divisor(n):
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x
def triangle_number_generator(n):
    return((n*(n+1))/2)
m = 1
divisors = 0
while divisors < 200:
    triangle_number = triangle_number_generator(m)
    divisors = divisor(m)
    print(str(triangle_number) + ' ' + str(divisors))
    m += 1
print("The triangluar number is: " + str(triangle_number))