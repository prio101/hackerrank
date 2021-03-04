# https://www.hackerrank.com/challenges/python-print/problem

from __future__ import print_function

if __name__ = '__main__':
    n = int(raw_input())

def print_function(n)
    list = []
    initial_val = 0
    word = ''

    while(inital_val < n):
        result = initial_val + 1
        list.append(result)

        initial_val = result

    for elem in list:
        word += str(elem)

    print(word)

