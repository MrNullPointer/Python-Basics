#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 15:03:30 2020

@author: parikshitdubey
"""

# def multiply(a,b):
#     result = 0
#     while(b > 0):
#         result += a
#         b -= 1
#     return result


#recursive solution:

def mult(x,y):
    if y == 1:
        return x
    else:
        return x + mult(x,y-1)