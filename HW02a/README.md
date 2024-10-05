# **Description of assignment:**

Sometimes you will be given a program that someone else has written, and you will be asked to fix, update and enhance that program.  In this assignment you will start with an existing implementation of the classify triangle program that will be given to you.  You will also be given a starter test program that tests the classify triangle program, but those tests are not complete.

In order to determine if the program is correctly implemented, you will need to update the set of test cases in the test program. You will need to update the test program until you feel that your tests adequately test all of the conditions. Then you should run the complete set of tests against the original triangle program to see how correct the triangle program is. Capture and then report on those results in a formal test report described below. For this first part you should not make any changes to the classify triangle program. You should only change the test program.

Based on the results of your initial tests, you will then update the classify triangle program to fix all defects. Continue to run the test cases as you fix defects until all of the defects have been fixed. Run one final execution of the test program and capture and then report on those results in a formal test report described below.   

Note that you should NOT simply replace the logic with your logic from Assignment 1. Test teams typically don't have the luxury of rewriting code from scratch and instead must fix what's delivered to the test team. 

## **Part 0:**

Create a new folder under your GitHub repository for SSW567 that you have created and shared with the instructor and TA. When creating the new folder, you should include a README file under it. Give your new folder a meaningful name. In our example here we will name our folder for this homework as "hw-02a" but you can name it anything (as long as it makes sense for this assignment).   

Of course, you should have git installed on your laptop, but if you do not then you will need to do that first. You can download git from here: https://git-scm.com/downloadsLinks to an external site. 

Next you should upload and commit both of these files, Triangle.py and TestTriangle.py in their original form to the new folder in your GitHub repo Then any changes you make to these programs will also be committed to the same GitHub repo.

## **Part 1:**

1. Review the Triangle.py file which includes the classifyTriangle() function implemented in Python.  
2. Enhance the set of test cases for the Triangle problem that adequately tests the classifyTriangle() function to find problems. The test cases will be in a separate test program file called TestTriangle.py. You should not fix any bugs in Triangle.py at this time, just make changes to TestTriangle.py
3. Run your test set against the classifyTriangle()
4. Create a test report in the format specified below.  This report shows the results of testing the initial classifyTriangle() implementation.
5. Commit and push your changes to the TestTriangle.py program to GitHub

## **Part 2:**

1. After you've completed part 1 that defines your test set and after running it against the buggy classifyTriangle() function, update the logic in classifytTriangle() to fix all of the logic bugs you found by code inspection and with your test cases.
2. Run the same test set on your improved classifyTriangle() function and create a test report on your improved logic
3. Commit and push your changes to the Triangle.py program to GitHub


----------------------------------------------------------------------------------
# **Assignment Summary:**

### Initial Run
|Test ID|Input|Expected Results|Actual Result|Pass or Fail|
|---|---|---|---|---|
|testRightTriangleA|classifyTriangle(3,4,5)|'Right'|'InvalidInput'|Fail|
|testRightTriangleB|classifyTriangle(5,3,4)|'Right'|'InvalidInput'|Fail|
|testEquilateralTriangles|classifyTriangle(1,1,1)|'Equilateral'|'InvalidInput'|Fail|
|testIsocelesTriangles|classifyTriangle(1,2,2)|'Isoceles'|'InvalidInput'|Fail|
|testScaleneTriangles|classifyTriangle(1,2,3)|'Scalene'|'InvalidInput'|Fail|
|testNotTriangles|classifyTriangle(300,1,5)|'InvalidInput'|'InvalidInput'|Pass|

### Final Run
|Test ID|Input|Expected Results|Actual Result|Pass or Fail|
|---|---|---|---|---|
|testRightTriangleA|classifyTriangle(3,4,5)|'Right'|'Right'|Pass|
|testRightTriangleB|classifyTriangle(5,3,4)|'Right'|'Right'|Pass|
|testEquilateralTriangles|classifyTriangle(1,1,1) <br> classifyTriangle(199,199,199)|'Equilateral'|'Equilateral'|Pass|
|testIsocelesTriangles|classifyTriangle(1,2,2) <br> classifyTriangle(2,1,2) <br> classifyTriangle(2,2,1)|'Isoceles'|'Isoceles'|Pass|
|testScaleneTriangles|classifyTriangle(1,2,3) <br> classifyTriangle(45,50,43)|'Scalene'|'Scalene'|Pass|
|testNotTriangles|classifyTriangle(300,1,5) <br> classifyTriangle(3,4,9) <br> classifyTriangle(300,1.5,5)|2 x 'InvalidInput' <br> 1 x 'NotATriangle'|2 x 'InvalidInput' <br> 1 x 'NotATriangle'|Pass|

### **Test Run Matrix:**
||Test Run 1|Test Run 2|Test Run 3|
|---|---|---|---|
|**Tests Planned**|6|6|6|
|**Tests Executed**|6|6|6|
|**Tests Passed**|1|1|3|
|**Defects Found**|1|1|1|
|**Defects Fixed**|(1) Faulty logic [Line 34] in boolean b <= b should be b <= 0|(1) Faulty Logic [Line 46] Boolean should check if a > (b+c)|(1) Right Triangle Logic|
