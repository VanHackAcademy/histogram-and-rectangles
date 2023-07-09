# VanHack Learning Hub Code Challenge - July 2023

## Histogram and Rectangles

## ***<span style="color:gray">*Question 1*</span>***
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


Example 1:
<br/>
***Input***: heights = [ 2, 1, 5, 6, 2, 3 ]
<br/>
***Output***: 10
<br/>
***Image***:
<br/>
![Histogram Chart](./vh-rectangles-imgs/histogram.jpg "Histogram Chart")
<br/>
***Explanation***: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
******


Example 2:
<br/> 
***Input*** prices = [ 2, 4 ]
<br/>
***Output***: 4
<br/>***Image***:
<br/>
![Histogram Chart](./vh-rectangles-imgs/histogram-1.jpg "Histogram Chart")
<br/>
******



Constraints:
<br/>
1 <= heights.length <= 105
<br/>
0 <= heights[i] <= 104
<br/>
<br/>
Source: [Leetcode 84 - Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/).
******
******
<br/>

## ***<span style="color:gray">*Question 2*</span>***
From **Question 1** above, write a method which returns a hashmap/dictionary/object with the following keys - ***totalPerimeter, totalArea, maxPerimeter, numOfRectangles and maxArea*** of the histogram chart.

### Keys
***totalPerimeter:*** The hashmap/dictionary/object "totalPerimeter" key is the key which holds the total perimeter value of the all the rectangles in the histogram chart.
<br/>
***totalArea:*** The hashmap/dictionary/object "totalArea" key is the key which holds the total area value of the all the rectangles in the histogram chart.
<br/>
***maxPerimeter:*** The hashmap/dictionary/object "maxPerimeter" key is the key which holds the value of the rectangle with the maximum perimeter of the all the rectangles in the histogram chart.
<br/>
***numOfRectangles:*** The hashmap/dictionary/object "numOfRectangles" key is the key which holds the value of the number of rectangles in the histogram chart.
<br/>
***maxArea:*** The hashmap/dictionary/object "maxArea" key is the key which holds the value of the rectangle with the maximum area of all the rectangles in the histogram chart.
<br/>

Example 1:
<br/>
***Input***: rectangleList_1 = [ 2, 1, 5, 6, 2, 3 ] 
<br/>
***Output***: 
{
  'totalPerimeter': 108, 
  'totalArea': 47, 
  'maxPerimeter': 14, 
  'maxArea': 10, 
  'numOfRectangles': 12
}
<br/>
******
<br/>

Example 2:
<br/>
***Input***: rectangleList_2 = [ 2, 4 ]
<br/>
***Output***: 
{
  'totalPerimeter': 24, 
  'totalArea': 10, 
  'maxPerimeter': 10, 
  'maxArea': 4, 
  'numOfRectangles': 3
}
******
<br/>

Example 3:
<br/>
***Input***: rectangleList_3 = [ 3, 7, 9, 16, 4, 7, 6, 2, 10, 8, 9 ]
<br/>
***Output***: 
{
  'totalPerimeter': 410, 
  'totalArea': 269, 
  'maxPerimeter': 34, 
  'maxArea': 21, 
  'numOfRect': 26
}
******
******


### ***You may decide to take a different path in designing and implementing your solution. Happy coding.***

***[VanHack Learning Hub](https://vanhack.com/learning-hub)***