#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 3 Quiz 3.

complexity: O(n)
'''

def expo(number: int, exponent: int) -> int:
    '''
    My pow().
    '''
    product = 1;
    for i in range(exponent):
        product *= number
    return product

def main() -> None:
    print(expo(2, 8))

# test
if __name__ == '__main__':
    main()
