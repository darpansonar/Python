class Student:
    def getinfo(self):
        self.name=str(input("Name : "))
        self.roll=int(input("Roll no. : "))

    def putinfo(self):
        print("NAME    =",self.name)
        print("ROLL NO =",self.roll)
pass

class Marks(Student):
    def getmarks(self):
        Student.getinfo(self)
        print("Enter marks in 3 subjects : ")
        self.m1=int(input("Maths   : "))
        self.m2=int(input("Science : "))
        self.m3=int(input("English : "))

    def putmarks(self):
        Student.putinfo(self)
        self.total=self.m1+self.m2+self.m3
        self.per=self.total*100/300
        print("TOTAL :",self.total)
        print("Percentage : %0.2f" %self.per)
pass

class Result(Marks):
    def getresult(self):
        Marks.getmarks(self)

    def putresult(self):
        Marks.putmarks(self)
pass

n=int(input("Enter no. of students : "))

for i in range(n):
    print("\nStudent",i+1)
    s=Result()
    s.getresult()

    print("\nStudent result : ")
    s.putresult()