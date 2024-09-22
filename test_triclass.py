import unittest
import triclass

class Test(unittest.TestCase):

    def testEq(self):
        a = 1
        b = 1
        c = 1
        #test a==b==c
        triangle = triclass.classify_triangle(a, b, c)
        self.assertEqual(triangle, 'Equilateral Triangle') 

    def testIso(self):
        a = 2
        b = 2
        c = 1
        #test a==b
        triangle = triclass.classify_triangle(a, b, c)
        self.assertEqual(triangle, 'Isosceles Triangle')
        a-=1
        c+=1
        #test b==c
        triangle = triclass.classify_triangle(a, b, c)
        self.assertEqual(triangle, 'Isosceles Triangle')
        a+=1
        b-=1
        #test a==c
        triangle = triclass.classify_triangle(a, b, c)
        self.assertEqual(triangle, 'Isosceles Triangle')


    def testScale(self):
        a = 1
        b = 2
        c = 3
        #test a!=b!=c
        triangle = triclass.classify_triangle(a, b, c)
        self.assertEqual(triangle, 'Scalene Triangle')

    def testRight(self):
        a = 3
        b = 4
        c = 5
        a1 = 5
        b1 = 12
        c1 = 13
        #test 3 4 5 and 5 12 13
        triangle1 = triclass.classify_triangle(a, b, c)
        triangle2 = triclass.classify_triangle(a, b, c)
        self.assertEqual(triangle1, 'Right Triangle')
        self.assertEqual(triangle2, 'Right Triangle')
        a*=3
        b*=3
        c*=3
        a1*=3
        b1*=3
        c1*=3
        #test multiples of 3 4 5 and 5 12 13
        triangle1 = triclass.classify_triangle(a, b, c)
        triangle2 = triclass.classify_triangle(a, b, c)
        self.assertEqual(triangle1, 'Right Triangle')
        self.assertEqual(triangle2, 'Right Triangle')

    def testInput(self):
        #test side not a positive int
        a = 1
        b = "hi"
        c = 1
        triangle = triclass.classify_triangle(a, b, c)
        self.assertEqual(triangle, "Please input positive integer value for Triangle Sides.")

        #test side is number but not positive int
        a = 1
        b = 0
        c = 1
        triangle = triclass.classify_triangle(a, b, c)
        self.assertEqual(triangle, "Please input positive integer value for Triangle Sides.")

if __name__ == "__main__":
    unittest.main()