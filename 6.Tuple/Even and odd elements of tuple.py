lst=[]

n=int(input("Enter no. of elements : "))
print("Enter elements : ")

for i in range(0,n):
    num=int(input())
    lst.append(num)

tupl=tuple(lst)

print("Even tuple elements : ")
for i in tupl:
    if (i%2==0):
        print(i)

print("Odd tuple elements : ")
for i in tupl:
    if (i%2==1):
        print(i)
