
list1=[]
n=int(input("Enter no. of elements : "))
print("Enter numbers : ")

for i in range(0,n):
    n = int(input())
    list1.append(n)

print("List : ",list1)

print("Even elements : ")
for i in list1:
    if (i % 2 == 0):
        print(i,end=" , ")

print("\n")

print("Odd elements : ")
for k in list1:
    if (k % 2 == 1):
        print(k,end=" , ")




