lst=[]

n=int(input("Enter no. of elements : "))
print("Enter elements : ")

for i in range(0,n):
    x=input()
    lst.append(x)

elem=input("Enter element that is to be searched : ")

tupl=tuple(lst)
print("Tuple =",tupl)

if elem in tupl:
    for i in range(n):
        if elem==tupl[i]:
            print(elem,"found at location",i+1)
else:
    print(elem,"not found in tuple")
