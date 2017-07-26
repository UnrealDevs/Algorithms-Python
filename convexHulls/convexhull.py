"""
   Convex Hull's
"""


def readDataPts(filename, N):
    """Reads the first N lines of data from the input file
          and returns a list of N tuples
          [(x0,y0), (x1, y1), ...]
    """
    listPts = []
    lines = open(filename, 'r').readlines()
    for i in range(0,N):
        temp = lines[i].strip().split(" ")
        listPts.append((float(temp[0]),float(temp[1])))
  
    return listPts





def theta(pointA, pointB):
    """Compuets an approximation of the angle between the line AB a horizontal line through A."""
    dx = pointB[0] - pointA[0]
    dy = pointB[1] - pointA[1]
   
    if abs(dx) < 0.000001 and abs(dy) < 0.000001:
        t = 0
    else:
        t = dy/(abs(dx) + abs(dy))
    if dx < 0:
        t = 2 - t
    elif dy < 0:
        t= 4 + t
   
    return t*90






def getRightMostLowest(listPts):
    min_num = listPts[0]
    k = 0
    for index,point in enumerate(listPts):
        if float(point[1]) < float(min_num[1]):
            min_num = point
            k = index
        elif float(point[1]) == float(min_num[1]):
            if float(point[0]) > float(min_num[0]):
                min_num = point
                k = index

    return min_num,k




    
def giftwrap(listPts):
    """Returns the convex hull vertices computed using the
          giftwrap algorithm as a list of 'h' tuples
          [(u0,v0), (u1,v1), ...]    
    """
    min_num, k = getRightMostLowest(listPts) # index and min vaule
    
    listPts.append(min_num) # append to the current points list
    
    v = 0
    i = 0
    while (k !=(len(listPts)-1)):
        listPts[i],listPts[k] = listPts[k],listPts[i] # swap points to get in correct ordering
        minAngle = 361
        for j in range(i+1,len(listPts)):
            angle = theta(listPts[i],listPts[j])
            if angle == 0:
                angle = 360 #return 360 degrees if the angle to the next point is 0, i.e. when points have the same y value
            if angle < minAngle and angle > v and listPts[j] != listPts[i]:
                minAngle = angle
                k = j
        i+=1
        v = minAngle
        
    return listPts[:i]



def isCCW(ptA,ptB,ptC): 
    return ((ptB[0]-ptA[0]) * (ptC[1]-ptA[1]) - (ptB[1] - ptA[1]) * (ptC[0] - ptA[0])>0) 




def grahamscan(listPts):
    """Returns the convex hull vertices computed using the
         Graham-scan algorithm as a list of 'h' tuples
         [(u0,v0), (u1,v1), ...]  
    """

    startingVertex = min(listPts, key=lambda p: (p[1], -p[0])) # lowest y first para, highest x 2nd param finds the min y and rightmost value in the list of points given
    newList  = []
    for i in range(0,len(listPts)):
        newList.append(((listPts[i][0],listPts[i][1]),theta(startingVertex,listPts[i]))) # calculates the angle between the starting point and the current coordinate in the listPts array
        
    newList.sort(key=lambda x: (x[1],x[0][1])) # now sorts the listPts array by angle and if two points are vertical on each other will sort by y value.
    stack = [newList[0][0],newList[1][0],newList[2][0]] #fill stack with first three elements in the list of points
 
    for i in range(3,len(newList)): # starts at the third position in the listPts array
        while not isCCW(stack[-2],stack[-1],newList[i][0]): # looks at the top 2 elements in the stack and the current point to see if it's CCW
                                                                                                                                               
            stack.pop()
        stack.append(newList[i][0]) # add to stack if the three points are CCW
       


   
    return stack[1:] # return stack from second element



def monotoneChaining(listPts):
    """Returns the convex hull vertices computed using 
          a third algorithm
    """
    points = sorted(set(listPts)) # sort the list of points by x, and then by y if there are ties

    upperHull= []
    lowerHull = []
    for p in points:
        while len(lowerHull) >= 2 and not isCCW(lowerHull[-2],lowerHull[-1],p):# checks CCW condition
            lowerHull.pop()
        lowerHull.append(p)

    
    for p in reversed(points):# iterate through the reverse sorted list
        while len(upperHull) >= 2 and not isCCW(upperHull[-2],upperHull[-1],p):# checks CCW condition
            upperHull.pop()
        upperHull.append(p)
      
    return lowerHull[:-1] + upperHull[:-1] # return joined hulls minus their last two elements which are the same


def main():
    listPts = readDataPts('Set_A.dat', 2000)  #File name, numPts given as example only
    #print(giftwrap(listPts))      
    #print (grahamscan(listPts))   
    #print(monotoneChaining(listPts))
    
if __name__  ==  "__main__":
    main()
  
