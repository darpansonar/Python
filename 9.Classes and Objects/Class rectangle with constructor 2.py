class Rectangle:
    l=int
    w=int

    def __init__(self):
        self.l=int(input("Enter length : "))
        self.w=int(input("Enter width : "))

    def area(self):
        self.area=self.l * self.w
        print("Area =",self.area)

    def perimeter(self):
        self.per=2*(self.l + self.w)
        print("Perimeter =",self.per)

#Constructor init() is called as soon as object is created

r1=Rectangle()
print("\nRectangle 1 : ")
r1.area()
r1.perimeter()

print("\n")

r2=Rectangle()
print("\nRectangle 2 : ")
r2.area()
r2.perimeter()