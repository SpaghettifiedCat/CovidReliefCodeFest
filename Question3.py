#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:13:17 2020

@author: spaghettifiedcat
"""
number = 2**1450
sum = 0
for i in list(str(number)):
    sum += int(i)
print("The sum is: " + str(sum))