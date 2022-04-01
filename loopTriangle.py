# Lab 4 Extra Credit Problem 1
# loopTriangle.py 
# Author: Cody Vantienen
# Date: 11/09/2020
# Purpose - Use nested loops to draw this pattern 
#      *******
#      ******
#      *****
#      ****
#      ***
#      **
#      *

# loop Triangle 
character = "*" # character to print 
size = 7 # number of rows and columns 

# Iterate over the rows 
for row in range(size):
    for col in range(size, row, -1): # makes each row have one less column 
        print(character, end=" ")
    print() 
