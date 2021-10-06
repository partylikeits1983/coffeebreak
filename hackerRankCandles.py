#!/bin/python3

'''
You are in charge of the cake for a child's birthday. 
You have decided the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. 
Count how many candles are tallest.

Example

candles = [3,2,1,3]

The maximum height candles are 3 units high. There are 2 of them, so return 2.

'''

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):    
    x = max(candles)
    y = candles.count(x)
    print(y)

if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
