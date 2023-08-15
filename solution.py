class Rectangles:
  def __init__(self):
    pass


  def getRectangleProperties(self, rectangleList: list[int]) -> int:
    numOfRect = len(rectangleList)
    maxPerimeter, maxArea, totalPerimeter, totalArea = 0, 0, 0, 0

    for i in rectangleList:
      perimeter = (i + 1) * 2
      totalPerimeter += perimeter
      maxPerimeter = max(maxPerimeter, perimeter)
      area = i
      totalArea += area
      maxArea = max(maxArea, area)
    i = 0
    
    while i < len(rectangleList) - 1:
      for k in range(i + 1, len(rectangleList)):
        if rectangleList[i] < rectangleList[k]:
          currPerimeter = (rectangleList[i] + k - i + 1) * 2
          totalPerimeter += currPerimeter
          maxPerimeter = max(maxPerimeter, currPerimeter)

          currArea = (rectangleList[i] * (k - i + 1))
          totalArea += currArea
          maxArea = max(maxArea, currArea)
          numOfRect += 1
        else:
          break
      i += 1

    return {
      "totalPerimeter" : totalPerimeter,
      "totalArea" : totalArea,
      "maxPerimeter" : maxPerimeter,
      "maxArea" : maxArea,
      "numOfRectangles" : numOfRect
    }



rectangleList_1 = [2,1,5,6,2,3] # Expected Result => {'totalPerimeter': 108, 'totalArea': 47, 'maxPerimeter': 14, 'maxArea': 10, 'numOfRectangles': 12}
rectangleList_2 = [2,4] # Expected Result => {'totalPerimeter': 24, 'totalArea': 10, 'maxPerimeter': 10, 'maxArea': 4, 'numOfRect': 3}
rectangleList_3 = [3, 7, 9, 16, 4, 7, 6, 2, 10, 8, 9] # Expected Result => {'totalPerimeter': 410, 'totalArea': 269, 'maxPerimeter': 34, 'maxArea': 21, 'numOfRect': 26}

sol = Rectangles()
print("the solution is", sol.getRectangleProperties(rectangleList_1))