# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:40:44 2024

@author: chanboonkwee
"""
import math
from time import time
from mod1 import printme


def timecheck(func):
    def wrapper(*args, **kwargs):
        start = time()
        obj = func(*args, **kwargs)
        stop = time()
        hh = int((stop - start) // 3600)
        mm = int((stop - start) % 3600 // 60)
        ss = int((stop - start) % 60)
        print(f"Duration: {hh:02d}:{mm:02d}:{ss:02d}")
        return obj
    return wrapper

@timecheck
def isPrime(num:int=0) -> bool:
    if num < 3:
        return {0: False, 1: False, 2: True}[num]
    else:
        max_num = math.ceil(num**0.5) + 1
        for i in range(2, max_num):
            if num % i == 0:
                return False
        return True

@timecheck
def findFactors(num:int=0) -> list:
    max_num = num//2 + 1
    return [i for i in range(2, max_num) if num % i == 0]

def check_prime(num:int=0):
    printme(f"{num:3d} is ", 'Prime' if isPrime(num) else 'not Prime')


if __name__=='__main__':
    print(f"17 is {'Prime' if isPrime(17) else 'Not Prime'}")
    printme("97 is ", 'Prime' if isPrime(97) else 'Not Prime')
    for i in range(100):
        check_prime(i)
    check_prime(987654321234)
    # print(repr(findFactors(9999999999)))
'''
>>> print(repr(findFactors(9999999999)))
Duration: 00:14:29
[3, 9, 11, 33, 41, 99, 123, 271, 369, 451, 813, 1353, 2439, 2981, 4059, 8943,
 9091, 11111, 26829, 27273, 33333, 81819, 99999, 100001, 122221, 300003,
 366663, 372731, 900009, 1099989, 1118193, 2463661, 3354579, 4100041, 7390983,
 12300123, 22172949, 27100271, 36900369, 81300813, 101010101, 243902439,
 303030303, 909090909, 1111111111, 3333333333]
'''
