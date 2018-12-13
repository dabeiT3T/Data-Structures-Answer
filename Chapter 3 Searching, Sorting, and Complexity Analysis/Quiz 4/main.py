#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 2 Quiz 4.

A little bit complex, maybe this is not the best answer.
The loop count equals to it's binary length + bit 1's count.
For an example: exponent 100,
bin(100) == '0b1100100'
So the count is len('1100100') + 3(This is 3 bits which is 1), which is 10 times.
BTW, a bit-1 means one more step 'number * expoHelper(number, exponent-1)'.

complexity: O(logn+k) ≈ O(logn)
'''

def expo(number: int, exponent: int) -> int:
    '''
    My pow().
    '''
    return expoHelper(number, exponent)
    
def expoHelper(number: int, exponent: int) -> int:
    if exponent == 0: return 1

    if exponent & 1 == 1:
        return number * expoHelper(number, exponent-1)
    else:
        return (expoHelper(number, exponent//2))**2

def main() -> None:
    print(expo(2, 8))

# test
if __name__ == '__main__':
    main()
