class Circle:
    def __init__(self,r):
        self.r=r
    def circle(self):
        pie=3.14
        A=pie*self.r*self.r
        C=2*pie*self.r
        print("area of the circle is",A)
        print("circumference of the circle",C)
R=int(input("enter the radius :"))
s1=Circle(R)
s1.circle()













