import math
from sys import maxsize
delta = 0.000001

class Point(object):
    """Point class with hidden x and y attributes (these must be accessed
    using a method)"""

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
 
    # access methods
    def get_x(self):
        return self._x
 
    def get_y(self):
        return self._y
 
    def set_x(self, x):
        self._x = x
 
    def set_y(self, y):
        self._y = y

    def printPoint(self):
        return self._x,self._y

    # distance between two points
    def distance(self, p):
        dx = self.get_x() - p.get_x()
        dy = self.get_y() - p.get_y()
        return math.sqrt(dx*dx + dy*dy)

    # get the slope of the line defined by two points
    def slope(self,p):
        dx = self.get_x() - p.get_x()
        dy = self.get_y() - p.get_y()
        if dx == 0:
            return maxsize
        else:
            return float(dy)/float(dx)

class Quad(object):

    def __init__(self,point1,point2,point3,point4,inside):
        self._point1 = point1
        self._point2 = point2
        self._point3 = point3
        self._point4 = point4
        self._insidepoint = inside
        self._side1=self._point1.distance(self._point2)
        self._side2=self._point2.distance(self._point3)
        self._side3=self._point3.distance(self._point4)
        self._side4=self._point4.distance(self._point1)
        self._inside1=self._point1.distance(self._insidepoint)
        self._inside2=self._point2.distance(self._insidepoint)
        self._inside3=self._point3.distance(self._insidepoint)
        self._inside4=self._point4.distance(self._insidepoint)
        self._slope1=self._point1.slope(self._point2)
        self._slope2=self._point2.slope(self._point3)
        self._slope3=self._point3.slope(self._point4)
        self._slope4=self._point4.slope(self._point1)
        self._diagonal1=self._point1.distance(self._point3)
        self._diagonal2=self._point2.distance(self._point4)
        
    def get_vertices(self):
        return self._point1.printPoint(),\
        self._point2.printPoint(),\
        self._point3.printPoint(),\
        self._point4.printPoint()

    def get_area(self,a,b,c):
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area

    def total_area(self):
        half1=self.get_area(self._side1,self._side2,self._diagonal1)
        half2=self.get_area(self._side3,self._side4,self._diagonal1)
        return half1+half2

    def get_parallels(self):
        if self._slope1==self._slope3 or self._slope2==self._slope4:
            if self._slope1==self._slope3 and self._slope2==self._slope4:
                return 2
            else: return 1
        else: return 0

    def test_parallelogram(self,parallels):
        if parallels==2:
            return True
        else: return False

    def test_rectangle(self):
        if self._diagonal1==self._diagonal2:
            return True
        else: return False

    def test_rhombus(self):
        if self._side1==self._side2 and self._side2==self._side3 and \
           self._side3==self._side4 and self._side4==self._side1:
            return True
        else: return False

    def test_square(self):
        if self.test_rectangle() and self.test_rhombus():
            return True
        else: return False

    def test_kite(self):
        if (self._side1==self._side2 and self._side3==self._side4) or \
           (self._side2==self._side3 and self._side4==self._side1):
            return True
        else: return False

    def test_trapezoid(self, parallels):
        if parallels==1:
            return True
        else: return False

    def test_isosceles(self):
        if self._diagonal1==self._diagonal2:
            return True
        else: return False

    def test_inside(self):
        t1=self.get_area(self._side1,self._inside1,self._inside2)
        t2=self.get_area(self._side2,self._inside2,self._inside3)
        t3=self.get_area(self._side3,self._inside3,self._inside4)
        t4=self.get_area(self._side4,self._inside4,self._inside1)
        parts = t1+t2+t3+t4
        total = self.total_area()
        return parts-total<delta
    
def main():
    infile = open("QuadCoordinates.txt","r")
    for line in infile:
        c = line.strip().split(' ')
        x1,y1,x2,y2,x3,y3,x4,y4=float(c[0]),float(c[1]),float(c[2]),float(c[3]),\
                                float(c[4]),float(c[5]),float(c[6]),float(c[7])

        print()
        print("******************************************************")
        print("Data from file:",c)
        print("******************************************************")
        print()
        
        p1 = Point(x1,y1)
        p2 = Point(x2,y2)
        p3 = Point(x3,y3)
        p4 = Point(x4,y4)
        inside = Point(x1+2,y1+1)

        q1 = Quad(p1,p2,p3,p4,inside)
        print("The vertices are",q1.get_vertices())
        if q1._slope1==q1._slope2 or q1._slope2==q1._slope3 or \
           q1._slope3==q1._slope4 or q1._slope4==q1._slope1:
            print("Invalid quadrialteral")
            continue
        print("The area is",q1.total_area())
        print("Parallelogram:",q1.test_parallelogram(q1.get_parallels()))
        if q1.test_parallelogram(q1.get_parallels()):
            print("Rectangle:",q1.test_rectangle())
            print("Rhombus:",q1.test_rhombus())
            print("Square:",q1.test_square())
        else: print("\t\ttherefore, it can't be a rectangle, rhombus, or square.")
        print("Kite:",q1.test_kite())
        print("Trapezoid:",q1.test_trapezoid(q1.get_parallels()))
        if q1.test_trapezoid(q1.get_parallels()):
            print("Isosceles trapezoid:",q1.test_isosceles())
        print("(%d,%d) is inside the quadrialteral:" % (x1+2,y1+1),q1.test_inside())
 
main()
