name=str
runs=int
ip=int   #Innings played
tno=int  #Times not out

class Players:
    def getdata(self):
        self.name=input("Enter name of the player : ")
        self.runs=int(input("Enter total runs scored : "))
        self.ip=int(input("Enter total no. of Innings played : "))
        self.tno=int(input("Enter total no. of times not out : "))

    def putdata(self):
        print(self.name,"    ",self.runs,"    ",self.ip,"    ",self.tno)

pass

n=int(input("Enter no. of players : "))

lst=[]

for i in range(n):
    print("\nStudent",i+1)
    s=Players()
    s.getdata()
    lst.append(s)

print("\nNAME    RUNS    IP    TNO")

for s in lst:
    s.putdata()