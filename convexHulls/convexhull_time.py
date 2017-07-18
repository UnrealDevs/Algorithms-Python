"""
   Convex Hull Assignment: COSC262 (2017)
   Student Name: Hayden Taylor
   Usercode: hta55
"""

import time # import python time module for timing algorithms

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

def giftwrapTime(): # giftwrap time test function
    listTimesGift = []
    setValue1 = 0
    averageCalcGift = []
    for k in range(0,15): # run at 15 data sizes
        setValue1 += 2000 # increment the set size by 2000 each time
        for i in range(0,3): # run 3 times at each data size
            listPts = readDataPts('Set_A.dat', setValue1) #read into list
            averageCalcGift.append(giftwrap(listPts))  # add the time to run to list
        listTimesGift.append((averageCalcGift[-3] + averageCalcGift[-2] + averageCalcGift[-1])/3) # calculate the average time for running at each step and add to new list
        
    return listTimesGift

def giftwrap(listPts):
    """Returns the convex hull vertices computed using the
          giftwrap algorithm as a list of 'h' tuples
          [(u0,v0), (u1,v1), ...]    
    """
    start = time.time() # get timestamp
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
                angle = 360 #set angle to 360 degrees if the angle to the next point is 0, i.e. when points have the same y value
            if angle < minAngle and angle > v and listPts[j] != listPts[i]:
                minAngle = angle
                k = j
        i+=1
        v = minAngle

    finish = time.time() # get timestamp
    
    return finish-start # find time it took for algorithm to run


def isCCW(ptA,ptB,ptC):
    return ((ptB[0]-ptA[0]) * (ptC[1]-ptA[1]) - (ptB[1] - ptA[1]) * (ptC[0] - ptA[0])>0) 


def timeGraham():
    listTimesGraham = []
    setValue = 0
    averageCalcGraham = []
    for k in range(0,15):
        setValue += 2000
        listPts = readDataPts('Set_A.dat', setValue)
        for i in range(0,3):
            averageCalcGraham.append(grahamscan(listPts))
        average = (averageCalcGraham[-3] + averageCalcGraham[-2] + averageCalcGraham[-1])  / 3
        listTimesGraham.append(average)


    return listTimesGraham

def grahamscan(listPts):
    """Returns the convex hull vertices computed using the
         Graham-scan algorithm as a list of 'h' tuples
         [(u0,v0), (u1,v1), ...]  
    """
    start = time.time()
    startingVertex = min(listPts, key=lambda p: (p[1], -p[0])) # finds the min y and rightmost value in the list of points given
    newList  = []
    for i in range(0,len(listPts)):
        newList.append(((listPts[i][0],listPts[i][1]),theta(startingVertex,listPts[i]))) # calculates the angle between the starting point and the current coordinate in the listPts array
        
    newList.sort(key=lambda x: (x[1],x[0][1])) # now sorts the listPts array by angle and if two points are vertical on each other will sort by y value.
    stack = [newList[0][0],newList[1][0],newList[2][0]] #fill stack with first three elements in the list of points
 
    for i in range(3,len(newList)): # starts at the third position in the listPts array
        while not isCCW(stack[-2],stack[-1],newList[i][0]): # looks at the top 2 elements in the stack and the current element in the listPts array, if the third
                                                                        #point is CCW then can append that point into the stack, otherwise it will keep poping off the
                                                                        #current until it finds a point that is CCW
            stack.pop()
        stack.append(newList[i][0])

    finish = time.time()

   
    return finish - start

def timeMono():
    listTimesMono = []
    setValue = 0
    averageCalcMono = []
    for k in range(0,15):
        setValue += 2000
        listPts = readDataPts('Set_A.dat', setValue)
        for i in range(0,3):
            averageCalcMono.append(amethod(listPts))
        average = (averageCalcMono[-3] + averageCalcMono[-2] + averageCalcMono[-1]) / 3
        listTimesMono.append(average)
    return listTimesMono

def amethod(listPts):
    """Returns the convex hull vertices computed using 
          a third algorithm
    """
    start = time.time()
    points = sorted(set(listPts)) # sort the list of points by x, and then by y if there are ties

    upperHull= []
    lowerHull = []
    for p in points:
        while len(lowerHull) >= 2 and not isCCW(lowerHull[-2],lowerHull[-1],p): # checks CCW condition
            lowerHull.pop()
        lowerHull.append(p)

    
    for p in reversed(points): # iterate through the reverse sorted list
        while len(upperHull) >= 2 and  not isCCW(lowerHull[-2],lowerHull[-1],p):
            upperHull.pop()
        upperHull.append(p)
    finish = time.time()
    return finish - start


def main():
    ##########################################
    #####Uncomment each to run the timers#####
    ##########################################
    
    #print(giftwrapTime())
    #print(timeMono())
    #print(timeGraham())
if __name__  ==  "__main__":
    main()
  
