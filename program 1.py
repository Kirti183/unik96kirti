# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Python program to calculate the factorial of a number
#First we ask the user the number whose factorial they want
n = int(input("Enter the number whose factorial you want to calculate "))
factorial = 1;

#loop for calculating the factorial

for i in range(1, n+1):
    factorial = factorial*i
    
#printing the factorial of the number
print("Factorial of the number is", factorial)
