lst=[]
n=int(input("Enter no. of elements : "))
print("Enter elements : ")

for i in range(n):
    elem=input()
    lst.append(elem)

A=set(lst)
print("Set = ",A)
