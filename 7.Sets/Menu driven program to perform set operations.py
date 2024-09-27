lst1=[]
lst2=[]

n1=int(input("Enter no. of elements in set A : "))
print("Enter",n1,"elements : ")
for i in range(n1):
    elem=input()
    lst1.append(elem)
A=set(lst1)

n2=int(input("Enter no. of elements in set B : "))
print("Enter",n2,"elements : ")
for i in range(n2):
    elem=input()
    lst2.append(elem)
B=set(lst2)

print("Set A =",A)
print("Set B =",B)

c=int
while(c!=4):
    c=int(input("\nEnter 1)Union 2)Intersection 3)Set Diff. 4)Exit : "))

    if(c==1):
        print("A | B = ",A|B)
    elif (c == 2):
        print("A & B = ", A & B)
    elif (c == 3):
        print("A - B = ", A - B)
    elif (c == 4):
        exit()
    else:
        print("Wrong input")
