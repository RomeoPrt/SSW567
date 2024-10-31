# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Romeo Parreott
"""

def classify_triangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    valid_tri = 1
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        valid_tri=-1
    if a > 200 or b > 200 or c > 200:
        valid_tri=-1
    if a <= 0 or b <= 0 or c <= 0:
        valid_tri=-1
    if valid_tri == -1:
        return 'InvalidInput'
    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly greater than the third side
    # of the specified shape is not a triangle
    if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    if a == b and b == c:
        return 'Equilateral'
    if (min(a,b,c)**2) + (((a+b+c)-(min(a,b,c)+max(a,b,c)))**2) == (max(a,b,c)**2):
        return 'Right'
    if (a != b) and (b != c) and (a != c):
        return 'Scalene'
    return 'Isoceles'
