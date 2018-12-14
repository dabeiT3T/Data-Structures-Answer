#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 3 Quiz 5.
'''

from random import shuffle

def selectionSort(lyst: list, reverse: bool = False) -> None:
    for i in range(len(lyst)-1):
        target = i
        for j in range(i+1, len(lyst)):
            if lyst[target] > lyst[j] and not reverse:
                target = j
            elif lyst[target] < lyst[j] and reverse:
                target = j

        if target != i:
            swap(lyst, target, i)

def swap(lyst: list, left: int, right: int) -> None:
    lyst[left], lyst[right] = lyst[right], lyst[left]

def main() -> None:
    L = list(range(20))
    shuffle(L)
    print(L)
    selectionSort(L, True)
    print(L)

# test
if __name__ == '__main__':
    main()
