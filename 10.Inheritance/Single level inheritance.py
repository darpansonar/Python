class Emp:
    def getdata1(self):
        print("Enter person details : ")
        self.name=str(input("Name : "))
        self.id=int(input("Employee ID : "))

    def putdata1(self):
        print("NAME   =",self.name)
        print("EMP ID =",self.id)
pass

class Salary(Emp):
    def getdata2(self):
        print("Enter salary details : ")
        self.basic=int(input("Basic salary : "))
        self.hra=int(input("HRA : "))
        self.tra=int(input("TRA : "))
        self.da=int(input("DA : "))
        self.total=self.basic+self.hra+self.tra+self.da

    def putdata2(self):
        print("BASIC =",self.basic)
        print("HRA   =",self.hra)
        print("TRA   =",self.tra)
        print("DA    =",self.da)
        print("TOTAL =",self.total)
pass

n=int(input("Enter no. of employees : "))
for i in range(n):
    print("\nEmployee",i+1)
    s=Salary()
    s.getdata1()
    s.getdata2()

    print("\nDisplaying employee Data : ")
    s.putdata1()
    s.putdata2()


