#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 1 Quiz 5.
'''

class CreditPlan:
    '''Display a table, with appropriate headers, of a payment schedule
    for the lifetime of the loan.'''

    
    # try-except ValueError
    purchasePrice = float(input('Please enter the purchase price: '))

    yrInterest  = 0.12
    monInterest = yrInterest / 12
    downPayment = purchasePrice * 0.1
    # the monthly payment
    payment     = (balanceOwed - downPayment) * 0.5
    balanceOwed = purchasePrice
    month       = 0
    while True:
        # the month number
        month   += 1
        # the interest owed
        interestOwed = balanceOwed * monInterest

        # the amount of principal owed
        principalOwed = payment - interestOwed
    
# test
if __name__ == '__main__':
    main()
