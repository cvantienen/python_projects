
# Chapter 2 Lab Problem 1 # salesPredictor.py
# Author: Cody Vantienen
# Date: 9/30/20
# Purpose: Write a program that calulates the projected total 
#          profit, given the user enters the total sales amount.
# Notes: projected profits are 23% of sales 

#input Section
totalSales = int(input("Please enter the yearly sales total: "))
print()
# processing Section
profitAmount = totalSales * .23
projectedProfit = profitAmount + totalSales

# output Section
print("The projected profit for the year is", projectedProfit) 

#end 