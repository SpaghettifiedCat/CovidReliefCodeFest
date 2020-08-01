#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:39:44 2020

@author: spaghettifiedcat
"""
initial_seq = input("What is the inital sequence? (provide a space separated string with letters A, B, C, D, and, E denoting the birds): ")
final_seq = input("What is the final sequence? (provide a space separated string with letters A, B, C, D, and, E denoting the birds): ")
initial_seq = initial_seq.split()
final_seq = final_seq.split()
#with A
A = [1, 2, 3, 4, 5][initial_seq.index('A') : final_seq.index('A') + 1] + [1, 2, 3, 4, 5][final_seq.index('A') : initial_seq.index('A') + 1]
B = [1, 2, 3, 4, 5][initial_seq.index('B') : final_seq.index('B') + 1] + [1, 2, 3, 4, 5][final_seq.index('B') : initial_seq.index('B') + 1] 
C = [1, 2, 3, 4, 5][initial_seq.index('C') : final_seq.index('C') + 1] + [1, 2, 3, 4, 5][final_seq.index('C') : initial_seq.index('C') + 1] 
D = [1, 2, 3, 4, 5][initial_seq.index('D') : final_seq.index('D') + 1] + [1, 2, 3, 4, 5][final_seq.index('D') : initial_seq.index('D') + 1] 
E = [1, 2, 3, 4, 5][initial_seq.index('E') : final_seq.index('E') + 1] + [1, 2, 3, 4, 5][final_seq.index('E') : initial_seq.index('E') + 1] 

if any(item in A for item in B):
    print("A and B collided")
if any(item in A for item in C):
    print("A and C collided")
if any(item in A for item in D):
    print("A and D collided")
if any(item in A for item in E):
    print("A and E collided")
if any(item in B for item in C):
    print("B and C collided")
if any(item in B for item in D):
    print("B and D collided")
if any(item in B for item in E):
    print("B and E collided")
if any(item in C for item in D):
    print('C and D collided')
if any(item in C for item in E):
    print('C and E collided')
if any(item in D for item in E):
    print('D and E collided')
