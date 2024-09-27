list=[]
n=int(input("Enter no. of employees : "))

print("Enter salary of each employee : ")
for i in range(0,n):
    salary=int(input())
    list.append(salary)

print("List of salary of employees : ",list)

print("Sum of salaries of all employees : ",sum(list))

list.sort(reverse=True)
print("Sorted list : ",list)

print("1st Highest salary : ",list[0])
print("2nd Highest salary : ",list[1])
print("3rd Highest salary : ",list[2])