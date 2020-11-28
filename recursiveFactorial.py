#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 15:20:00 2020

@author: parikshitdubey
"""

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)