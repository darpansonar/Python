lst=[]

n=int(input("Enter no. of elements in set : "))
print("Enter",n,"elements : ")
for i in range(n):
    elem=input()
    lst.append(elem)
A=set(lst)

c=int
while(c!=5):
    c=int(input("Enter 1)Add 2)Remove 3)Sort 4)Clear 5)Exit : "))

    if(c==1):
        elem=input("Enter element that is to be added : ")
        A.add(elem)
        print(A)
    if(c==2):
        elem = input("Enter element that is to be removed : ")
        A.remove(elem)
        print(A)
    if(c==3):
        print("Sorted set : ",sorted(A))
    if(c==4):
        A.clear()
        print(A)
    if(c==5):
        exit()
