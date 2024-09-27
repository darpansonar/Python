roll=int
name=str
m1=int
m2=int
m3=int

class Student:
    def getdata(self):
        self.roll=int(input("Enter Roll No of student : "))
        self.name=input("Enter name of the student : ")
        self.m1=int(input("Enter marks obtained in Maths out of 100 : "))
        self.m2=int(input("Enter marks obtained in Science out of 100 : "))
        self.m3=int(input("Enter marks obtained in English out of 100 : "))

    def total(self):
        self.t=self.m1 + self.m2 + self.m3
        return self.t

    def percentage(self):
        self.per = (self.t / 300)*100
        return self.per

    def putdata(self):
        print(self.roll,"      ",self.name,"   ",self.total(),"   ",self.percentage())

n=int(input("Enter no. of students : "))
lst=[]

for i in range(n):
    print("\nStudent",i+1)
    s=Student()
    s.getdata()
    lst.append(s)

print("\nResult : ")
print("Roll No.    Name    Total    Per")

for s in lst:
    s.putdata()

c=int
while(c!=3):
    c=int(input("\nEnter  1)Add Student  2)Display details of all students  3)Exit : "))

    if(c==1):
        n=n+1
        print("Student",n)
        a=Student()
        a.getdata()
        lst.append(a)

    elif(c==2):
        print("Roll No.   Name   Total   Per")
        for s in lst:
            s.putdata()

    elif(c==3):
        exit()

    else:
        print("Wrong input")





