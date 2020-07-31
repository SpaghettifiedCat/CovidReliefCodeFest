#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:42:00 2020

@author: spaghettifiedcat
"""

option1=10000+1000 ## bonus added
option2=10000
year=0 
print("Year Option 1 Option 2")
while option2<option1:
    print(str(year)+" "+str(option1)+" "+str(option2))
    option1=option1+0.1*option1
    power=12*(year+1)
    monthlyrate=10/1200
    multiplier=(1+(monthlyrate))**float(power) # '**' is the operation for the power ('^') symbol
    option2=10000*multiplier
    year=year+1

print(str(year)+" "+str(option1)+" "+str(option2))
