# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(199,199,199),'Equilateral','199,199,199 should be equilateral')

    def testIsocelesTriangles(self): 
        self.assertEqual(classify_triangle(1,2,2),'Isoceles','1,2,2 should be Isoceles')
        self.assertEqual(classify_triangle(2,1,2),'Isoceles','2,1,2 should be Isoceles')
        self.assertEqual(classify_triangle(2,2,1),'Isoceles','2,2,1 should be Isoceles')

    def testScaleneTriangles(self): 
        self.assertEqual(classify_triangle(1,2,3),'Scalene','1,2,3 should be Scalene')
        self.assertEqual(classify_triangle(45,50,43),'Scalene','45,50,43 should be Scalene')

    def testNotTriangles(self): 
        self.assertEqual(classify_triangle(300,1,5),'InvalidInput')
        self.assertEqual(classify_triangle(3,4,9),'NotATriangle')
        self.assertEqual(classify_triangle(300,1.5,5),'InvalidInput')
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

