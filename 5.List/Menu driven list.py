def add():
    n1=int(input("Enter location : "))
    n2=input("Enter element to insert : ")

    lst.insert(n1,n2)

def remove():
    n=input("Enter element to remove : ")

    lst.remove(n)

    print(n,"removed")

def display():
    print("List :",lst)

def search():
    n=input("Enter element to search : ")

    if n in lst:
        print(n,"is present in list at the location",lst.index(n))
    else:
        print(n, "is not present in the list")


lst=[]

str=input("Enter elements : ")
lst=list(str.split())

print("Created list : ",lst)

n=int
while(n!=6):
    n=int(input("Enter 1]Add  2]Remove  3]Display  4]Search  5]Clear  6]Exit : "))

    if(n==1):
        add()

    elif(n==2):
        remove()

    elif(n==3):
        display()

    elif(n==4):
        search()

    elif(n==5):
        lst.clear()
        print("List cleared")

    elif(n==6):
        exit()

    else:
        print("Incorrect input")




