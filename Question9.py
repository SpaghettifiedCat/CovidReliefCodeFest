#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:05:19 2020

@author: spaghettifiedcat
"""
s1 = input("What is S1?: ")
s2 = input("What is S2?: ")
def sub(s): 
    sub = []
    for i in range(len(s)): 
        for m in range(i+1,len(s)+1): 
            sub.append(s[i: m]) 
    return(sub)
substrings = sub(s1)
substrings2 = []
for i in substrings:
    if all(item in i for item in s2):
        substrings2.append(i)
min_len = len(s1)
for ele in substrings2:  
    if len(ele) < min_len:  
        min_len = len(ele)  
        res = ele
print("The smallest substring is: " + res)