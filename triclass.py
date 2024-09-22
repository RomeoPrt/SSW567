'''
Created on 9.19.2024
@author:   Romeo Parreott
Pledge:    I pledge my Honor that I have abided the Stevens Honor System

Triangle Types
- Equilateral: all three sides with the same length
- Isosceles: two sides with the same length
- Scalene: three sides with different lengths
- Right: sides with lengths, a, b, and c where a^2 + b^2 = c^2
'''

def classify_triangle(a, b, c):
    try:
        if a+b+c >= 3 and (a+b+c)%1 == 0: #sides != 0 AND sides are int value
            if a == b and b == c:
                return "Equilateral Triangle"
            else:
                if a != b and b != c and a != c:
                    if a**2 + b**2 == c**2:
                            return "Right Triangle"
                    return "Scalene Triangle"
                else:
                    if a == b or b == c or a == c:
                        return "Isosceles Triangle"
        else: 
            return "Please input positive integer value for Triangle Sides."
    except TypeError:
        return "Please input positive integer value for Triangle Sides."         
