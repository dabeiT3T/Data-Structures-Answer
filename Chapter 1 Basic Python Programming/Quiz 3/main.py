#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 1 Quiz 3.
'''

def main() -> float:
    '''Output the total distance traveled by the ball.'''
    # try-except ValueError
    height  = float(input('Please enter the initial height: '))
    times   = int(input('Please enter the times: '))
    ratio       = 0.6
    distance    = 0
    lastUp      = height
    for n in range(times):
        # last time rasing distance equals this time falling distance
        distance+= lastUp
        # this time rasing distance
        lastUp  *= ratio
        distance+= lastUp
    return distance

# test
if __name__ == '__main__':
    distance = main()
    print(distance)
