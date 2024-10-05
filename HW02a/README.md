**Assignment Summary:**

Initial Run
|Test ID|Input|Expected Results|Actual Result|Pass or Fail|
|---|---|---|---|---|
|testRightTriangleA|classifyTriangle(3,4,5)|'Right'|'InvalidInput'|Fail|
|testRightTriangleB|classifyTriangle(5,3,4)|'Right'|'InvalidInput'|Fail|
|testEquilateralTriangles|classifyTriangle(1,1,1)|'Equilateral'|'InvalidInput'|Fail|
|testIsocelesTriangles|classifyTriangle(1,2,2)|'Isoceles'|'InvalidInput'|Fail|
|testScaleneTriangles|classifyTriangle(1,2,3)|'Scalene'|'InvalidInput'|Fail|
|testNotTriangles|classifyTriangle(300,1,5)|'InvalidInput'|'InvalidInput'|Pass|

Final Run
|Test ID|Input|Expected Results|Actual Result|Pass or Fail|
|---|---|---|---|---|
|testRightTriangleA|classifyTriangle(3,4,5)|'Right'|'Right'|Pass|
|testRightTriangleB|classifyTriangle(5,3,4)|'Right'|'Right'|Pass|
|testEquilateralTriangles|classifyTriangle(1,1,1) <br> classifyTriangle(199,199,199)|'Equilateral'|'Equilateral'|Pass|
|testIsocelesTriangles|classifyTriangle(1,2,2) <br> classifyTriangle(2,1,2) <br> classifyTriangle(2,2,1)|'Isoceles'|'Isoceles'|Pass|
|testScaleneTriangles|classifyTriangle(1,2,3) <br> classifyTriangle(45,50,43)|'Scalene'|'Scalene'|Pass|
|testNotTriangles|classifyTriangle(300,1,5) <br> classifyTriangle(3,4,9) <br> classifyTriangle(300,1.5,5)|2 x 'InvalidInput' <br> 1 x 'NotATriangle'|2 x 'InvalidInput' <br> 1 x 'NotATriangle'|Pass|

**Test Run Matrix:**
||Test Run 1|Test Run 2|Test Run 3|
|---|---|---|---|
|**Tests Planned**|6|6|6|
|**Tests Executed**|6|6|6|
|**Tests Passed**|1|1|3|
|**Defects Found**|1|1|1|
|**Defects Fixed**|(1) Faulty logic [Line 34] in boolean b <= b should be b <= 0|(1) Faulty Logic [Line 46] Boolean should check if a > (b+c)|(1) Right Triangle Logic|
