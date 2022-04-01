# Midterm Question 26
# shipping.py 
# Author: Cody Vantienen
# Date: 11/12/2020
# Purpose - Create a program where a user can enter the weight of a packadge
# and then calulates and displays the shipping charges
# Notes: 
# Rates per pound depending on weight,  
# Two or less = $1.50
# Over two less than six = $3.00
# Over six less than ten = $4.00
# Over 10 = $4.75

# Name  the constants for cost of shipping
RATE_PER_POUND_ONE = 1.50
RATE_PER_POUND_TWO = 3.00
RATE_PER_POUND_THREE = 4.00
RATE_PER_POUND_FOUR = 4.75

# Assign initail values and set to zero
packadgeWeight = 0.0 # weight entered by user
shippingRate = 0.0 # Rate given to user depending on weight entered
shippingCharge = 0.0 # total cost of shipping 

# Have user input the weight if packadge using float to allow decimal value
packadgeWeight = float(input("Enter the weight of the packadge in pounds: "))

# Algorithm / conditional processing 
# use if statement to calculate the shipping rate based on the weight
if packadgeWeight > 10:
    shippingRate = RATE_PER_POUND_FOUR
elif packadgeWeight > 6: 
    shippingRate = RATE_PER_POUND_THREE
elif packadgeWeight >2:
    shippingRate = RATE_PER_POUND_TWO
else:
    shippingRate = RATE_PER_POUND_ONE 

# Calculate the cost of shipping 
shippingCharge = packadgeWeight * shippingRate 

# add blank print statement to create new line to make more readable 
#  use print and format to two decimal places 
print()
print("Shipping charge: $" + format(shippingCharge,'.2f'))
