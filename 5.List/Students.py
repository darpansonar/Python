n=int(input("Enter no. of students : "))
list=[]
print("Enter marks of each student")
for i in range (n):
    num=int(input())
    list.append(num)

print("List of marks = ",list)
print("Total marks : ",sum(list))
print("Average marks : ",(sum(list))/n)
print("Max marks : ",max(list))
print("Min marks : ",min(list))
