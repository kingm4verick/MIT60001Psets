# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:32:36 2018

@author: Maverick
"""


def savings(annual_salary, bestSavingsRate):

    semi_annual_raise = 0.07
    
    current_savings = 0
    r = 0.04
    numOfMonths = 36

    for i in range(1, numOfMonths+1):
        if(i % 6 == 0):
            annual_salary += annual_salary * semi_annual_raise
            
        current_savings += (bestSavingsRate * (annual_salary/12)) + (current_savings * (r/12))
        
    return current_savings



annual_salary = float(input('Enter the starting salary: '))
stepsInBisect = 1
total_cost = 1000000.00
portion_down_payment = 0.25 * total_cost
high = 1.0
low = 0.0
guess = (high + low)/2.0


while abs(portion_down_payment - savings(annual_salary, guess)) > 0.000001:

    if savings(annual_salary, guess) < portion_down_payment:
        low = guess
    else:
        high = guess

    guess = (high + low)/2.0
    savings(annual_salary, guess)
    stepsInBisect +=1
    
    if stepsInBisect == 1000:
        print('It is not possible to pay the downpayment in 3 years.')
        break
if abs(portion_down_payment - savings(annual_salary, guess)) < 0.000001:
    print('Best savings rate is:', round(guess, 2))    
    print('steps in bisect is:', stepsInBisect)