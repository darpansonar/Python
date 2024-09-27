lst=[]

n=int(input("Enter no. of elements : "))
print("Enter elements : ")

for i in range(0,n):
    num=int(input())
    lst.append(num)

tupl=tuple(lst)
print("Tuple =",tupl)
print("Max =",max(tupl))
print("Min =",min(tupl))
print("Sum =",sum(tupl))