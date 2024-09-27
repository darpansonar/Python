lst=[]

n=int(input("Enter no. of elements : "))
print("Enter elements : ")

for i in range(0,n):
    num=input()
    lst.append(num)

print("List =",lst)

tupl=tuple(lst)

print("Tuple =",tupl)

print("Elements of tuple : ")

for i in tupl:
    print(i,end=" , ")