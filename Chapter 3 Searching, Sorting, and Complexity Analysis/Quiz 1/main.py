#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 2 Quiz 1.

best: O(1)
worst: O(n)
avg.: O(1+2+..+n/n) 
    = O((1+n)*n/2/n) 
    = O(1/2+n/2)
    ≈ O(n)
'''

def sequentialSearch(target: int, lyst: list) -> int:
    '''
    Return the index or -1 if not found.
    Target less than item which means not found.
    '''
    for position, item in enumerate(lyst):
        if target == item:
            return position
        elif target < item:
            return -1
    return -1

def main() -> None:
    L = list(range(0, 20, 2))
    target = 5
    print(sequentialSearch(target, L))

# test
if __name__ == '__main__':
    main()
