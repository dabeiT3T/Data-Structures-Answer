#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 1 Quiz 4.
'''

def quarterPI(times: int) -> float:
    '''Get 1/4 PI'''
    if times == 1:
        return 1

    sign = 1 if times & 1 else -1
    return 1/(times*2-1)*sign + quarterPI(times-1)

def main() -> float:
    '''Approximate the value of PI'''
    # try-except ValueError
    times = int(input('Please enter the times: '))
    pi = quarterPI(times) * 4
    return pi
# test
if __name__ == '__main__':
    pi = main()
    print(pi)
