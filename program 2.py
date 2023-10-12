# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:49:28 2023

@author: Kirti Sharma
"""

#Python program to accept list of a numbers and then return the sum and average of the numbers in the list
#first we ask the user to enter the list
lists = input("Enter the list of numbers ")
#Now we define a function which returns the sum and average
def desired_function(lst):
    #now we split the list at white spaces; this gives us entries as strings
    p = lst.split()
    sums = 0
    #This loop is for finding the sum of all the numbers in the list
    for i in range(len(p)):
        sums = sums + int(p[i])
    #Now we find the average of all the numbers of the list    
    average = sums/len(p)
    return sums, average

print("The sum of the list is", desired_function(lists)[0])
print("The average of the list is", desired_function(lists)[1])
