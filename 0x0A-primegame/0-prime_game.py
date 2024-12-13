#!/usr/bin/python3
""" 0. Prime Game """


def isWinner(x, nums):
    """ Maria and Ben are playing a game """
    ben = 0
    maria = 0

    for round in range(x):
        playing_numbers = [num for num in range(2, nums[round] + 1)]
        i = 0

        while (i < len(playing_numbers)):
            current_prime = playing_numbers[i]
            index = i + current_prime
            while(index < len(playing_numbers)):
                playing_numbers.pop(index)
                index += current_prime - 1
            i += 1

        prime_count = (len(playing_numbers))
        if prime_count and prime_count % 2:
            maria += 1
        else:
            ben += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
