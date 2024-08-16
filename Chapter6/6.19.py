# Return true if point (x2, y2) is on the left side of the
# directed line from (x0, y0) to (x1, y1)
def leftOfTheLine(x0, y0, x1, y1, x2, y2):
    R = ((x1 - x0)*(y2 - y0)) - ((x2 - x0)*(y1 - y0))
    if ( R > 0 ) :
        return True
    elif ( R < 0 ) :
        return False
    
# Return true if point (x2, y2) is on the same
# line from (x0, y0) to (x1, y1)
def onTheSameLine(x0, y0, x1, y1, x2, y2):
    R = ((x1 - x0)*(y2 - y0)) - ((x2 - x0)*(y1 - y0))
    if ( R == 0 ) :
        return True

# Return true if point (x2, y2) is on the
# line segment from (x0, y0) to (x1, y1)
def onTheLineSegment(x0, y0, x1, y1, x2, y2):
     R = ((x1 - x0)*(y2 - y0)) - ((x2 - x0)*(y1 - y0))
     
     xo , yo  = (x1 + x0)/2 , (y1 + y0)/2

     R_p1_po = (((x1-xo)**2)+((y1-yo)**2))**0.5
     R_p2_po = (((x2-xo)**2)+((y2-yo)**2))**0.5
     
     if ( R == 0 ) and (R_p2_po <= R_p1_po ) :
         return True
     elif ( R == 0 ) and (R_p2_po > R_p1_po ) :
         return False    
    

def main():
    x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2:"))
    
    leftOfTheLine(x0, y0, x1, y1, x2, y2)
    onTheSameLine(x0, y0, x1, y1, x2, y2)
    onTheLineSegment(x0, y0, x1, y1, x2, y2)
    
    if leftOfTheLine(x0, y0, x1, y1, x2, y2) == True :
        print("p2 is on the left side of the line from p0 to p1")

    elif leftOfTheLine(x0, y0, x1, y1, x2, y2) == False :
        print("p2 is on the right side of the line from p0 to p1")

    elif onTheLineSegment(x0, y0, x1, y1, x2, y2) == True :
        print("p2 is on the line segment of the line from p0 to p1")

    elif onTheLineSegment(x0, y0, x1, y1, x2, y2) == False :
        print("p2 is not on the line segment of the line from p0 to p1")

    elif onTheSameLine(x0, y0, x1, y1, x2, y2) == True :
        print("p2 is on the same line from p0 to p1")

main()
