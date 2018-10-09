# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:18:15 2018

@author: Maverick
"""

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percentage of salary to save, as decimal: '))
total_cost = float(input('Enter the the cost of your dream home: '))
semi_annual_raise = float(input('Enter semi-annual raise, as decimal: '))

portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
numOfMonths = 0

while current_savings < portion_down_payment:
    current_savings += (portion_saved * (annual_salary/12)) + (current_savings * (r/12))
    numOfMonths += 1
    if(numOfMonths % 6 == 0):
        annual_salary += annual_salary * semi_annual_raise
    
print('Number of months:', numOfMonths)