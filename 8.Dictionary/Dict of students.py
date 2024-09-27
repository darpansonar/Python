stud={}

n=int(input("Enter no. of students : "))
for i in range(n):
    roll_no=int(input("\nEnter roll no. : "))
    name=input("Enter name : ")
    stud.update({roll_no:name})

print("Dict of students with roll nos. as keys and names as values : ",stud)

c=int
while(c!=6):
    c=int(input("\nEnter 1)Add 2)Remove 3)Display 4)Search 5)Clear 6)Exit : "))

    if(c==1):
        key=int(input("Enter roll no. to add : "))
        value=input("Enter name : ")
        stud.update({key:value})
        print("Roll no. -",key,"with name",value,"is added")

    elif(c==2):
        key = int(input("Enter roll no. to remove : "))
        stud.pop(key)
        print("Roll no. -",key,"is removed")

    elif(c==3):
        print("Dict =",stud)

    elif(c==4):
        key=int(input("Enter roll no. that is to be searched : "))
        for i in stud:
            if(i==key):
                print("Element found in the dict")
        if(i==n):
            print("Element not found in the dict")

    elif(c==5):
        stud.clear()
        print("Dict cleared")

    elif(c==6):
        exit()

    else:
        print("Wrong input")




