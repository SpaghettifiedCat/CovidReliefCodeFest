#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:58:53 2020

@author: spaghettifiedcat
"""
#LOOPHOLE
import datetime 
import calendar 
  
date = '18 03 4056'
day_number = datetime.datetime.strptime(date, '%d %m %Y').weekday() 

  
# Driver program 
date = '03 02 2019'
print("The day is " + calendar.day_name[day_number])

