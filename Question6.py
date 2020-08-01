#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:25:17 2020

@author: spaghettifiedcat
"""
n = 1000
for i in range(1, int(n / 3) + 1):  
    for j in range(i + 1, int(n / 2) + 1):  
        k = n - i - j 
        if (i * i + j * j == k * k):  
            print("The triplet is:")
            print(i, ", ", j, ", ",  k, sep = "") 
print("The product is :" + str(i*j*k))