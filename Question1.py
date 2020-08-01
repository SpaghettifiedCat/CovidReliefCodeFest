#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:01:10 2020

@author: spaghettifiedcat
"""
word = input("What is the word?: ").strip()
if [char for char in word][0].isupper():
    if len(word.split()) == 1:
        if [char for char in word][len(word) - 1].isnumeric():
            print("The word is valid")
        else:
            print("The word is invalid")
    else:
        print("The word is invalid")
else:
    print("The word is invalid")