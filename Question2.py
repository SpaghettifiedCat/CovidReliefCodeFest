#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:07:19 2020

@author: spaghettifiedcat
"""
bus_a = 293
bus_a_rate = 2.6
bus_b = 130
bus_b_rate = 5
weeks = 0
while bus_b < bus_a:
    bus_a = bus_a*((1 + bus_a_rate/100)**(weeks))
    bus_b = bus_b*((1 + bus_b_rate/100)**(weeks))
    print(str(weeks) + "  " + str(bus_a) + "  " +  str(bus_b))
    weeks += 1
print("The number of weeks is: " + str(weeks - 1))