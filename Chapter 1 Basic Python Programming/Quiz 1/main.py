#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 1 Quiz 1.
'''

import math

def main() -> tuple:
    '''Get Cube's diameter, circumference, surface area and volume.'''
    # try-except ValueError
    radius = float(input('Please enter the radius: '))
    diameter        = 2 * radius
    circumference   = 2 * math.pi * radius
    surfaceArea     = 4 * math.pi * radius ** 2
    volume          = 4 / 3 * math.pi * radius ** 3
    return diameter, circumference, surfaceArea, volume

# test
if __name__ == '__main__':
    cube = main()
    print('diameter:', cube[0])
    print('circumference:', cube[1])
    print('surface area:', cube[2])
    print('volume:', cube[3])
