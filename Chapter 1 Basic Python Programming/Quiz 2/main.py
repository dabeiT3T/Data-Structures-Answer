#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 1 Quiz 2.
'''

def main(wagePerHour, routine, overtime) -> float:
    '''Calculate wage.'''
    routineWage     = wagePerHour * routine
    overtimeWage    = wagePerHour * 1.5 * overtime
    return routineWage + overtimeWage

# test
if __name__ == '__main__':
    wagePerHour = 20
    routine     = 40
    overtime    = 5
    wage = main(wagePerHour, routine, overtime)
    print(wage)
