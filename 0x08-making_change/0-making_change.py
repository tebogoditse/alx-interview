#!/usr/bin/python3
"""Determines the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    if total < 1:
        return 0
    coins.sort()
    coins.reverse()
    temp = 0
    for i in coins:
        if total <= 0:
            break
        buff = total // i
        temp += buff
        total -= (buff * i)
    if total == 0:
        return temp
    return -1
