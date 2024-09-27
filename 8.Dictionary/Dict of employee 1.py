empl={}
lst=[]

n=int(input("Enter no. of employees : "))
for i in range(n):
    name=input("\nEnter name : ")
    sal = int(input("Enter salary in Rs : "))
    empl.update({name:sal})

print("\nDict of employee with name as key and Salary as value : ",empl)

for i in empl:
    lst.append(empl[i])

print("Sum of salaries = Rs",sum(lst))
print("Highest salary =",max(lst))

target_value=max(lst)
for key,value in empl.items():
    if value==target_value:
        print("Employee with highest salary =",key)




