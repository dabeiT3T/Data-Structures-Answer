#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 3 Quiz 2.

complexity: O(n/2) ≈ O(n)
'''

def reverse(lyst: list) -> None:
    '''
    Reverse the list.
    '''
    for i in range(len(lyst)//2):
        lyst[i], lyst[-(i+1)] = lyst[-(i+1)], lyst[i]

def main() -> None:
    L = list(range(2))
    reverse(L)
    print(L)

# test
if __name__ == '__main__':
    main()
