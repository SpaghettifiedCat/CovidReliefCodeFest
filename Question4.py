#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:16:02 2020

@author: spaghettifiedcat
"""
code = list(str(input("What is the code?: " )))
guess = list(str(input("What is the guess?: ")))
correct = 0
correct_but_wrong = 0
for i in range(len(code)):
    if guess[i] == code[i]:
        correct += 1
    if guess[i] in code:
        correct_but_wrong += 1
print("The number of correct guesses in the correct positions are: " + str(correct))
print("The number of correct guesses in wrong positions are " + str(correct_but_wrong))
    