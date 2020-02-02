#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:25:20 2020

@author: parikshitdubey
"""

def fib(x):
    if x == 1 or x == 0:
        return 1
    else:
        return fib(x-1) + fib(x-2)