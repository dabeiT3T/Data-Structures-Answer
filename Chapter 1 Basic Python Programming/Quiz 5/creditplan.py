#!/usr/bin/env python3
'''
Author: dabei
My answer to Chapter 1 Quiz 5.
'''

class CreditPlan:
    '''Display a table, with appropriate headers, of a payment schedule
    for the lifetime of the loan.'''

    # Constructor
    def __init__(self, purchasePrice: float):
        '''Sets up the credit plan'''
        self._purchasePrice     = purchasePrice
        self._yearlyInterestRatio   = 0.12
        self._monthlyInterestRatio  = self._yearlyInterestRatio / 12
        self._downPayment       = self._purchasePrice * 0.1
        self._monthlyPayment    = (self._purchasePrice-self._downPayment)*0.05
        self._totalInterest     = 0.00
        self._monthCost         = self.monthCost(0, self._purchasePrice)
        self._totalPayment      = self._purchasePrice + self._totalInterest

    
    # method
    def monthCost(self, month: int, left) -> int:
        '''Get the month spent on returning money and the total interest.'''
        month += 1
        # interest this month
        interest = left * self._monthlyInterestRatio
        # self._totalInterest = 0 before calling monthCost
        # or u should not use self._totalInterest
        self._totalInterest += interest
        # at the beginning of the month
        left += interest

        if round(left, 2) <= round(self._monthlyPayment, 2):
            return month

        # at the end of the month
        left -= self._monthlyPayment
        return self.monthCost(month, left)

    def printTitle(self) -> None:
        '''Print title'''
        print(
            'month',
            'total_balance_owed',
            'interest_owed',
            'principal_owed',
            'payment',
            'balance_remaining'
        )

    def printRow(self, *col) -> None:
        '''Print row'''
        string = '%5d %18.2f %13.2f %14.2f %7.2f %17.2f'%col
        print(string)

    def printPlan(self) -> None:
        '''Print plan'''
        left = self._totalPayment
        
        self.printTitle()

        for month in range(1, self._monthCost+1):
            interestOwed    = left * self._monthlyInterestRatio
            monthlyPayment  = self._monthlyPayment if left >= self._monthlyPayment else left
            principalOwed   = monthlyPayment - interestOwed
            
            self.printRow(
                month,
                left,
                interestOwed,
                principalOwed,
                monthlyPayment,
                left-monthlyPayment
            )

            left -= self._monthlyPayment
    
# test
if __name__ == '__main__':
    # try-except ValueError
    purchasePrice = float(input('Please enter the purchase price: '))
    # purchasePrice must above 0.1
    creditPlan = CreditPlan(purchasePrice)
    creditPlan.printPlan()

'''
here is a sample
Please enter the purchase price: 100
month total_balance_owed interest_owed principal_owed payment balance_remaining
    1             113.66          1.14           3.36    4.50            109.16
    2             109.16          1.09           3.41    4.50            104.66
    3             104.66          1.05           3.45    4.50            100.16
    4             100.16          1.00           3.50    4.50             95.66
    5              95.66          0.96           3.54    4.50             91.16
    6              91.16          0.91           3.59    4.50             86.66
    7              86.66          0.87           3.63    4.50             82.16
    8              82.16          0.82           3.68    4.50             77.66
    9              77.66          0.78           3.72    4.50             73.16
   10              73.16          0.73           3.77    4.50             68.66
   11              68.66          0.69           3.81    4.50             64.16
   12              64.16          0.64           3.86    4.50             59.66
   13              59.66          0.60           3.90    4.50             55.16
   14              55.16          0.55           3.95    4.50             50.66
   15              50.66          0.51           3.99    4.50             46.16
   16              46.16          0.46           4.04    4.50             41.66
   17              41.66          0.42           4.08    4.50             37.16
   18              37.16          0.37           4.13    4.50             32.66
   19              32.66          0.33           4.17    4.50             28.16
   20              28.16          0.28           4.22    4.50             23.66
   21              23.66          0.24           4.26    4.50             19.16
   22              19.16          0.19           4.31    4.50             14.66
   23              14.66          0.15           4.35    4.50             10.16
   24              10.16          0.10           4.40    4.50              5.66
   25               5.66          0.06           4.44    4.50              1.16
   26               1.16          0.01           1.15    1.16              0.00
'''
